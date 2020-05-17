from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#pack函数的使用
redbutton = Button(window, text="Red", fg="red")
redbutton.pack(side=LEFT)
greenbutton = Button(window, text="Black", fg="black")
greenbutton.pack(side=RIGHT)
bluebutton = Button(window, text="Blue", fg="blue")
bluebutton.pack(side=TOP)
blackbutton = Button(window, text="Green", fg="red")
blackbutton.pack(side=BOTTOM)

#保持窗口
window.mainloop()
