#!/usr/bin/env python

from __future__ import print_function
from requests.auth import HTTPBasicAuth
import requests
import mycredentials


domain = mycredentials.hostname
username = mycredentials.username
password = mycredentials.password

url = 'domains.google.com/nic/update?'
ip = requests.get('http://ipv4.icanhazip.com')
headers = {'User-Agent': 'my_app/0.0.1', 'cache-control':'no-cache'}
my_ip = ip.text.strip()
mypayload = {'myip': my_ip}

api = "https://{}hostname={}".format(url, domain)

update = requests.post(api, auth=HTTPBasicAuth(username, password), headers=headers, data=mypayload)

print(update.status_code)
print(update.text)
