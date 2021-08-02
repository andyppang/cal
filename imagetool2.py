"""
图片处理小程序
主要功能：选取多张图片进行压缩、调整大小
知识点：首先给窗口的每个部件给予name属性，则可以通过 窗口.children['name'] 获取到该部件
从而可对该部件进行外部调用操作
"""
from PIL import Image as img
from tkinter import *
from tkinter.filedialog import *

# 创建空列表存放图片路径，全局变量供各个功能函数调用
path = []
logo_path = []

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
    try:
        app.children['message']['text'] = '压缩完成'
    except:
        app.children['message']['text'] = '出错啦'


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
    try:
        app.children['message']['text'] = '大小调整完成'
    except:
        app.children['message']['text'] = '出错啦'


def select_logo():
    global logo_path
    logo_path = askopenfilename()   # 水印图片地址


def copy():
    output = 'C:/Users/pl/Desktop/'
    x = app.children['x'].get()  # 获取app窗口的名称为'x'的部件，即输入框的值
    y = app.children['y'].get()  # 获取app窗口的名称为'y‘的部件，即输入框的值
    for filepath in path:
        name = filepath.split('/')[-1]  # 获取文件名
        image = img.open(filepath)  # 读取图片
        logo = img.open(logo_path)  # 读取logo图片
        logo.convert('RGBA')
        logo.thumbnail((200, 200))  # 将logo改成合适的大小
        image_copy = image.copy()   # 复制图象
        position = (int(x), int(y))           # 粘贴的位置
        image_copy.paste(logo, position)
        image_copy.save(output + '水印' + name)   # 保存图片并改名
    try:
        app.children['message']['text'] = '已添加水印'
    except:
        app.children['message']['text'] = '出错啦'


# 交互界面窗口
def gui_app():
    app = Tk()
    app.geometry('320x400')
    Label(app, text='图片处理小程序', font=('Arial', 20, 'bold')).pack()
    Listbox(app, name='listbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app, text='打开路径', command=open_path).pack(side=TOP)
    e1 = StringVar()
    e1.set('宽')
    e2 = StringVar()
    e2.set('高')
    Label(app, name='message', text='这里用来显示反馈信息').pack(side=BOTTOM, fill=X)
    Entry(app, name='x', textvariable=e1, width=12).pack(side=BOTTOM, fill=X)
    Entry(app, name='y', textvariable=e2, width=12).pack(side=BOTTOM, fill=X)
    Button(app, text='压缩图片', command=compress).pack(side=LEFT, fill=X, padx=1)
    Button(app, text='调整大小', command=resize).pack(side=LEFT, fill=X, padx=1)
    Button(app, text='添加水印', command=copy).pack(side=LEFT, fill=X, padx=1)
    Button(app, text='水印图片', command=select_logo).pack(side=LEFT, fill=X, padx=1)
    return app


app = gui_app()
app.mainloop()