from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('200x250')

#滚动条
sb = Scrollbar(window)
sb.pack(side = RIGHT, fill = Y)

mylist = Listbox(window, yscrollcommand = sb.set)

for line in range(30):
    mylist.insert(END, "Number" + str(line))

mylist.pack(side = LEFT)
sb.config(command = mylist.yview())

#保持窗口
window.mainloop()