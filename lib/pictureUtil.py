import os
from conf.path import PICTUREPATH

'''
    图片处理工具类：
'''
class PictureUtil(object):

    def __init__(self):
        '''
            初始化时,获取图片目录下的所以文件
        '''
        self.fileList = os.listdir(PICTUREPATH)

    # 获取所有以jpg结尾的文件
    def errorPicture(self):
        picture = []
        for item in self.fileList:
            if item.endswith('.jpg'):
                picture.append((item,))
        return picture

    # 清除图片目录下的所有文件
    def clear_picture(self):
        list(map(os.remove, map(lambda file: PICTUREPATH + file, self.fileList)))


