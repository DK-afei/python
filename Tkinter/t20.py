from tkinter import *

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('200x250')

#菜单按钮
menubutton = Menubutton(window, text = "Language", relief = FLAT)
menubutton.grid()
menubutton.menu = Menu(menubutton, tearoff=0)
menubutton["menu"]=menubutton.menu
menubutton.menu.add_checkbutton(label = "Hindi", variable=IntVar())
menubutton.menu.add_checkbutton(label = "English", variable = IntVar())
menubutton.pack()

#保持窗口
window.mainloop()