#!/usr/bin/env python3
import requests
response = requests.post("http://ip-api.com/batch", json=[
    {"query": input("put in the ip:\n")}
]).json()
for ip_info in response:
    for k, v in ip_info.items():

        print(k, v)
    print('\n')
