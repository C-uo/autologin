# _*_coding:utf-8_*_
# !usr/bin/env python

import requests

url = r"https://webauth.ritsumei.ac.jp/login.html"
s = requests.Session()  # cookie

payload = {
        'buttonClicked': '4',
        'err_flag': '0',
        'info_flag': '0',
        'network_name': 'Guest Network',
        'username': 'your_username',
        'password': 'your_password'}

r = s.post(url, data=payload)
print(r.text)