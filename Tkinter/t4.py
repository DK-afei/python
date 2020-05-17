from tkinter import *
from tkinter.ttk import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#按钮事件1
def clicked1():
    print("hello")

#单选按钮
selected = IntVar()
rad1 = Radiobutton(window, text='First', value=1, variable=selected, command=clicked1)
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='Third', value=3, variable=selected)
#获取当前选择的item的值
def clicked():
        print(selected.get())
btn = Button(window, text="Click Me", command=clicked)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)



#保持窗口
window.mainloop()