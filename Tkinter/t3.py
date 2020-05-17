from tkinter import *
from tkinter.ttk import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('200x200')

#组合框
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
chkbtn1 = Checkbutton(window, text="C", variable=checkvar1, onvalue=1, offvalue=0, width=10)
chkbtn2 = Checkbutton(window, text="C++", variable=checkvar2, onvalue=1, offvalue=0, width=10)
chkbtn3 = Checkbutton(window, text="Java", variable=checkvar3, onvalue=1, offvalue=0, width=10)
chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()

#保持窗口
window.mainloop()