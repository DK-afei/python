from tkinter import filedialog
from os import path

# dir = filedialog.askdirectory()#指定目录

#指定初始目录为该程序文件所在的目录
# file = filedialog.askopenfilename(initialdir=path.dirname(__file__))


file = filedialog.askopenfile()#单个文件



# files = filedialog.askopenfilenames()#多个文件



#指定文件类型(过滤器文件扩展名）
# file = filedialog.askopenfilename(filetypes = (("text files","*.txt"),("all files","*.*")))

