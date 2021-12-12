import click


@click.command()
@click.pass_context
def add_user(ctx):
    """Provision RBAC user with a specific role"""
    click.echo(ctx.obj)

