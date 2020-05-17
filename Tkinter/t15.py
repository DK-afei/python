from tkinter import *
from tkinter import messagebox

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x250')

#按钮函数
def fun():
    messagebox.showinfo("Hello", "red Button clicked")

#按钮实例
b1 = Button(window, text = "Red", command = fun, activeforeground = "red", activebackground = "pink", pady=10)
b2 = Button(window, text = "Blue", activeforeground = "blue", activebackground = "pink", pady=10)
b3 = Button(window, text = "Green", activeforeground = "green", activebackground = "pink", pady=10)
b4 = Button(window, text = "Yellow", activeforeground = "yellow", activebackground = "pink", pady=10)
b1.pack(side = LEFT)
b2.pack(side = RIGHT)
b3.pack(side = TOP)
b4.pack(side = BOTTOM)


#保持窗口
window.mainloop()

