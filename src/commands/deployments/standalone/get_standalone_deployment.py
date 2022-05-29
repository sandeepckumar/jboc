from src.apis.deployments.standalone import get_standalone_deployment_api
import click
from src.models import request

@click.command()
@click.pass_context
def get_standalone_deployment(ctx):
    """Lists all deployments for standalone profile"""
    req = request(username=ctx.obj.get("username"),
                  url=ctx.obj.get("url"),
                  password=ctx.obj.get("password"),
                  verify=ctx.obj.get("verify"),
                  certs=ctx.obj.get("certs"),
                  payload=None)
    result = get_standalone_deployment_api.get_standalone_deployment_api(req)
    return result