import json
import requests

resp = requests.get('http://api.tianapi.com/allnews/index?key=6108db9f49b44a21f43304eb78af39f6&num=10&col=7')
newslist = json.loads(resp.text)['newslist']
result =[]
data = './语法基础/Day11/data.json'
for news in newslist:
    temp_dict = {}
    temp_dict['title'] = news['title']
    temp_dict['pic_url'] = news['picUrl']
    temp_dict['time'] = news['ctime']
    temp_dict['description'] = news['description']
    temp_dict['url'] = news['url']
    result.append(temp_dict)
with open(data,'w') as f:
    json.dump(result,f)