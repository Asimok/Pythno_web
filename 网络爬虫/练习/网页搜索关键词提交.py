import requests

# 百度搜索器引擎
try:
    url = 'http://www.baidu.com/s'
    kv = {'wd': 'python'}
    r = requests.get(url, params=kv)
    print(r.request.url)
    print(len(r.text))
    print(r.text[0:2000])
except:
    print('爬取失败')
