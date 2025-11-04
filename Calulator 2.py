from tkinter import *

expression=""

def equal():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression=""
def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)
def clear():
    global expression
    equation.set("")
    expression=""

if __name__=='__main__':
    window = Tk()
    window.geometry("250x250")
    window.title("Tutorial")

    equation = StringVar()

    entry = Entry(window,textvariable = equation)
    entry.grid(row=2,column=6)

    button0=Button(window,text=0,command=lambda:press(0),height=1,width=5)
    button0.grid(row=0,column=1)
    button1 = Button(window, text=1, command=lambda:press(1))
    button1.grid(row=1,column=0)
    button2 = Button(window, text=2, command=lambda:press(2))
    button2.grid(row=1,column=1)
    button3 = Button(window, text=3, command=lambda:press(3))
    button3.grid(row=1,column=2)
    button4 = Button(window, text=4, command=lambda:press(4))
    button4.grid(row=2,column=0)
    button5 = Button(window, text=5, command=lambda:press(5))
    button5.grid(row=2,column=1)
    button6 = Button(window, text=6, command=lambda:press(6))
    button6.grid(row=2,column=2)
    button7 = Button(window, text=7, command=lambda:press(7))
    button7.grid(row=3,column=0)
    button8 = Button(window, text=8, command=lambda:press(8))
    button8.grid(row=3,column=1)
    button9 = Button(window, text=9, command=lambda:press(9))
    button9.grid(row=3,column=2)
    buttonadd = Button(window, text='+', command=lambda:press('+'))
    buttonadd.grid(row=0,column=4)
    buttonsub = Button(window, text='-', command=lambda:press('-'))
    buttonsub.grid(row=1,column=4)
    buttonmul = Button(window, text='*', command=lambda:press('*'))
    buttonmul.grid(row=2,column=4)
    buttondiv = Button(window, text='/', command=lambda:press('/'))
    buttondiv.grid(row=3,column=4)
    buttoneq = Button(window, text='=', command = equal)
    buttoneq.grid(row=4,column=2)
    buttonclr = Button(window, text='C', command = clear)
    buttonclr.grid(row=4,column=3)

window.mainloop()
    
