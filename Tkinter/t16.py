from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('200x200')

c = Canvas(window, bg = "pink", height = "200")
arc = c.create_arc((5,10,150,200), start=0, extent=150, fill = "white")

c.pack()

#保持窗口
window.mainloop()