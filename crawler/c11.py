import requests
#ip地址归属地查询
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + '202.202.202.100')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
