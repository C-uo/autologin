# !usr/bin/env python
# _*_coding:utf-8_*_

import requests
import re
import time

username = ""
password = ""


def main():
    """
    每隔15秒检测一次网络是否畅通,并登录
    """
    login(username, password)
    while True:
        while monitor():
            login(username, password)
        time.sleep(15)


def login(name, pwd):
    """
    将表单丢给学校的登录页面
    """
    url = r"https://webauth.ritsumei.ac.jp/login.html"
    format_data = {
            'buttonClicked': '4',
            'err_flag': '0',
            'info_flag': '0',
            'network_name': 'Guest Network',
            'username': name, 
            'password': pwd
            }
    s = requests.Session()
    login = s.post(url, data=format_data)
    print(login.text)


def monitor():
    """
    用正则抓取对象页面的标题,以此来判断是否为学校的登录页面
    """
    check = requests.get(r"http://www.google.co.jp")
    pattern = re.compile(r"<TITLE>.*</TITLE>", re.I)
    title = re.search(pattern, check.text).group()
    return "web" in title


main()
