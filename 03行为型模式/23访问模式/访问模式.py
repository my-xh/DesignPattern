from abc import ABCMeta, abstractmethod


class DataNode(metaclass=ABCMeta):
    """数据结构类"""

    def accept(self, visitor):
        """接受访问者的访问"""
        visitor.visit(self)


class Visitor(metaclass=ABCMeta):
    """访问者"""

    @abstractmethod
    def visit(self, data):
        """对数据对象的访问操作"""
        pass


class ObjectStructure:
    """数据结构的管理类，也是数据对象的一个容器，可以遍历容器内的所有元素"""

    def __init__(self):
        self.__datas = []

    def add(self, data_element):
        self.__datas.append(data_element)

    def action(self, visitor):
        for data in self.__datas:
            data.accept(visitor)


class DesignPatternBook(DataNode):
    """《从生活的角度解读设计模式》一书"""

    @property
    def name(self):
        return '《从生活的角度解读设计模式》'


class Engineer(Visitor):
    """工程师"""

    def visit(self, book):
        print(f'技术人读{book.name} 一书后的感受: 能抓住模式的核心思想，深入浅出，很有见地！')


class ProductManager(Visitor):
    """产品经理"""

    def visit(self, book):
        print(f'产品经理读{book.name} 一书后的感受: 配图非常有趣，文章很有层次感！')


class OtherFriend(Visitor):
    """IT圈外的朋友"""

    def visit(self, book):
        print(f'IT圈外的朋友读{book.name} 一书后的感受: 技术的内容一脸懵，但故事很精彩，想看小说或故事集！')


if __name__ == '__main__':
    book = DesignPatternBook()
    obj_mgr = ObjectStructure()
    obj_mgr.add(book)
    obj_mgr.action(Engineer())
    obj_mgr.action(ProductManager())
    obj_mgr.action(OtherFriend())
