import tkinter as tk
from tkinter import *

def CreateWidgets():
    CalcDisplay = Entry(root, bd=10, justify="right", font=("Comic Sans MS", 20, "bold"), textvariable=d_value, bg="#ffffff")
    CalcDisplay.grid(row=0, column=0, columnspan=5)

    B_AllClear = Button(root, text="AC", bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=allclearEntry)
    B_AllClear.grid(row=1, column=0, padx=5, pady=5)

    B_Clear = Button(root, text="C", bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=clearEntry)
    B_Clear.grid(row=1, column=1, padx=5, pady=5)

    B_2 = Button(root, text='%', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick('%'))
    B_2.grid(row=1, column=2, padx=5, pady=5)

    B_D = Button(root, text='/', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick('/'))
    B_D.grid(row=1, column=3, padx=5, pady=5)

    B_7 = Button(root, text='7', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(7))
    B_7.grid(row=2, column=0, padx=5, pady=5)

    B_8 = Button(root, text='8', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(8))
    B_8.grid(row=2, column=1, padx=5, pady=5)

    B_9 = Button(root, text='9', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(9))
    B_9.grid(row=2, column=2, padx=5, pady=5)

    B_M = Button(root, text='*', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick('*'))
    B_M.grid(row=2, column=3, padx=5, pady=5)

    B_4 = Button(root, text='4', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(4))
    B_4.grid(row=3, column=0, padx=5, pady=5)

    B_5 = Button(root, text='5', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(5))
    B_5.grid(row=3, column=1, padx=5, pady=5)

    B_6 = Button(root, text='6', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(6))
    B_6.grid(row=3, column=2, padx=5, pady=5)

    B_D = Button(root, text='-', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick('-'))
    B_D.grid(row=3, column=3, padx=5, pady=5)

    B_1 = Button(root, text='1', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(1))
    B_1.grid(row=4, column=0, padx=5, pady=5)

    B_2 = Button(root, text='2', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(2))
    B_2.grid(row=4, column=1, padx=5, pady=5)

    B_3 = Button(root, text='3', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick(3))
    B_3.grid(row=4, column=2, padx=5, pady=5)

    B_A = Button(root, text='+', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick('+'))
    B_A.grid(row=4, column=3, padx=5, pady=5)

    B_0 = Button(root, text='0', bd=5,  font=("Comic Sans MS", 20, "bold"), width=10, height=2, command=lambda : buttonClick(0))
    B_0.grid(row=5, column=0, padx=5, pady=10, columnspan=2)

    B_DP = Button(root, text='.', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=lambda : buttonClick('.'))
    B_DP.grid(row=5, column=2, padx=5, pady=10)

    B_E = Button(root, text='=', bd=5,  font=("Comic Sans MS", 20, "bold"), width=4, height=2, command=calculateResult)
    B_E.grid(row=5, column=3, padx=5, pady=10)

def buttonClick(c_input):
    global c_expression
    c_expression = c_expression + str(c_input)
    d_value.set(c_expression)

def calculateResult():
    global c_expression
    result = str(eval(c_expression))
    d_value.set(result)

def allclearEntry():
    global c_expression
    c_expression = ""
    d_value.set(c_expression)

def clearEntry():
    global c_expression, d_value
    cleared_value =  d_value.get()[:-1]
    c_expression = cleared_value
    d_value.set(c_expression)

root = tk.Tk()

root.title('Calculator')
root.resizable(False, False)
root.configure(background="#ffffff")

d_value = StringVar()
c_expression = ""

CreateWidgets()
root.mainloop()