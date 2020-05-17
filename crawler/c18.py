import requests
import re

def getHTMLText(url):
    headers={
        'cookie': '__wpkreporterwid_=4f0c4347-9199-4cdd-a804-91dd697afb40; ctoken=-DcQv9o27rCwIjXlY56ZdpnX; _m_h5_tk=6a81e5bc34e2314d8bcecffc72463571_1586018784062; _m_h5_tk_enc=444e0b48a49bbac92a8999b9b3581718; cna=gZIAFyDNcWICAXZ4ZGTAt6io; _samesite_flag_=true; cookie2=1307d5885fd98aead25e8e1d0ac0e7d0; t=fa764485392c86bb9b66657179e192d6; _tb_token_=e5eb10b77e31; tfstk=c-2CB0vDXeYQxkY-CysZTMerPgMRZ7Qsj6gLA5Bj9VWhxDECiv9qlRTUZFvtMc1..; unb=2784618912; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UU8A4oh%2FDURtcg%3D%3D&vt3=F8dBxdAUy1Y9fZKx9uQ%3D&nk2=0Xn7guMjqvI%3D; csg=4999a51f; lgc=%5Cu4E0D%5Cu95F2%5Cu7684%5Cu96E8; cookie17=UU8A4oh%2FDURtcg%3D%3D; dnk=%5Cu4E0D%5Cu95F2%5Cu7684%5Cu96E8; skt=e0672d7b98a37674; existShop=MTU4NjAxMDkxNQ%3D%3D; uc4=id4=0%40U22HvyB9CCGzSLd8TyYIyCKQ2fwK&nk4=0%4000HQOXkUgYC%2BrLmQ%2Fp85i2xeaQ%3D%3D; tracknick=%5Cu4E0D%5Cu95F2%5Cu7684%5Cu96E8; _cc_=UIHiLt3xSw%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E9%9B%A820; _nk_=%5Cu4E0D%5Cu95F2%5Cu7684%5Cu96E8; cookie1=BvXj4mzcfI7PUow3ACRqjXjqU2PtTWgTa8QgZpRAtbA%3D; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTUPOTz3K6eZg%3D%3D&lng=zh_CN; mt=ci=0_1; v=0; thw=cn; isg=BGVlWSmoV-xIKbMwTRWzCEYkdCGfohk0ndex4GdK8hyrfobwJPOJBLwWDOII-DHs; l=dBjXD_X7QXOYYiWbBOfZ5xo4mZQ9aIRf1rVyuqLXAICP_kfJ5mA1WZftni8vCnGVH6-kz35mgkfMBJYFfydKnxv9-b293OHmndC..',
             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    try:
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt,html):
    #正则表达式获取商品名称和商品价格
    try:
#使用正则表达式，\表示引入一个"view_price"的键，后面\引入键的值
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
#*？表示最小匹配
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price,title])
    except:
        print(" ")
def printGoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for x in ilt:
        count = count + 1
        print(tplt.format(count,x[0],x[1]))
def main():
    goods = '内裤'
    depth = 2
    star_url = 'https://s.taobao.com/search?q=' +goods
    infoList = []
    for i in range(depth):
        try:
            url = star_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodslist(infoList)
main()