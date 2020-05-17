from tkinter import *
from tkinter import ttk

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#添加笔记本小部件
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
tab_control.add(tab3, text='third')
lbl1 = Label(tab1, text='label1', padx=5, pady=5)
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='label2')
lbl2.grid(column=0, row=0)
lbl3 = Label(tab3, text='label3')
lbl3.grid(column=0, row=3)
tab_control.pack(expand=False, fill='both')



#保持窗口
window.mainloop()