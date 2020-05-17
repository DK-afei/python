from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('200x250')

def open():
    top = Toplevel(window)
    top.mainloop()

#打开另外一个窗口
btn = Button(window, text = "open", command = open)

btn.place(x=75, y=50)





#保持窗口
window.mainloop()