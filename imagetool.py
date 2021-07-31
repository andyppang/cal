from PIL import Image as img
from tkinter import *
from tkinter.filedialog import *

# 创建字典存放图片路径
info = {'path': []}

# 打开路径
def open_path():
    filenames = askopenfilenames()  # 文件路径列表
    lbox = app.children['listbox']  # 获取窗口子对象
    info['path'] = filenames
    if info['path']:
        for name in filenames:
            lbox.insert(END, name.split('/')[-1])


def compress():
    output = 'C:/Users/pl/Desktop/'
    for filepath in info['path']:
        name = filepath.split('/')[-1]
        image = img.open(filepath)
        image.save(output+'压缩'+name, quality=50)


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