from .entity import EntityType, Entity
from .validator import PropertyValidator


class RunbookType(EntityType):
    __schema_name__ = "Runbook"
    __openapi_type__ = "app_runbook"

    def __call__(*args, **kwargs):
        pass

    @classmethod
    def pre_decompile(mcls, cdict, context=[]):

        cdict = super().pre_decompile(cdict, context=context)
        # Removing additional attributes
        cdict.pop("state", None)
        cdict.pop("message_list", None)
        return cdict


class RunbookValidator(PropertyValidator, openapi_type="app_runbook"):
    __default__ = None
    __kind__ = RunbookType


def _runbook(**kwargs):
    name = kwargs.get("name", None)
    bases = (Entity,)
    return RunbookType(name, bases, kwargs)


Runbook = _runbook()


def runbook_create(**kwargs):
    name = kwargs.get("name", kwargs.get("__name__", None))
    bases = (Entity,)
    return RunbookType(name, bases, kwargs)
