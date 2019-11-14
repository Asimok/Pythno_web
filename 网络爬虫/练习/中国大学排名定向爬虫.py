import bs4
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            if tds.__len__()>1:
                ulist.append([tds[0].string, tds[3].string, tds[6].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:{4}^10}"
    print(tplt.format("排名", "学校名称", "总分",chr(12288),chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2],chr(12288),chr(12288)))
    print("Suc" + str(num))


if __name__ == '__main__':
    uinfo = []
    url = 'http://www.zuihaodaxue.com/BCSR/jisuanjikexueyujishu2019.html'
    # url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
