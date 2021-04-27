import os
from 组合模式 import Component, Composite


class FileDetail(Component):
    """文件详情"""

    def __init__(self, name):
        super().__init__(name)
        self.__size = 0

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def feature(self, indent):
        """文件大小, 单位: KB, 精确度: 2位小数"""
        file_size = round(self.size / 1024, 2)
        print(f'{indent}文件名称: {self.name}, 文件大小: {file_size}KB')


class FolderDetail(Composite):
    """文件夹详情"""

    def __init__(self, name):
        super().__init__(name)
        self.__count = 0

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, cnt):
        self.__count = cnt

    def feature(self, indent=''):
        print(f'{indent}文件夹名: {self.name}, 文件数量: {self.count}。包含的文件:')
        super().feature(indent)


def scan_dir(root_path, folder_detail):
    """扫描某一文件夹下的所有目录"""
    if not os.path.isdir(root_path):
        raise ValueError(f'root_path不是有效的路径: {root_path}')
    if folder_detail is None:
        raise ValueError(f'folder_detail 不能为空!')

    files = os.listdir(root_path)
    for file in files:
        file_path = os.path.join(root_path, file)
        if os.path.isdir(file_path):
            folder = FolderDetail(file)
            scan_dir(file_path, folder)
            folder_detail.add_component(folder)
        else:
            file_detail = FileDetail(file)
            file_detail.size = os.path.getsize(file_path)
            folder_detail.add_component(file_detail)
            folder_detail.count += 1


if __name__ == '__main__':
    folder_detail = FolderDetail('设计模式')
    scan_dir(r'D:\Python学习\代码\设计模式', folder_detail)
    folder_detail.feature()
