from  tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('200x250')

#Listbox列表框
lbl = Label(window, text = "A list of favourite countries...")
listbox = Listbox(window)
listbox.insert(1,"India")
listbox.insert(2,"USA")
listbox.insert(3,"Japan")
listbox.insert(4,"Austrelia")
btn = Button(window, text = "delete", command = lambda listbox=listbox: listbox.delete(ANCHOR))

lbl.pack()
listbox.pack()
btn.pack()

#保持窗口
window.mainloop()