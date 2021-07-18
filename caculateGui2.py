"""
简易计算器程序
|   显示屏Label        |
1   2   3   +       CE
4   5   6   -       X
7   8   9   *
0   .   =   /
大按钮大界面
"""


from tkinter import *

vtext = ''
# 捕获动作，获取点击按钮的'text'属性，并在显示屏显示
def renew(event):
    global vtext
    vtext += event.widget['text']
    label['text'] = vtext

def caculate(event):
    if '+' in vtext:
        templist = vtext.split('+')
        m = float(templist[0])
        n = float(templist[1].split('=')[0])
        result = m + n
    if '-' in vtext:
        templist = vtext.split('-')
        m = float(templist[0])
        n = float(templist[1].split('=')[0])
        result = m - n
    if '*' in vtext:
        templist = vtext.split('*')
        m = float(templist[0])
        n = float(templist[1].split('=')[0])
        result = m * n
    if '/' in vtext:
        templist = vtext.split('/')
        m = float(templist[0])
        n = float(templist[1].split('=')[0])
        result = m / n
    label['text'] = vtext + '=' + str(result)

def reset(event):
    global vtext
    vtext = ''
    label['text'] = vtext

def delete(event):
    global vtext
    vtext = vtext[:-1]                  # 字符串删除最后一个字符
    label['text'] = vtext

root = Tk()                              # 创建窗口
root.title('简易计算器')
root.geometry('470x375+600+300')
label = Label(root, text='0', width=25, borderwidth=3, relief="sunken",
              height=2, bg='yellow', font=('Arial', 15))               # 创建显示屏，默认显示0
label.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)
# 数字按钮和加减乘除按钮
b1 = Button(root, text='1', width=5, height=2, font=('Arial', 15))
b1.grid(row=1, column=0, sticky=E+W+N+S)
b1.bind('<Button-1>', renew)
b2 = Button(root, text='2', width=5, height=2, font=('Arial', 15), bg='yellow')
b2.grid(row=1, column=1, sticky=E+W+N+S)
b2.bind('<1>', renew)
b3 = Button(root, text='3', width=5, height=2, font=('Arial', 15))
b3.grid(row=1, column=2, sticky=E+W+N+S)
b3.bind('<1>', renew)
badd = Button(root, text='+', width=5, height=2, font=('Arial', 15))
badd.grid(row=1, column=3, sticky=E+W+N+S)
badd.bind('<1>', renew)
b4 = Button(root, text='4', width=5, height=2, font=('Arial', 15), bg='yellow')
b4.grid(row=2, column=0, sticky=E+W+N+S)
b4.bind('<1>', renew)
b5 = Button(root, text='5', width=5, height=2, font=('Arial', 15))
b5.grid(row=2, column=1, sticky=E+W+N+S)
b5.bind('<1>', renew)
b6 = Button(root, text='6', width=5, height=2, font=('Arial', 15), bg='yellow')
b6.grid(row=2, column=2, sticky=E+W+N+S)
b6.bind('<1>', renew)
bminus = Button(root, text='-', width=5, height=2, font=('Arial', 15))
bminus.grid(row=2, column=3, sticky=E+W+N+S)
bminus.bind('<1>', renew)
b7 = Button(root, text='7', width=5, height=2, font=('Arial', 15))
b7.grid(row=3, column=0, sticky=E+W+N+S)
b7.bind('<1>', renew)
b8 = Button(root, text='8', width=5, height=2, font=('Arial', 15), bg='yellow')
b8.grid(row=3, column=1, sticky=E+W+N+S)
b8.bind('<1>', renew)
b9 = Button(root, text='9', width=5, height=2, font=('Arial', 15))
b9.grid(row=3, column=2, sticky=E+W+N+S)
b9.bind('<1>', renew)
btimes = Button(root, text='*', width=5, height=2, font=('Arial', 15))
btimes.grid(row=3, column=3, sticky=E+W+N+S)
btimes.bind('<1>', renew)
b0 = Button(root, text='0', width=5, height=2, font=('Arial', 15))
b0.grid(row=4, column=0, sticky=E+W+N+S)
b0.bind('<1>', renew)
bdot = Button(root, text='.', width=5, height=2, font=('Arial', 15))
bdot.grid(row=4, column=1, sticky=E+W+N+S)
bdot.bind('<1>', renew)
# 等号键进行计算，单击绑定caculate()函数
bequal = Button(root, text='=', width=5, height=2, font=('Arial', 15))
bequal.grid(row=4, column=2, sticky=E+W+N+S)
bequal.bind('<1>', caculate)                # ‘=‘号单击绑定caculate函数
bdiv = Button(root, text='/', width=5, height=2, font=('Arial', 15))
bdiv.grid(row=4, column=3, sticky=E+W+N+S)
bdiv.bind('<1>', renew)
# 清零键，单击绑定reset()函数
breset = Button(root, text='CE', width=5, height=2, font=('Arial', 15))
breset.grid(row=1, column=4, sticky=E+W+N+S)
breset.bind('<1>', reset)
# 删除键，单击绑定del()函数
bdelete = Button(root, text='Ⅹ', width=5, height=2, font=('Arial', 15))
bdelete.grid(row=2, column=4, sticky=E+W+N+S)
bdelete.bind('<1>', delete)

root.mainloop()


