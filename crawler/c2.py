import requests
#爬虫通用爬取框架
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == '__main__':
    url = "http://www.baidu.com"
    url0 = "www.baidu.com"
    print(getHTMLText(url))