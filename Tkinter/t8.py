from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#进度条
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70#设置进度条
bar.grid(column=0, row=0)


#保持窗口
window.mainloop()