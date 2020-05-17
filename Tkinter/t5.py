from tkinter import *
from tkinter import scrolledtext

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#文本域
txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.insert(INSERT,'You text goes here')
# txt.delete(1.0,END)
txt.grid(column=0,row=0)

#保持窗口
window.mainloop()