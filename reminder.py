#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from tkinter import *

delaymin = 0.5


def show_reminder():
    root = Tk()
    root.withdraw()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight() - 100
    root.resizable(False, False)
    root.title("reminder")
    frame = Frame(root, relief=RIDGE, borderwidth=3)
    frame.pack(fill=BOTH, expand=1)
    label = Label(frame, text="啊欧,已经工作1小时了，站起来休息一下吧!", font="Monotype\ Corsiva -20 bold")
    label.pack(fill=BOTH, expand=1)
    button = Button(frame, text="OK", font="Cooper -25 bold", fg="red", command=root.destroy)
    button.pack(side=BOTTOM)
    root.update_idletasks()
    root.deiconify()
    root.withdraw()
    # root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10,
    #                                (screenwidth - root.winfo_width()) / 2,
    #                                (screenheight - root.winfo_height()) / 2))  # 窗口所在位置以及大小，前两个字符串代表窗口宽高，后两个字符串代表左上角坐标
    root.geometry('800x200')
    root.deiconify()
    root.lift(aboveThis=None)
    root.mainloop()


while True:
    time.sleep(delaymin * 60)
    show_reminder()
