from calm.dsl.builtins import (
    ref,
    basic_cred,
    secret_cred,
    CalmVariable,
    CalmTask,
    action,
)
from calm.dsl.builtins import Service, Package, Substrate
from calm.dsl.builtins import Deployment, Profile, Blueprint
from calm.dsl.builtins import read_provider_spec, read_local_file, read_spec

CRED_USERNAME = read_local_file(".tests/username")
CRED_PASSWORD = read_local_file(".tests/password")
DNS_SERVER = read_local_file(".tests/dns_server")


class AhvService(Service):
    """Sample mysql service"""

    ENV = CalmVariable.Simple("DEV")


class AhvPackage(Package):
    """Example package with variables, install tasks and link to service"""

    foo = CalmVariable.Simple("bar")
    services = [ref(AhvService)]

    @action
    def __install__():
        CalmTask.Exec.ssh(name="Task1", script="echo @@{foo}@@")


class AhvSubstrate(Substrate):
    """AHV VM config given by reading a spec file"""

    provider_spec = read_provider_spec("specs/ahv_provider_spec.yaml")
    editables = read_spec("specs/ahv_substrate_editable.yaml")


class AhvDeployment(Deployment):
    """Sample deployment pulling in service and substrate references"""

    packages = [ref(AhvPackage)]
    substrate = ref(AhvSubstrate)


class DefaultProfile(Profile):
    """Sample application profile with variables"""

    nameserver = CalmVariable.Simple(DNS_SERVER, label="Local DNS resolver")
    foo1 = CalmVariable.Simple("bar1", runtime=True)
    foo2 = CalmVariable.Simple("bar2", runtime=True)

    deployments = [AhvDeployment]

    @action
    def test_profile_action():
        """Sample description for a profile action"""
        CalmTask.Exec.ssh(name="Task5", script='echo "Hello"', target=ref(AhvService))


class TestRuntime(Blueprint):

    credentials = [
        basic_cred(CRED_USERNAME, CRED_PASSWORD, default=True)
    ]
    services = [AhvService]
    packages = [AhvPackage]
    substrates = [AhvSubstrate]
    profiles = [DefaultProfile]
