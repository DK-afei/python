from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x250')

#
labelframe1 = LabelFrame(window, text="Positive Comments")
labelframe1.pack(fill="both", expand="yes")

toplabel = Label(labelframe1, text="Place to put the positive comments")
toplabel.pack()

labelframe2 = LabelFrame(window, text="Negative Comments")
labelframe2.pack(fill="both", expand="yes")

bottomlabel = Label(labelframe2, text="Place to put the negative comments")

#保持窗口
window.mainloop()