from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#标签
# lab = Label(window, text = "Hello", font=("Arial Bold", 50))
lbl = Label(window, text = "Hello")
lbl.grid(column=0, row=0)

#文本框
txt = Entry(window, width=10)
# txt = Entry(window,width = 10, state = 'disabled' )#禁用
txt.grid(column=1, row=0)
txt.focus()#自动聚焦

#按钮点击事件
def clicked():
    # lbl.configure(text="Button was clicked!!")
    res = "Welcome to "+ txt.get()
    lbl.configure(text = res)

#按钮
# btn = Button(window, text="Click Me", bg="orange", fg="red")
btn = Button(window, text = "Click Me", command=clicked)
btn.grid(column=2, row=0)



#保持窗口
window.mainloop()