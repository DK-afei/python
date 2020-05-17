from tkinter import *

def select():
    sel = "Value = " + str(v.get())
    label.config(text = sel)
#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('200x250')


#scale量表
v = DoubleVar()
scale = Scale(window, variable = v, from_=1, to=50, orient = HORIZONTAL)
scale.pack(anchor=CENTER)

btn = Button(window, text="Value", command=select)
btn.pack(anchor=CENTER)

label = Label(window)
label.pack()

#保持窗口
window.mainloop()
