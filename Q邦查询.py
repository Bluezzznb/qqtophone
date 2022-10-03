#!/bin/python3
from email import message
from email.errors import MultipartInvariantViolationDefect
import json
from turtle import ht
from webbrowser import get
import requests
import re
import os
def httpcode(url):
    gethttp = requests.get(url)
    if gethttp.status_code == 200:
        print ('服务器连接成功!')
        httpcode = re.findall('"status":(.*?),',gethttp.text)
        if httpcode[0] == '200':
            getqq(url)
        else:
            print ('未找到该用户信息')
            os.system("pause")

def getqq(url):
    gethttp = requests.get(url)
    qq = re.findall('"qq":(.*?),',gethttp.text)
    phone = re.findall('"phone":(.*?),',gethttp.text)
    phonediqu = gethttp.text.split('"')[17]
    print ('[+]查询成功!')
    print('\nQQ:',qq[0],'\nQQ绑定的电话号码:',phone[0],'\n号码属地:',phonediqu,'\n')
    os.system("pause")
    
if __name__ == '__main__':
    print ('<Q绑查询>\n')
    url1 = input("你要查询的QQ>")
    url2 = 'https://zy.xywlapi.cc/qqapi?qq='+url1
    print ('[*]正在连接服务器')
    httpcode(url2)
    pass
