import  requests
from bs4 import  BeautifulSoup
#BeautifulSoup库安装后的测试
r = requests.get("http://python123.io/ws/demo.html")
print(r.text)
demo = r.text

soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())


