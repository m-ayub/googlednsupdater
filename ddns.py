#!/usr/bin/env python

from __future__ import print_function
import requests
import mycredentials

api_host = 'domains.google.com/nic/update?'
domain = mycredentials.hostname
username = mycredentials.username
password = mycredentials.password
ip = requests.get('http://ipv4.icanhazip.com')
my_ip = ip.text

api_call = "https://{}:{}@{}hostname={}&myip={}".format(username, password, api_host, domain, my_ip)

print(api_call)

send_update = requests.post(api_call)
print(send_update)
