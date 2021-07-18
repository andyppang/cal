"""
简易计算器程序
|   显示屏Label        |
1   2   3   +       CE
4   5   6   -       X
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
root.geometry('300x300+600+300')
label = Label(root, text='0', width=25, bg='yellow')               # 创建显示屏，默认显示0
label.grid(row=0, column=0, columnspan=4, sticky=W)
# 数字按钮和加减乘除按钮
b1 = Button(root, text='1', width=5)
b1.grid(row=1, column=0)
b1.bind('<Button-1>', renew)
b2 = Button(root, text='2', width=5, bg='yellow')
b2.grid(row=1, column=1)
b2.bind('<1>', renew)
b3 = Button(root, text='3', width=5)
b3.grid(row=1, column=2)
b3.bind('<1>', renew)
badd = Button(root, text='+', width=5)
badd.grid(row=1, column=3)
badd.bind('<1>', renew)
b4 = Button(root, text='4', width=5, bg='yellow')
b4.grid(row=2, column=0)
b4.bind('<1>', renew)
b5 = Button(root, text='5', width=5)
b5.grid(row=2, column=1)
b5.bind('<1>', renew)
b6 = Button(root, text='6', width=5, bg='yellow')
b6.grid(row=2, column=2)
b6.bind('<1>', renew)
bminus = Button(root, text='-', width=5)
bminus.grid(row=2, column=3)
bminus.bind('<1>', renew)
b7 = Button(root, text='7', width=5)
b7.grid(row=3, column=0)
b7.bind('<1>', renew)
b8 = Button(root, text='8', width=5, bg='yellow')
b8.grid(row=3, column=1)
b8.bind('<1>', renew)
b9 = Button(root, text='9', width=5)
b9.grid(row=3, column=2)
b9.bind('<1>', renew)
btimes = Button(root, text='*', width=5)
btimes.grid(row=3, column=3)
btimes.bind('<1>', renew)
b0 = Button(root, text='0', width=5)
b0.grid(row=4, column=0)
b0.bind('<1>', renew)
bdot = Button(root, text='.', width=5)
bdot.grid(row=4, column=1)
bdot.bind('<1>', renew)
# 等号键进行计算，单击绑定caculate()函数
bequal = Button(root, text='=', width=5)
bequal.grid(row=4, column=2)
bequal.bind('<1>', caculate)                # ‘=‘号单击绑定caculate函数
bdiv = Button(root, text='/', width=5)
bdiv.grid(row=4, column=3)
bdiv.bind('<1>', renew)
# 清零键，单击绑定reset()函数
breset = Button(root, text='CE', width=5)
breset.grid(row=1, column=4)
breset.bind('<1>', reset)
# 删除键，单击绑定del()函数
bdelete = Button(root, text='Ⅹ', width=5)
bdelete.grid(row=2, column=4)
bdelete.bind('<1>', delete)

root.mainloop()


