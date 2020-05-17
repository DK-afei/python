from tkinter import *
from tkinter import messagebox

#开窗口
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')


#创建一个普通信息框
#按钮事件
def clicked1():
    messagebox.showinfo('information', 'Information')
btn1 = Button(window,text='showinfo', command=clicked1)
btn1.grid(column=0,row=0)

#创建一个警告提示信息框
#按钮事件
def clicked2():
    messagebox.showwarning('warning', 'Warning')
btn2 = Button(window,text='showwarning', command=clicked2)
btn2.grid(column=1,row=0)

#创建一个错误提示信息框
#按钮事件
def clicked3():
    messagebox.showerror('error', 'Error')
btn3 = Button(window,text='showerror', command=clicked3)
btn3.grid(column=2,row=0)

'''
如果单击“确定”或“是”或“重试”，它将返回True值，
但是如果选择“否”或“取消”，它，将返回False，
返回三个值之一的唯一函数是askyesnocancel函数，
它返回True或False或None
'''

#创建一个问题提示信息框
#按钮事件
def clicked4():
    messagebox.askquestion('Confirm', 'Are you sure?')
btn4 = Button(window,text='askquestion', command=clicked4)
btn4.grid(column=3,row=0)

#创建一个yesno提示信息框
#按钮事件
def clicked5():
    messagebox.askyesno('Application', 'Got It?')
btn5 = Button(window,text='askyesno', command=clicked5)
btn5.grid(column=0,row=1)

#创建一个yesnocancel提示信息框
#按钮事件
def clicked6():
    messagebox.askyesnocancel('Message title', 'Message content')
btn6 = Button(window,text='askyesnocancel', command=clicked6)
btn6.grid(column=1,row=1)

#创建一个是否取消提示信息框
#按钮事件
def clicked7():
    messagebox.askokcancel('Redirect', 'Redirecting you to www.ooo.com')
btn7 = Button(window,text='askokcancel', command=clicked7)
btn7.grid(column=2,row=1)

#创建一个重试提示信息框
#按钮事件
def clicked8():
    messagebox.askretrycancel('Application', 'try again?')
btn8 = Button(window,text='askretrycancel', command=clicked8)
btn8.grid(column=3,row=1)




#保持窗口
window.mainloop()