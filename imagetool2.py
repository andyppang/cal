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
            lbox.insert(END, name)  # 向listbox末尾添加图片名称


# 压缩图片
def compress():
    output = 'C:/Users/pl/Desktop/'     # 存放压缩文件的路径
    for filepath in path:
        name = filepath.split('/')[-1]  # 获取文件名
        image = img.open(filepath)      # 读取图片
        # print(image.format, image.size, image.mode)   # 图片格式，大小，像素类型
        image.save(output+'压缩'+name, quality=50)    # 保存图片并改名，改质量


# 调整图片大小
def resize():
    output = 'C:/Users/pl/Desktop/'  # 存放压缩文件的路径
    x = app.children['x'].get()     # 获取app窗口的名称为'x'的部件，即输入框的值
    y = app.children['y'].get()     # 获取app窗口的名称为'y‘的部件，即输入框的值
    for filepath in path:
        name = filepath.split('/')[-1]  # 获取文件名
        image = img.open(filepath)  # 读取图片
        # print(image.format, image.size, image.mode)   # 图片格式，大小，像素类型
        image_small = image.resize((int(x), int(y)))    # 注意resize函数的大小为元组形式
        image_small.save(output + '变小' + name)  # 保存图片并改名


# 交互界面窗口
def gui_app():
    app = Tk()
    app.geometry('300x400')
    Label(app, text='压缩图片小程序', font=('Arial', 20, 'bold')).pack()
    Listbox(app, name='listbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='打开路径', command=open_path).pack()
    Button(app, text='开始压缩', command=compress).pack()
    Button(app, text='调整大小', command=resize).pack(anchor='w', side='left', expand=True)
    e1 = StringVar()
    e2 = StringVar()
    Entry(app, name='x', textvariable=e1).pack(anchor='w', side='left', expand=True)
    Entry(app, name='y', textvariable=e2).pack(anchor='e', side='left', expand=True)
    return app


app = gui_app()
app.mainloop()