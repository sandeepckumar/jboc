import sys
from getpass import getuser

import click
import os

from src.commands.user_management import add_user
from src.commands.user_management import get_user
from src.commands.deployments.standalone import get_standalone_deployment


class HiddenPassword(object):
    def __init__(self, password=""):
        self.password = password

    def __str__(self):
        return "*" * len(self.password)


@click.group()
@click.option("-h", "--url", type=str, default="", help="jboss management url")
@click.option("--username", "-u", prompt=True, default=getuser(),
              help="username for connecting to jboss management api")
@click.option("--password", "-p", prompt=True, default=HiddenPassword(os.environ.get("PASSWORD", "")),
              hide_input=True, help="password for connecting to jboss management api")
@click.option("--verify", "-v", default=False, help="verify SSL connection/certs", show_default=True)
@click.option("--certs", "-c", default="", help="ca cert path, valid only if verify is TRUE")
@click.version_option(version="0.1.0", package_name="jboc", prog_name="jboc", help="shows version package_name "
                                                                                   "prog_name")
@click.pass_context
def cli(ctx, url, username, password, verify, certs):
    """An adhoc Jboss Command Line Utility, to make your life easy."""
    if isinstance(password, HiddenPassword):
        password = password.password
    ctx.ensure_object(dict)
    ctx.obj["url"] = url
    ctx.obj["username"] = username
    ctx.obj["password"] = password
    ctx.obj["verify"] = verify
    ctx.obj["certs"] = certs



# user management

cli.add_command(get_user.get_user)
cli.add_command(add_user.add_user)
cli.add_command(get_standalone_deployment.get_standalone_deployment)
