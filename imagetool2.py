from PIL import Image as img
from tkinter import *
from tkinter.filedialog import *

# 创建空列表存放图片路径
path = []


# 打开路径
def open_path():
    global path
    path = askopenfilenames()  # 文件路径列表
    lbox = app.children['listbox']  # 获取窗口子对象
    if path:
        for filepath in path:
            name = filepath.split('/')[-1]  # 获取文件名
            lbox.insert(END, name)


# 压缩图片
def compress():
    output = 'C:/Users/pl/Desktop/'     # 存放压缩文件的路径
    for filepath in path:
        name = filepath.split('/')[-1]  # 获取文件名
        image = img.open(filepath)      # 读取图片
        image.save(output+'压缩'+name, quality=50)    # 保存图片并改名，改质量


# 交互界面窗口
def gui_app():
    app = Tk()
    app.geometry('300x400')
    Label(app, text='压缩图片小程序', font=('Arial', 20, 'bold')).pack()
    Listbox(app, name='listbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='打开路径', command=open_path).pack()
    Button(app, text='开始压缩', command=compress).pack()
    return app


app = gui_app()
app.mainloop()