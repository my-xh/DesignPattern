import os
from abc import ABCMeta, abstractmethod
from 第三方PDF解析库 import ThirdPdf


class Page:
    """电子书一页的内容"""

    def __init__(self, page_num):
        self.__page_num = page_num

    def get_content(self):
        return f'第 {self.__page_num} 页的内容......'


class Catalogue:
    """目录结构"""

    def __init__(self, title):
        self.__title = title
        self.__chapters = []

    def add_chapter(self, chapter):
        self.__chapters.append(chapter)

    def show_info(self):
        print(f'书名: {self.__title}')
        print('目录:')
        for chapter in self.__chapters:
            print('\t' + chapter)


class IBook(metaclass=ABCMeta):
    """电子书文档的接口类"""

    @abstractmethod
    def parse_file(self, file_path):
        """解析文档"""
        pass

    @abstractmethod
    def get_catalogue(self):
        """获取目录"""
        pass

    @abstractmethod
    def get_page_count(self):
        """获取页数"""
        pass

    @abstractmethod
    def get_page(self, num):
        """获取第 num 页的内容"""
        pass


class TxtBook(IBook):
    """TXT 解析类"""

    def parse_file(self, file_path):
        print(f'{file_path} 解析成功!')
        self.__title = os.path.splitext(file_path)[0]
        self.__page_count = 500
        return True

    def get_catalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.add_chapter('第一章 标题')
        catalogue.add_chapter('第二章 标题')
        return catalogue

    def get_page_count(self):
        return self.__page_count

    def get_page(self, num):
        return Page(num)


class EpubBook(IBook):
    """Epub 解析类"""

    def parse_file(self, file_path):
        print(f'{file_path} 解析成功!')
        self.__title = os.path.splitext(file_path)[0]
        self.__page_count = 800
        return True

    def get_catalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.add_chapter('第一章 标题')
        catalogue.add_chapter('第二章 标题')
        return catalogue

    def get_page_count(self):
        return self.__page_count

    def get_page(self, num):
        return Page(num)


class PdfAdapterBook(IBook):
    """对第三方PDF解析库重新进行包装"""

    def __init__(self, third_pdf):
        self.__third_pdf = third_pdf

    def parse_file(self, file_path):
        rtn = self.__third_pdf.open(file_path)
        if rtn:
            print(f'{file_path} 解析成功!')
        return rtn

    def get_catalogue(self):
        outline = self.__third_pdf.get_outline()
        print('将 Outline 结构的目录转换成 Catalogue 结构的目录')
        catalogue = Catalogue(self.__third_pdf.get_title())
        for title in outline.get_outlines():
            catalogue.add_chapter(title)
        return catalogue

    def get_page_count(self):
        return self.__third_pdf.get_size()

    def get_page(self, num):
        page = self.__third_pdf.page(num)
        print('将 PDFPage 的面对象转换成 Page 的对象')
        return Page(page.get_page_num())


class Reader:
    """阅读器"""

    def __init__(self, name):
        self.__name = name
        self.__file_path = ''
        self.__cur_book = None
        self.__cur_page_num = -1

    def __init_book(self, file_path):
        self.__file_path = file_path
        self.__cur_book = None
        ext = os.path.splitext(file_path)[-1]
        if ext.lower() == '.txt':
            self.__cur_book = TxtBook()
        elif ext.lower() == '.epub':
            self.__cur_book = EpubBook()
        elif ext.lower() == '.pdf':
            self.__cur_book = PdfAdapterBook(ThirdPdf())

    def open_file(self, file_path):
        self.__init_book(file_path)
        if self.__cur_book is not None:
            rtn = self.__cur_book.parse_file(file_path)
            if rtn:
                self.__cur_page_num = 1
            return rtn
        return False

    def close_file(self):
        print(f'关闭 {self.__file_path}')
        return True

    def show_catalogue(self):
        catalogue = self.__cur_book.get_catalogue()
        catalogue.show_info()

    def pre_page(self):
        print('往前翻一页: ', end='')
        return self.goto_page(self.__cur_page_num - 1)

    def next_page(self):
        print('往后翻一页: ', end='')
        return self.goto_page(self.__cur_page_num + 1)

    def goto_page(self, page_num):
        if 1 <= page_num <= self.__cur_book.get_page_count():
            self.__cur_page_num = page_num

        print(f'显示第 {self.__cur_page_num} 页')
        page = self.__cur_book.get_page(self.__cur_page_num)
        page.get_content()
        return page


if __name__ == '__main__':
    reader = Reader('阅读器')
    if reader.open_file('平凡的世界.txt'):
        reader.show_catalogue()
        reader.pre_page()
        reader.next_page()
        reader.next_page()
        reader.close_file()
        print()

    if reader.open_file('追风筝的人.epub'):
        reader.show_catalogue()
        reader.next_page()
        reader.next_page()
        reader.pre_page()
        reader.close_file()
        print()

    if reader.open_file('如何从生活中领悟设计模式.pdf'):
        reader.show_catalogue()
        reader.pre_page()
        reader.next_page()
        reader.next_page()
        reader.close_file()
