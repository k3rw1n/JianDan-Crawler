#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import time
import random
import os


def fetchimg(link):
    # r.get(link)
    filename = './pic/laosiji-' + \
        ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))+'.'+link.split('.').pop()
    img = open(filename, 'wb')
    img.write(r.get(link, headers=xx).content)
    img.close()


url = "http://jandan.net/ooxx/"
r = requests.session()
# xx = {'User-Agent':
#       'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
xx = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
      'referer': 'http://jandan.net/',
      'Upgrade-Insecure-Requests': '1',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Encoding': 'gzip, deflate, sdch',
      'Accept-Language': 'zh-CN,zh;q=0.8',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'DNT': '1'
      }


for i in range(10):
    r.get(url, headers=xx)
    html = r.get(url, headers=xx).content
    # print html
    if "屏蔽提示" in html:
        print "请先绕过防爬虫校验"
        f = open(r'C:\Users\Kerwin\AppData\Local\Temp\temp.html', 'w')
        f.write(html)
        os.system(r'C:\Users\Kerwin\AppData\Local\Temp\temp.html')
        exit(0)
    soup = BeautifulSoup(html)
    # print soup.prettify

    if not os.path.exists('pic'):
        os.mkdir('pic')
    for href in soup.find_all(href=re.compile('http\:\/\/ww\d\.sina.*')):
        print href.get('href')
        fetchimg(href.get('href'))
    time.sleep(1)
    url = BeautifulSoup(requests.get(url, headers=xx).text).find(
        'a', {'class': 'previous-comment-page'}).get('href')
