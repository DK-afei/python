import  requests
from bs4 import  BeautifulSoup
#BeautifulSoupt库的基本元素
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, "html.parser")
tag  = soup.a
print(soup.title)
print(tag)

# print(soup.a.name)
# print(soup.a.parent.name)
# print(soup.a.parent.parent.name)

# print(tag.attrs)
# print(tag.attrs['class'])
# print(tag.attrs['href'])
# print(type(tag.attrs))
# print(type(tag))

# print(soup.a)
# print(soup.a.string)
# print(soup.p)
# print(soup.p.string)
# print(type(soup.p.string))

# newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is a comment</p>", "html.parser")
# print(newsoup.b.string)
# print(type(newsoup.b.string))
# print(newsoup.p.string)
# print(type(newsoup.p.string))




