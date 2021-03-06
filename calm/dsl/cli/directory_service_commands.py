import click

from .directory_services import get_directory_services
from .main import get


@get.command("directory_services")
@click.option(
    "--name", "-n", default=None, help="Search for directory services by name"
)
@click.option(
    "--filter",
    "filter_by",
    "-f",
    default=None,
    help="Filter directory services by this string",
)
@click.option("--limit", "-l", default=20, help="Number of results to return")
@click.option(
    "--offset", "-s", default=0, help="Offset results by the specified amount"
)
@click.option(
    "--quiet",
    "-q",
    is_flag=True,
    default=False,
    help="Show only directory service names",
)
@click.option(
    "--out",
    "-o",
    "out",
    type=click.Choice(["text", "json"]),
    default="text",
    help="output format",
)
def _get_directory_services(name, filter_by, limit, offset, quiet, out):
    """Get directory services, optionally filtered by a string"""

    get_directory_services(name, filter_by, limit, offset, quiet, out)
