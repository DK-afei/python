from tkinter import *
import tkinter as tk
from functools import partial

#计算函数
def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)*int(num2)
    label_result.config(text="Result = %d"%result)
    return

#开窗口
window = Tk()
window.title("Calculator")
window.geometry('400x200+100+200')

#简易计算器
number1 = tk.StringVar()
number2 = tk.StringVar()
labelNum1 = tk.Label(window, text="A").grid(row=1, column=0)
labelNum2 = tk.Label(window, text="B").grid(row=2, column=0)
labelResult = tk.Label(window)
labelResult.grid(row=7, column=2)
entryNum1 = tk.Entry(window, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(window, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
buttonCal = tk.Button(window, text="Calculate", command=call_result).grid(row=3, column=0)

#保持窗口
window.mainloop()
