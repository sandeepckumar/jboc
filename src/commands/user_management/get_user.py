from src.apis.user_management import get_user_api
import click
from src.models import request


@click.command()
@click.pass_context
def get_user(ctx):
    """Lists all RBAC users"""
    req = request(username=ctx.obj.get("username"),
                  url=ctx.obj.get("url"),
                  password=ctx.obj.get("password"),
                  verify=ctx.obj.get("verify"),
                  certs=ctx.obj.get("certs"),
                  payload=None
                  )
    result = get_user_api.get_user_call(req)
    return result


