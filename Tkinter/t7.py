from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#数字小部件
#设置默认值
var = IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
# spin = Spinbox(window,from_=0, to=100, width=5)
# spin = Spinbox(window, values=(3,8,11), width=5)#初始化指定数字
spin.grid(column=0,row=0)



#保持窗口
window.mainloop()