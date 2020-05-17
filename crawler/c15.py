import requests
from bs4 import BeautifulSoup
#基于bs4库的HTML的格式化和编码
# r = requests.get("http://python123.io/ws/demo.html")
# demo = r.text
# soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
# print(soup.a.prettify())
soup = BeautifulSoup("<p>中文</p>", "html.parser")
print(soup.p.string)
print(soup.p.prettify())
