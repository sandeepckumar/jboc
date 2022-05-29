import click
from src.apis.user_management import add_user_api
from src.models import request
import sys


@click.command()
@click.pass_context
@click.option("--username", "-u", type=str, help="username to be added", required=True)
@click.option("--role", "-r", type=click.Choice(["Monitor", "Operator", "Maintainer", "Deployer", "Auditor",
                                                 "Administrator", "SuperUser"], case_sensitive=True),
              help="available roles [Monitor, Operator, Maintainer, Deployer, Auditor, "
                   "Administrator, SuperUser] (case-sensitive)", required=True)
def add_user(ctx, username, role):
    """Provision RBAC user with a specific role"""
    user_to_be_added = username
    req = request(username=ctx.obj.get("username"),
                  url=ctx.obj.get("url"),
                  password=ctx.obj.get("password"),
                  verify=ctx.obj.get("verify"),
                  certs=ctx.obj.get("certs"),
                  payload=None)
    result = add_user_api.add_user_call(req, user_to_be_added, role)
    return result
