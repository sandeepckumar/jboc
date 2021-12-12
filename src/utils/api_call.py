import requests
from collections import namedtuple
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def api_call(req):
    timeout = 5
    headers = {
        "Content-type": "application/json; charset=utf-8",
        "Accept": "application/json"
    }
    res = namedtuple("response", "result error")
    url = req.url.strip("/") + "/management"

    try:
        result = requests.post(url, auth=(req.username, req.password), data=json.dumps(req.payload),
                               verify=req.verify, headers=headers, timeout=timeout)
        response = res(result=result, error=None)
        return response
    except Exception as e:
        response = res(result=None, error=e)
        return response


if __name__ == "__main__":
    from getpass import getpass

    request = namedtuple("request", "url username password verify payload")
    url = "https://usadevcatmdom01.cotiiti.com:9443"
    payload = {"operation": "read-children-resources",
               "child-type": "role-mapping",
               "recursive": "true",
               "address": ["core-service", "management", "access", "authorization"],
               "json.pretty": 1
               }
    username = "sandeep.chenna"
    password = getpass()
    verify = False
    req = request(url=url, username=username, password=password, verify=verify, payload=payload)
    result = api_call(req)
    print(result.error)
