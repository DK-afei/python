from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x250')

#信息窗口，place函数的使用
name = Label(window, text = "Name").place(x=30, y=50)
email = Label(window, text = "Email").place(x=30, y=90)
password = Label(window, text = "Password").place(x=30, y=130)
submit = Button(window, text = "Submit", activebackground = "pink", activeforeground="blue").place(x=30, y=170)
e1 = Entry(window).place(x=80, y=50)
e2 = Entry(window).place(x=80, y=90)
e3 = Entry(window).place(x=95, y=130)

#保持窗口
window.mainloop()