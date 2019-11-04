import requests
r = requests.get('http://39.96.68.13:8080/SmartLockServer/servlet/AppControlServlet','username=mq&sessionId=CONN_9527&code=BBBB')
r = requests.get('http://39.96.68.13:8080/SmartLockServer/servlet/AppControlServlet','username=mq&sessionId=CONN_9527&code=AAAA')
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
r.encoding = 'utf-8'
print(r.text)
