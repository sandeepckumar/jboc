from collections import namedtuple

request = namedtuple("request", "url username password verify payload certs")
