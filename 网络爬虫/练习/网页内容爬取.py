import requests

url = 'https://item.jd.com/100002749549.html'
try:
    kv = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[0:200])
except:
    print('爬取失败')
