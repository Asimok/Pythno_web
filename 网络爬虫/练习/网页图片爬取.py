import os

import requests

# 网络图片爬取

url = 'https://img14.360buyimg.com/n4/jfs/t1/95706/11/1279/276153/5dbc1948Ebb1d6f48/e6318f80fa8d3146.jpg'
# root = '//home/mq//PycharmProjects//Pythno_web//网络爬虫//爬取图片//'
root ='爬取图片_inproject//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
        print('创建文件夹')
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        print(r.status_code)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
