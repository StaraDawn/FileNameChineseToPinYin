import tkinter as tk  # 窗口
from tkinter import filedialog  # 选择文件夹
from PIL import Image, ImageTk  # 载入图片
import tkinter.messagebox  # 弹窗
import tkinter.simpledialog  # 弹出选择窗口


class 界面显示输出接口(object):
    def __init__(self):
        self.接收类 = 0

    def 初始化(self, 输入端):
        self.接收类 = 输入端

    def 输出开始运行(self, 输入的初始路径):
        self.接收类.开始运行(输入的初始路径)


class 窗口(object):

    def __init__(self):
        self.已选择文件 = 0
        self.已确认路径 = 0
        self.文件夹路径 = 0  # 保存文件夹路径
        self.显示文本 = '请选择文件夹'  # 显示的文本

    文本标签 = 0  # 显示文本的界面
    输出接口 = 界面显示输出接口()

    def 拖入文件夹(self):
        # 文件路径 = filedialog.askopenfilename()  # 调用 askopenfilename 函数选择文件
        文件路径 = filedialog.askdirectory()  # 选择文件夹
        if 文件路径 != 0:
            self.更新文本(文件路径)
            self.已选择文件 = 1  # 设置已选择文件
            self.文件夹路径 = 文件路径  # 保存文件夹路径
            print(f'文件路径:{文件路径}')

    def 更新文本(self, 文本):
        self.显示文本 = 文本
        self.文本标签.config(text=self.显示文本)

    def 确认路径(self):
        if self.已选择文件 == 1 & bool(self.文件夹路径 != 0):
            print('弹窗')
            确认弹窗 = tkinter.messagebox.askyesno("确认路径", f"请确认你的路径为{self.文件夹路径}")
            if 确认弹窗:
                self.已确认路径 = 1  # 设置已选择文件
                tkinter.messagebox.showinfo('再次确认', f"运行后不可停止,再次确认你的路径为{self.文件夹路径}")
                print('已确认路径')
                self.更新文本('已确认路径: ' + self.文件夹路径)
            else:
                self.已确认路径 = 0
                self.更新文本('没有确认路径')
        elif self.文件夹路径 == 0:
            self.更新文本('路径为空')
        else:
            self.更新文本('请先选择文件')

    def 开始运行函数(self):
        if self.已确认路径 == 1:
            self.更新文本('===开始执行===')
            self.输出接口.输出开始运行(self.文件夹路径)

        else:
            self.更新文本('请先确认路径')

    def 文件处理完成(self):
        tkinter.messagebox.showinfo('处理完成', f"{self.文件夹路径}---处理完成")
        self.__init__()

    def 显示窗口(self):
        窗口 = tk.Tk()  # 创建窗口
        窗口.title('批量文件夹内文件中文转拼音')  # 设置标题名称
        窗口.geometry("500x600")  # 设置窗口大小

        图标img = Image.open("img/图标.ico")  # 打开图标
        图标 = ImageTk.PhotoImage(图标img)  # 保存图标
        窗口.wm_iconphoto(1, 图标)  # 修改图标

        img = Image.open("img/图片.png")  # 打开图片
        图片 = ImageTk.PhotoImage(img)  # 保存图片并设置图片大小
        图片标签 = tk.Label(窗口, image=图片, width=500, height=500)  # 创建一个标签显示图片
        图片标签.pack(fill="both", expand=True)  # 将标签填充整个窗口

        self.文本标签 = tk.Label(图片标签, text=self.显示文本, width=70)
        self.文本标签.pack(side="top")

        按钮1 = tk.Button(text='1.选择文件', command=self.拖入文件夹, bg="White", height=5, width=23)  # 创建按钮
        按钮1.pack(side="left")
        按钮2 = tk.Button(窗口, text='2.确认路径', command=self.确认路径, bg="White", height=5, width=22)  # 创建按钮
        按钮2.pack(side="left")
        按钮 = tk.Button(窗口, text='3.开始运行', command=self.开始运行函数, bg="White", height=5, width=23)  # 创建按钮
        按钮.pack(side="right")

        窗口.mainloop()  # 进入循环
