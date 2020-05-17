import requests
from bs4 import BeautifulSoup
#基于bs4库的HTML的内容遍历方法
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")


#标签树的下行遍历
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[1])

#遍历儿子节点
# for child in soup.body.children:
#     print(child)

#遍历子孙节点
# for child in soup.body.descendants:
#     print(child)

#标签树的上行遍历
# print(soup.title.parent)
# print(soup.html.parent)
# print(soup.parent)

# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)

#标签树的平行遍历
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.next_sibling)
# print(soup.a.previous_sibling)
# print(soup.a.previous_sibling.previous_sibling)
# print(soup.a.parent)

#b遍历后续节点
# for sibling in soup.a.next_siblings:
#     print(sibling)
#遍历前续节点
# for sibling in soup.a.previous_siblings:
#     print(sibling)
