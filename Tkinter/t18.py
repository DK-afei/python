from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('140x100')
frame = Frame(window)
frame.pack()

#frame的使用
leftframe = Frame(window)
leftframe.pack(side = LEFT)

rightframe = Frame(window)
rightframe.pack(side = RIGHT)

btn1 = Button(frame, text="Submit", fg="red", activebackground = "red")
btn1.pack(side = LEFT)

btn2 = Button(frame, text="Remove", fg="brown", activebackground = "brown")
btn2.pack(side = RIGHT)

btn3 = Button(rightframe, text="Add", fg="blue", activebackground = "blue")
btn3.pack(side = LEFT)

btn4 = Button(leftframe, text="Modify", fg="black", activebackground = "white")
btn4.pack(side = RIGHT)

#保持窗口
window.mainloop()

