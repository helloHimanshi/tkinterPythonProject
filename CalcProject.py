from tkinter import *
import math

preval = ''


def get_variables(n):
    global preval
    currentval = preval + str(n)
    preval = currentval
    outputval.set(currentval)


def percentfunc(n):
    return n/100


def percent():
    global preval
    if preval == '':
        raise ValueError
    currentval = str(percentfunc(float(preval)))
    preval = currentval
    outputval.set(currentval)


def div(n):
    global preval
    if preval == '':
        raise ValueError
    currentval = preval + str(n)
    preval = currentval
    outputval.set(currentval)


def mul(n):
    global preval
    if preval == '':
        raise ValueError
    currentval = preval + str(n)
    preval = currentval
    outputval.set(currentval)


def sub(n):
    global preval
    if preval == '':
        raise ValueError
    currentval = preval + str(n)
    preval = currentval
    outputval.set(currentval)


def add(n):
    global preval
    currentval = preval + str(n)
    preval = currentval
    outputval.set(currentval)


def dec(n):
    global preval
    currentval = preval + str(n)
    preval = currentval
    outputval.set(currentval)


def ln():
    global preval
    if preval == '' or preval < '0':
        raise ValueError
    currentval = str(math.log(float(preval)))
    preval = currentval
    outputval.set(currentval)


def clear_all():
    global preval
    currentval = ''
    preval = currentval
    outputval.set(currentval)


def clear():
    global preval
    count = len(preval)
    currentval = ''
    for i in range(0, count-1):
        val = preval[i]
        currentval = currentval + val
    preval = currentval
    outputval.set(currentval)


def equal():
    global preval
    result = str(eval(preval))
    outputval.set(result)
    preval = result


def pi(n):
    global preval
    currentval = preval + str(float(n) * math.pi)
    preval = currentval
    outputval.set(currentval)


def sin():
    global preval
    currentval = str(math.sin(float(preval)))
    preval = currentval
    outputval.set(currentval)


def cos():
    global preval
    currentval = str(math.cos(float(preval)))
    preval = currentval
    outputval.set(currentval)


def tan():
    global preval
    currentval = str(math.tan(float(preval)))
    preval = currentval
    outputval.set(currentval)


def sinh():
    global preval
    currentval = str(math.sinh(float(preval)))
    preval = currentval
    outputval.set(currentval)


def cosh():
    global preval
    currentval = str(math.cosh(float(preval)))
    preval = currentval
    outputval.set(currentval)


def tanh():
    global preval
    currentval = str(math.tanh(float(preval)))
    preval = currentval
    outputval.set(currentval)


def logbasetwo():
    global preval
    if preval == '' or preval < '0':
        raise ValueError
    currentval = str(math.log2(float(preval)))
    preval = currentval
    outputval.set(currentval)


def exp():
    global preval
    currentval = str(math.exp(float(preval)))
    preval = currentval
    outputval.set(currentval)


def exponent():
    global preval
    currentval = preval + str(math.e)
    preval = currentval
    outputval.set(currentval)


def mod(n):
    global preval
    currentval = preval + str(n)
    preval = currentval
    outputval.set(currentval)


def logbaseten():
    global preval
    if preval == '' or preval < '0':
        raise ValueError
    currentval = str(math.log10(float(preval)))
    preval = currentval
    outputval.set(currentval)


def degree():
    global preval
    currentval = str(math.degrees(float(preval)))
    preval = currentval
    outputval.set(currentval)


def fact():
    global preval
    val = 1
    currentval = ''
    if preval < '0':
        raise ValueError
    elif preval == '0' or preval == '1':
        currentval = '1'
    elif preval > '1':
        for i in range(2, int(preval)+1):
            val = val * i
        currentval = str(val)
#       currentval = str(math.factorial(int(preval)))
        preval = currentval
    outputval.set(currentval)


def inverfunc():
    global preval
    currentval = str(1/float(preval))
    preval = currentval
    outputval.set(currentval)


def squareroot():
    global preval
    currentval = str(math.sqrt(float(preval)))
    preval = currentval
    outputval.set(currentval)


def square():
    global preval
    currentval = str(math.pow(float(preval), 2))
    preval = currentval
    outputval.set(currentval)


def cube():
    global preval
    currentval = str(math.pow(float(preval), 3))
    preval = currentval
    outputval.set(currentval)


def powerfunc():
    global preval
    currentval = str(math.pow(2, float(preval)))
    preval = currentval
    outputval.set(currentval)


if __name__ == '__main__':

    calc = Tk()
    calc.configure(background='light green')
    calc.title('Python Calculator')
    calc.geometry('400x400')

    scicalc = Frame(calc)
    scicalc.grid()
    outputval = StringVar()
    display = Entry(calc, font=('Lucida Console', 18, 'bold'), textvariable=outputval)
    display.grid(row=1, columnspan=4, ipadx=48, ipady=30, sticky=N+E+W+S)
    Button(calc, text="AC", height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10,  'bold'), command=lambda: clear_all()).grid(row=2, column=0, sticky=N+E+W+S)
    Button(calc, text='C', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'),  command=lambda: clear()).grid(row=2, column=1, sticky=N+E+W+S)
    Button(calc, text='%', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: percent()).grid(row=2, column=2, sticky=N+E+W+S)
    Button(calc, text='/', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: div('/')).grid(row=2, column=3, sticky=N+E+W+S)
    Button(calc, text='7', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(7)).grid(row=3, column=0, sticky=N+E+W+S)
    Button(calc, text='8', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(8)).grid(row=3, column=1, sticky=N+E+W+S)
    Button(calc, text='9', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(9)).grid(row=3, column=2, sticky=N+E+W+S)
    Button(calc, text='*', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: mul('*')).grid(row=3, column=3, sticky=N+E+W+S)
    Button(calc, text='4', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(4)).grid(row=4, column=0, sticky=N+E+W+S)
    Button(calc, text='5', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(5)).grid(row=4, column=1, sticky=N+E+W+S)
    Button(calc, text='6', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(6)).grid(row=4, column=2, sticky=N+E+W+S)
    Button(calc, text='-', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: sub('-')).grid(row=4, column=3, sticky=N+E+W+S)
    Button(calc, text='1', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(1)).grid(row=5, column=0, sticky=N+E+W+S)
    Button(calc, text='2', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(2)).grid(row=5, column=1, sticky=N+E+W+S)
    Button(calc, text='3', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(3)).grid(row=5, column=2, sticky=N+E+W+S)
    Button(calc, text='+', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: add('+')).grid(row=5, column=3, sticky=N+E+W+S)
    Button(calc, text='ln', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda:  ln()).grid(row=6, column=0, sticky=N+E+W+S)
    Button(calc, text='0', height=3, width=2, font=('Georgia', 10, 'bold'),
           command=lambda: get_variables(0)).grid(row=6, column=1, sticky=N+E+W+S)
    Button(calc, text='.', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: dec('.')).grid(row=6, column=2, sticky=N+E+W+S)
    Button(calc, text='=', height=3, width=2, bg='gray', fg='black', font=('Georgia', 10, 'bold'),
           command=lambda:  equal()).grid(row=6, column=3, sticky=N+E+W+S)
    Label(calc, text="Scientific Calculator", font=('Georgia', 20, 'bold'), bg='gray', fg='black',
          justify=CENTER).grid(row=1, column=4, columnspan=4, ipadx=57,  ipady=32,  sticky=N+E+W+S)
    Button(calc, text='pi', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: pi('1')).grid(row=2, column=4, sticky=N+E+W+S)
    Button(calc, text='sin', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: sin()).grid(row=2, column=5, sticky=N+E+W+S)
    Button(calc, text='cos', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: cos()).grid(row=2, column=6, sticky=N+E+W+S)
    Button(calc, text='tan', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: tan()).grid(row=2, column=7, sticky=N+E+W+S)
    Button(calc, text='2pi', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: pi('2')).grid(row=3, column=4, sticky=N+E+W+S)
    Button(calc, text='sinh', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: sinh()).grid(row=3, column=5, sticky=N+E+W+S)
    Button(calc, text='cosh', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: cosh()).grid(row=3, column=6, sticky=N+E+W+S)
    Button(calc, text='tanh', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: tanh()).grid(row=3, column=7, sticky=N+E+W+S)
    Button(calc, text='log2', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: logbasetwo()).grid(row=4, column=4, sticky=N+E+W+S)
    Button(calc, text='exp', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: exp()).grid(row=4, column=5, sticky=N+E+W+S)
    Button(calc, text='e', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: exponent()).grid(row=4, column=6, sticky=N+E+W+S)
    Button(calc, text='Mod', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: mod('%')).grid(row=4, column=7, sticky=N+E+W+S)
    Button(calc, text='log10', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: logbaseten()).grid(row=5, column=4, sticky=N+E+W+S)
    Button(calc, text='degree', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: degree()).grid(row=5, column=5, sticky=N+E+W+S)
    Button(calc, text='x!', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: fact()).grid(row=5, column=6, sticky=N+E+W+S)
    Button(calc, text='1/x', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: inverfunc()).grid(row=5, column=7, sticky=N+E+W+S)
    Button(calc, text='sqrt', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: squareroot()).grid(row=6, column=4, sticky=N+E+W+S)
    Button(calc, text='sq', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: square()).grid(row=6, column=5, sticky=N+E+W+S)
    Button(calc, text='cube', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: cube()).grid(row=6, column=6, sticky=N+E+W+S)
    Button(calc, text='2 pow x', height=3, width=2, bg='gray', fg='black',
           font=('Georgia', 10, 'bold'), command=lambda: powerfunc()).grid(row=6, column=7, sticky=N+E+W+S)

    def standard():
        calc.resizable(width=False, height=False)
        calc.geometry('400x400+0+0')

    def scientefic():
        calc.resizable(width=False, height=False)
        calc.geometry('800x400+0+0')


    menubar = Menu(scicalc)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Standard Calculator', command=lambda: standard())
    filemenu.add_separator()
    filemenu.add_command(label='Scientific Calculator', command=lambda: scientefic())

    calc.config(menu=menubar)

    calc.mainloop()
