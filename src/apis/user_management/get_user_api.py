from src.utils import api_call
from src.utils import parser
from collections import namedtuple


def payload():
    data = {"operation": "read-children-resources",
            "child-type": "role-mapping",
            "recursive": "true",
            "address": ["core-service", "management", "access", "authorization"],
            "json.pretty": 1
            }
    return data


def get_user_call(user_req):
    request = namedtuple("request", "url username password verify payload")
    req = request(url=user_req.url, username=user_req.username, password=user_req.password, verify=user_req.verify,
                  payload=payload())
    res = api_call.api_call(req)
    if res.error:
        return parser.parse_error(res.error)
    else:
        return parser.parse_get_user(res.result)


if __name__ == "__main__":
    request = namedtuple("request", "url username password verify")
    url = "https://usadevcatmdom01.cotiviti.com:9443"
    username = "sandeep.chenna"
    password = "Winter$56789"
    verify = False
    req = request(url=url, username=username, password=password, verify=verify)
    get_user_call(req)
