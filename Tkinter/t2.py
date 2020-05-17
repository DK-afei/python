from tkinter import *
from tkinter.ttk import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#组合框
combo = Combobox(window)
combo['values']=(1,2,3,4,5, "Text")
combo.current(1)
combo.grid(column=0, row=0)

#保持窗口
window.mainloop()