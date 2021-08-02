# Author:FuJLiny
# CSDN blog homepage:https://blog.csdn.net/FujLiny
# ------version 1-1,Update time:2021/5/12------

import tkinter as tk
import pyperclip as pc


class Button:
    def __init__(self, win, txt):
        win.children['!entry'].delete(0, 'end')  # win.children 以字典方式存储窗口中的所有组件
        self.txt = txt
        self.button = tk.Button(win, text=txt, font=('SimHei',14), width=48, relief='groove', command=self.copy_text)
        self.buttonDel = tk.Button(win,text='Del', width=7, relief='groove', command=self.destroy)

        x = win.grid_size()[1] + 1  # grid_size()以元组形式返回窗口中网格的行数和列数：(列,行)
        self.button.grid(row=x, column=0)
        self.buttonDel.grid(row=x, column=1)

    def copy_text(self):
        pc.copy(self.txt)

    def destroy(self):
        self.button.destroy()
        self.buttonDel.destroy()


root = tk.Tk()
root.title('easy-copy')
root.attributes('-topmost', True)  # 窗口显示在屏幕最前面，不会被电脑其他窗口遮挡
root.resizable(width=False, height=False)  # 不允许调节窗口尺寸
root.bind('<Return>', lambda x : Button(root, entry.get()))  # 绑定回车键

entry = tk.Entry(root,width=40, font=('SimHei', 18))
entry.grid(row=0, column=0)
tk.Button(root, text='Append', width=7, relief='groove',
          command=lambda:Button(root, entry.get())).grid(row=0, column=1)
root.mainloop()

