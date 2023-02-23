


class 界面显示输出接口(object):
    def __init__(self):
        self.接收类 = 0

    def 初始化(self, 输入端):
        self.接收类 = 输入端

    def 输出开始运行(self, 输入的初始路径):
        self.接收类.开始运行(输入的初始路径)
