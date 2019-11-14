import requests
import re
from bs4 import BeautifulSoup

r = requests.get('http://www.baidu.com')
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

# print(soup.a.attrs)
# print(soup.prettify())   # 格式化
# print(soup.a.prettify())
print(soup(string =re.compile('a')))
