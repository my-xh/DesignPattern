import os


class Outline:
    """目录类"""

    def __init__(self):
        self.__outlines = []

    def add_outline(self, outline):
        self.__outlines.append(outline)

    def get_outlines(self):
        return self.__outlines


class PDFPage:
    """PDF页"""

    def __init__(self, page_num):
        self.__page_num = page_num

    def get_page_num(self):
        return self.__page_num


class ThirdPdf:
    """第三方PDF解析库"""

    def __init__(self):
        self.__page_size = 0
        self.__title = ''

    def open(self, file_path):
        print(f'第三方库解析PDF文件: {file_path}')
        self.__title = os.path.splitext(file_path)[0]
        self.__page_size = 1000
        return True

    def get_title(self):
        return self.__title

    def get_outline(self):
        outline = Outline()
        outline.add_outline('第一章 PDF电子书标题')
        outline.add_outline('第二章 PDF电子书标题')
        return outline

    def get_size(self):
        return self.__page_size

    def page(self, index):
        return PDFPage(index)
