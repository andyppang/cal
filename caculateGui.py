"""
简易计算器程序
|   显示屏Label        |
1   2   3   +       CE
4   5   6   -
7   8   9   *
0   .   =   /
"""


from tkinter import *

vtext = ''
# 捕获动作，获取点击按钮的'text'属性，并在显示屏显示
def renew(event):
    global vtext
    vtext += event.widget['text']
    label['text'] = vtext


root = Tk()                              # 创建窗口
root.title('简易计算器')
root.geometry('250x300+600+300')
label = Label(root, text='0', width=20, bg='yellow')               # 创建显示屏，默认显示0
label.grid(row=0, column=0, columnspan=4, sticky=W)
b1 = Button(root, text='1', width=5)
b1.grid(row=1, column=0)
b1.bind('<Button-1>', renew)

b2 = Button(root, text='2', width=5, bg='yellow')
b2.grid(row=1, column=1)
b3 = Button(root, text='3', width=5)
b3.grid(row=1, column=2)
badd = Button(root, text='+', width=5)
badd.grid(row=1, column=3)
b4 = Button(root, text='4', width=5, bg='yellow')
b4.grid(row=2, column=0)
b5 = Button(root, text='5', width=5)
b5.grid(row=2, column=1)
b6 = Button(root, text='6', width=5, bg='yellow')
b6.grid(row=2, column=2)
bminus = Button(root, text='-', width=5)
bminus.grid(row=2, column=3)
b7 = Button(root, text='7', width=5)
b7.grid(row=3, column=0)
b8 = Button(root, text='8', width=5, bg='yellow')
b8.grid(row=3, column=1)
b9 = Button(root, text='9', width=5)
b9.grid(row=3, column=2)
btimes = Button(root, text='*', width=5)
btimes.grid(row=3, column=3)
b0 = Button(root, text='0', width=5)
b0.grid(row=4, column=0)
bdot = Button(root, text='.', width=5)
bdot.grid(row=4, column=1)
bequal = Button(root, text='=', width=5)
bequal.grid(row=4, column=2)
bdiv = Button(root, text='/', width=5)
bdiv.grid(row=4, column=3)


root.mainloop()


