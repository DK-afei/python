from tkinter import *
from tkinter import Menu

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#按钮事件
def clicked1():
    print('new1')

def clicked2():
    print('new2')


#菜单
menu = Menu(window)
#第一个主菜单项
new_item1 = Menu(menu, tearoff=0)#去掉虚线
new_item1.add_command(label='New1', command = clicked1)
new_item1.add_separator()
new_item1.add_command(label='Edit1')
new_item1.add_separator()
new_item1.add_command(label='hello1')
menu.add_cascade(label='File1', menu=new_item1)

#第二个主菜单项
new_item2 = Menu(menu, tearoff=0)#去掉虚线
new_item2.add_command(label='New2', command = clicked2)
new_item2.add_separator()
new_item2.add_command(label='Edit2')
new_item2.add_separator()
new_item2.add_command(label='hello2')
menu.add_cascade(label='File2', menu=new_item2)

#第三个主菜单项
menubar = Menu(menu, tearoff=0)#去掉虚线
menubar.add_command(label="Quit!", command=window.quit)
menu.add_cascade(label='third', menu=menubar)

#窗口设置菜单
window.config(menu=menu)



#保持窗口
window.mainloop()