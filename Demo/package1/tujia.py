#!/usr/bin/python

# -*- coding: gbk -*
import requests
r = requests.get('https://2.taobao.com/')
print(r.text)

#print(r.text.encode(r.encoding).decode('utf-8'))
#print(r.json())
#print(r.content)