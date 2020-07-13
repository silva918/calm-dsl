from calm.dsl.config import print_config
from .main import show


@show.command("config", invoke_direct=True)
def show_config():
    print_config()
