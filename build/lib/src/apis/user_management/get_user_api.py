from src.utils import api_call
from src.utils import parser
from src.apis.status_codes import codes
from src.models import request


def payload():
    data = {"operation": "read-children-resources",
            "child-type": "role-mapping",
            "recursive": "true",
            "address": ["core-service", "management", "access", "authorization"],
            "json.pretty": 1
            }
    return data


def get_user_call(user_req):
    req = request(url=user_req.url, username=user_req.username, password=user_req.password, verify=user_req.verify,
                  payload=payload(), certs=user_req.certs)
    res = api_call.api_call(req)
    if res.error:
        return parser.parse_error(res.error)
    elif res.result.status_code in codes.keys():
        return parser.parse_error(codes[res.result.status_code])
    else:
        return parser.parse_get_user(res.result)



