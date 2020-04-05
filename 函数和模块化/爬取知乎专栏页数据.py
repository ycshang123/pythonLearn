"""
爬取知乎专栏粉丝
"""
import requests
import csv
import json
def crawl():
    url = "https://www.zhihu.com/api/v4/columns/NewsFlash/followers" 
    # 必须指定UA，否则知乎服务器会判定请求不合法
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"
    }
    csvfile = open('./file/zhihu.csv',"w",newline='')
    writer = csv.writer(csvfile,delimiter=',',quoting=csv.QUOTE_ALL)
    keys = ['is_followed','avatar_url_template','user_type','is_following','type','name']
    writer.writerow(keys)
    for i in range(10000):
      # 查询参数
        params ={ 
         "limit": 20,
         "offset": i,
         "include": "data[*].follower_count,gender,is_followed,is_following"   
    }
        response = requests.get(url,headers=headers,params=params)
        print("请求URL:",response.url)
        print("返回数据:",response.text)
    # 解析返回的数据
    j = 1
    for dic in response.json().get("data"):
        writer.writerow([dic['is_followed'],dic['avatar_url_template'],dic['user_type'],
            dic['is_following'],dic['type'],dic['is_following'],dic['type'],dic['name']])
        j += 1
    csvfile.close()

if __name__ == '__main__':
    crawl()