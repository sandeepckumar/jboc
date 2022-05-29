from src.utils import api_call
from src.utils import parser
from src.apis.status_codes import codes
from src.models import request

import json

def payload():
    data = {
        "operation":"read-attribute",
        "address":[{"deployment":"*"}],
        "name":"enabled",
        "json.pretty": 1,
    }
    return data

def get_standalone_deployment_api(user_req):
    req = request(url=user_req.url, username=user_req.username, password=user_req.password,
                  payload=payload(), certs=user_req.certs, verify=user_req.verify)
    res = api_call.api_call(req)
    if res.error:
        return parser.parse_error(res.error)
    elif res.result.status_code in codes.keys():
        return parser.parse_error(codes[res.result.status_code])
    else:
        return parser.parse_get_deployment(res.result)


