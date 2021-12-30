# 一系列按钮操作函数
from tkinter.messagebox import *
import tkinter
from configobj import ConfigObj, ParseError
import os
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText
import sys

# 调整雪花个数按钮
def snow_num():
    window = tkinter.Tk()
    window.resizable(False, False)
    window.geometry('300x200')

    label = tkinter.Label(window, text='请输入个数', bg='silver', fg='red')
    label.place(x=10, y=50)
    entry = tkinter.Entry(window)
    entry.place(x=100, y=50)

    def got():
        a = entry.get()
        try:
            if int(a):
                if 250 >= int(a) >= 50:
                    config = ConfigObj('initialize.ini', encoding='utf-8')
                    config['num'] = int(a)
                    config.write()
                    showinfo(message='修改完毕！')
                else:
                    showerror(message='雪花限制数目不能低于50，也不能高于250')
        except ValueError:
            e = ValueError('您输入的不是整数')
            showerror(message=e)

    def deleted():
        entry.delete(0, 'end')

    button = tkinter.Button(window, text='确定', bg='silver', fg='red', font=('黑体', 18), command=got)
    button.place(x=10, y=100)
    button1 = tkinter.Button(window, text='清除', bg='silver', fg='red', font=('黑体', 18), command=deleted)
    button1.place(x=200, y=100)
    window.mainloop()

# 导入图片
def import_image():
    window = tkinter.Tk()
    window.resizable(False, False)
    window.geometry('800x200')

    label = tkinter.Label(window, text='图片路径', bg='silver', fg='red')
    # E:\Pycharm专业版Projects\文档操作助手\Tkinter_for_Opening\bg.jpg
    label.place(x=10, y=50)
    entry = tkinter.Entry(window, width=70)
    entry.place(x=100, y=50)

    def got():
        e = entry.get()
        if os.path.exists(e):
            config = ConfigObj('initialize.ini', encoding='utf-8')
            # 当然了，这里可以灵活的调整为多种图片的重影效果
            config['back_image'] = e
            config['back_image2'] = e
            config.write()
            showinfo(message='修改完毕！')
        else:
            showerror(message=FileExistsError('找不到此文件！'))
    def deleted():
        entry.delete(0, 'end')

    button = tkinter.Button(window, text='确定', bg='silver', fg='red', font=('黑体', 18), command=got)
    button.place(x=10, y=100)
    button1 = tkinter.Button(window, text='清除', bg='silver', fg='red', font=('黑体', 18), command=deleted)
    button1.place(x=650, y=100)
    window.mainloop()

# 图片自适应
def fit():
    window = tkinter.Tk()
    window.resizable(False, False)
    window.geometry('800x200')

    label = tkinter.Label(window, text='图片路径', bg='silver', fg='red')
    # E:\Pycharm专业版Projects\文档操作助手\Tkinter_for_Opening\bg.jpg
    label.place(x=10, y=50)
    entry = tkinter.Entry(window, width=70)
    entry.place(x=100, y=50)

    def got():
        e = entry.get()
        if os.path.exists(e):
            config = ConfigObj('initialize.ini', encoding='utf-8')
            # 当然了，这里可以灵活的调整为多种图片的重影效果
            config['back_image'] = e
            config['back_image2'] = e
            image = Image.open(e)
            bg_image = ImageTk.PhotoImage(image)
            width = bg_image.width()
            height = bg_image.height()
            # 获得比例
            k = width/height
            if width > 600 and height > 400:
                config['width'] = 600
                config['height'] = 400
                config.write()
                showinfo(message='修改完毕！')
            elif width < 600 and height >= 400:
                config['width'] = width
                config['height'] = int(float(width * k))
                config.write()
                showinfo(message='修改完毕！')
            elif width >= 600 and height <= 400:
                config['width'] = int(float(height * k))
                config['height'] = height
                config.write()
                showinfo(message='修改完毕！')
        else:
            showerror(message=FileExistsError('找不到此文件！'))
    def deleted():
        entry.delete(0, 'end')

    button = tkinter.Button(window, text='确定', bg='silver', fg='red', font=('黑体', 18), command=got)
    button.place(x=10, y=100)
    button1 = tkinter.Button(window, text='清除', bg='silver', fg='red', font=('黑体', 18), command=deleted)
    button1.place(x=650, y=100)
    window.mainloop()

# 导入音乐
def music():
    window = tkinter.Tk()
    window.resizable(False, False)
    window.geometry('800x200')

    label = tkinter.Label(window, text='音乐路径', bg='silver', fg='red')
    # E:\Pycharm专业版Projects\文档操作助手\Tkinter_for_Opening\bg.jpg
    label.place(x=10, y=50)
    entry = tkinter.Entry(window, width=70)
    entry.place(x=100, y=50)

    def got():
        e = entry.get()
        if os.path.exists(e):
            config = ConfigObj('initialize.ini', encoding='utf-8')
            # 当然了，这里可以灵活的调整为多种图片的重影效果
            config['back_music'] = e
            config.write()
            showinfo(message='修改完毕！')
        else:
            showerror(message=FileExistsError('找不到此文件！'))
    def deleted():
        entry.delete(0, 'end')

    button = tkinter.Button(window, text='确定', bg='silver', fg='red', font=('黑体', 18), command=got)
    button.place(x=10, y=100)
    button1 = tkinter.Button(window, text='清除', bg='silver', fg='red', font=('黑体', 18), command=deleted)
    button1.place(x=650, y=100)
    window.mainloop()

# 修改图片透明度
def alpha():
    window = tkinter.Tk()
    window.resizable(False, False)
    window.geometry('200x200')

    label = tkinter.Label(window, text='设置透明度', bg='silver', fg='red')
    # E:\Pycharm专业版Projects\文档操作助手\Tkinter_for_Opening\bg.jpg
    label.place(x=10, y=50)
    entry = tkinter.Entry(window, width=10)
    entry.place(x=100, y=50)

    def got():
        e = entry.get()
        try:
            if int(e):
                if 0 <= int(e) <= 255:
                    config = ConfigObj('initialize.ini', encoding='utf-8')
                    config['alpha'] = e
                    config.write()
                    showinfo(message='修改完毕！')
                else:
                    showerror(message='请输入0~255以内的整数')
        except ValueError:
            showerror(message=ValueError('请输入0~255以内的整数'))
    def deleted():
        entry.delete(0, 'end')

    button = tkinter.Button(window, text='确定', bg='silver', fg='red', font=('黑体', 18), command=got)
    button.place(x=10, y=100)
    button1 = tkinter.Button(window, text='清除', bg='silver', fg='red', font=('黑体', 18), command=deleted)
    button1.place(x=100, y=100)
    window.mainloop()

# 重置注册机
def reg():
    window = tkinter.Tk()
    window.resizable(False, False)
    window.geometry('200x200')
    def regs():
        try:
            config = ConfigObj('initialize.ini', encoding='utf-8')
            config['width'] = 600
            config['height'] = 400
            config['num'] = 200
            config['back_image'] = 'bg.jpg'
            config['back_image2'] = 'bg2.png'
            config['back_music'] = 'jn.mp3'
            config['alpha'] = 120
            config['snow_color'] = [192, 192, 192]
            showinfo(message='修改完毕!')
            config.write()
        except ParseError:
            config = open('initialize.ini', 'w', encoding='utf-8')
            config.write('width = 600\nheight = 400\nnum = 200\nback_image = bg.jpg\n'
                         'back_image2 = bg2.png\nback_music = jn.mp3\n'
                         'alpha = 120\n'
                         'snow_color = 192, 192, 192')
            config.close()
            showinfo(message='修改完毕!')
    button = tkinter.Button(window, text='重置', bg='yellow', fg='indigo', font=('黑体', 18), command=regs)
    button.place(x=10, y=70)
    button1 = tkinter.Button(window, text='算了', bg='silver', fg='blue', font=('黑体', 18), command=sys.exit)
    button1.place(x=100, y=70)
    window.mainloop()

# 关于
def about():
    window = tkinter.Tk()
    window.resizable(False, False)
    window.geometry('400x400')
    a = open('author.txt', 'r', encoding='utf-8')
    f = a.read()
    a.close()
    view_text = ScrolledText(window, font=('宋体', 12), fg='black', bg='silver')
    view_text.insert('0.0', f)
    view_text.place(x=10, y=5, height=380, width=380)
    window.mainloop()

if __name__ == '__main__':
    reg()