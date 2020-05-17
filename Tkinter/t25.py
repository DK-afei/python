from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('200x250')



def add():
    a = int(e1.get())
    b = int(e2.get())
    leftdata = ' ' + str(a+b)
    left.insert(0, leftdata)


#PanedWindow部件的使用
w1 = PanedWindow()
w1.pack(fill = BOTH, expand=1)

left = Entry(w1, bd=5)
w1.add(left)

w2 = PanedWindow(w1, orient = VERTICAL)
w1.add(w2)

e1 = Entry(w2)
e2 = Entry(w2)

w2.add(e1)
w2.add(e2)

bottom = Button(w2, text = "Add", command = add)
w2.add(bottom)

#保持窗口
window.mainloop()
