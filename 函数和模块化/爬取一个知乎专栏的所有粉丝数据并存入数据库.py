"""
爬取知乎一个专栏的所有粉丝数据并存入数据库
"""
import requests
import json
import time
import pymysql
def crawl():
    followers_data = []
    for offset in range(2000,2200,20):
        time.sleep(1)
        url =""



