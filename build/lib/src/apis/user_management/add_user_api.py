import click

from src.utils import api_call
from src.utils import parser
from src.apis.status_codes import codes
from src.models import request


def payload(user_to_be_added, role):
    data = {
        "operation": "add",
        "include-runtime": "true",
        "address": [
            "core-service",
            "management",
            "access",
            "authorization",
            "role-mapping",
            role,
            "include",
            "user-{}".format(user_to_be_added)
        ],
        "name": user_to_be_added,
        "type": "USER"
    }
    return data


def add_user_call(user_req, user_to_be_added, role):
    req = request(url=user_req.url, username=user_req.username, password=user_req.password, verify=user_req.verify,
                  payload=payload(user_to_be_added, role), certs=None)
    res = api_call.api_call(req)
    if res.error:
        return parser.parse_error(res.error)
    elif res.result.status_code in codes.keys():
        return parser.parse_error(codes[res.result.status_code])
    elif res.result.status_code == 200:
        return click.echo("[{}] -- URL: {} -- USER: {} -- ROLE: {} -- Provisioned".format("SUCCESS", user_req.url,
                                                                                          user_to_be_added, role))
