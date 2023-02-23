


class 文件处理输出接口(object):
    def __init__(self):
        self.接收类 = 0

    def 初始化(self, 输入端):
        self.接收类 = 输入端

    def 输出文本(self, 文本):
        self.接收类.更新文本(文本)

    def 处理完成(self):
        self.接收类.文件处理完成()
