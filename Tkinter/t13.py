from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#登陆窗口,grid用法
name = Label(window, text="Name").grid(row=0,column=0)
e1 = Entry(window).grid(row=0, column=1)
password = Label(window,text="Password").grid(row=1,column=0)
e2 = Entry(window).grid(row=1, column=1)
submit = Button(window, text="Submit").grid(row=4,column=0)

#保持窗口
window.mainloop()