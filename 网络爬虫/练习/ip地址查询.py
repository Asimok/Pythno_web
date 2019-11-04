import requests

try:
    url = 'http://m.ip138.com/ip.asp?ip='
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    print(r.text[-500:])  # 最后500个字节
except:
    print('爬取失败')