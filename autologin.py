#!/usr/bin/env python
# _*_coding:utf-8_*_

import requests
import re
import time


def main():
    """
    每隔5秒检测一次网络是否畅通,并登录
    """
    while True:
        while monitor():
            login(username, password)
            break
        time.sleep(5)


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
            'password': pwd,
            }
    access = requests.Session()
    try:
        access.post(url, data=format_data)
    except requests.exceptions.ConnectionError:
        print("网络错误")


def monitor():
    """
    用正则抓取对象页面的标题,以此来判断是否为学校的登录页面
    """
    try:
        check = requests.get(r"http://www.google.co.jp")
        pattern = re.compile(r"<TITLE>.*</TITLE>", re.I)
        title = re.search(pattern, check.text).group()
        return "Web Authentication" in title
    except requests.exceptions.ConnectionError:
        print("网络无连接")
        return False


# 将info写成字典也许会更好
try:
    with open("personal_info.txt") as personal_info:
        info = []
        lines = personal_info.readlines()
        for line in lines:
            info.append(line.rstrip())
        username, password = info[0], info[1]
except FileNotFoundError:
    username = (input("Enter your username, please:\n"))
    password = (input("Enter your password: \n"))
    with open("personal_info.txt", "w") as personal_info:
        personal_info.write(username + "\n")
        personal_info.write(password + "\n")
finally:
    main()
