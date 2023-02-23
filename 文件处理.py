from ctypes import WinError
import os
import pypinyin
import shutil
import 文件接口


# 初始设置
# 输入的初始路径 = 'N:\\OtherFile\\演示\\01\\test\\界面 - 副本'


class 文件(object):

    def __init__(self):
        self.输出接口 = 文件接口.文件处理输出接口()

    def 创建复制文件夹(self, 文件夹路径, 输入复制文件夹路径):
        拼音文件名 = self.文件名中文转拼音(self.从目录分离出文件名(文件夹路径))

        # 是否首次调用
        if 输入复制文件夹路径 is None:
            复制文件夹路径 = os.path.join(os.path.dirname(文件夹路径), 拼音文件名)  # 原目录+改名后文件夹名称
        else:
            复制文件夹路径 = os.path.join(输入复制文件夹路径, 拼音文件名)  # 原目录+改名后文件夹名称

        # 复制文件夹
        try:
            os.makedirs(复制文件夹路径)  # 创建复制文件夹
            self.输出文字信息('创建复制文件夹:' + 复制文件夹路径)
        except:
            self.输出文字信息('已跳过复制文件夹')

        return 复制文件夹路径

    def 从目录分离出文件名(self, 输入文件夹路径):
        输出文件名 = os.path.basename(输入文件夹路径)
        return 输出文件名

    def 文件名中文转拼音(self, 文件名):
        拼音文件名 = ''.join(pypinyin.lazy_pinyin(文件名))  # 文件名中文转拼音
        self.输出文字信息('正在处理\'' + 文件名 + '\'为: ' + 拼音文件名)
        return 拼音文件名

    def 复制文件(self, 文件名, 输入文件夹路径, 复制文件夹路径):
        拼音文件名 = self.文件名中文转拼音(文件名)
        复制文件到此路径 = os.path.join(复制文件夹路径, 拼音文件名)  # 复制到复制文件夹路径

        # 复制文件
        try:
            shutil.copy(输入文件夹路径, 复制文件到此路径)
        except:
            self.输出文字信息('已跳过复制文件')

        self.输出文字信息('复制文件\'' + 文件名 + '\'到' + 复制文件到此路径)

    def 判断是否为文件夹(self, 文件名, 输入文件夹路径, 复制文件夹路径):
        文件夹路径 = os.path.join(输入文件夹路径, 文件名)
        if os.path.isdir(文件夹路径):  # 如果原文件路径是一个文件夹,那么进入此文件夹处理文件
            self.输出文字信息('进入\'' + 文件夹路径 + '\'文件夹')
            self.重命名文件(文件夹路径, 复制文件夹路径)
        else:
            self.复制文件(文件名, 文件夹路径, 复制文件夹路径)

    def 重命名文件(self, 文件夹路径, 复制文件夹路径):

        if 复制文件夹路径 is None:  # 首次调用,不是递归
            复制文件夹路径 = self.创建复制文件夹(文件夹路径, None)
        else:
            复制文件夹路径 = self.创建复制文件夹(文件夹路径, 复制文件夹路径)
        for 文件名 in os.listdir(文件夹路径):  # 遍历路径下文件列表中所有文件
            self.判断是否为文件夹(文件名, 文件夹路径, 复制文件夹路径)
        self.输出文字信息('退出\'' + 文件夹路径 + '\'文件夹,处理完毕')

    def 输出文字信息(self, 文本):
        self.输出接口.输出文本(文本)
        print(文本)

    def 开始运行(self, 输入的初始路径):
        # 文件夹路径
        print(f'文件处理开始运行,路径{输入的初始路径}')
        初始路径 = 输入的初始路径

        # 判断是否文件夹
        if os.path.isdir(初始路径):
            self.重命名文件(初始路径, None)
        else:
            self.输出文字信息('不是文件夹')
            return
        self.输出接口.处理完成()
