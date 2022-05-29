import click
from src.utils import format_out


def parse_add_user():
    pass


def parse_error(e):
    click.echo(f"Error: {e}")


def parse_get_user(res):
    res_json = res.json()
    users_data = []
    for role, include_user in res_json["result"].items():
        for user in include_user["include"]:
            users_data.append([user.replace("user-", ""), role])
    output = format_out.format_out(table=users_data, headers=["Name", "Role"])
    click.echo(output)

def parse_get_deployment(res):
    res_json = res.json()
    for result in res_json["result"]:
        for address in result['address']:
            click.echo(address['deployment'])


