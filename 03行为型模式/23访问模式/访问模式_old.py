from abc import ABCMeta, abstractmethod


class DesignPatternBook:
    """《从生活的角度解读设计模式》一书"""

    @property
    def name(self):
        return '《从生活的角度解读设计模式》'


class Reader(metaclass=ABCMeta):
    """访问者（读者）"""

    @abstractmethod
    def read(self, book):
        pass


class Engineer(Reader):
    """工程师"""

    def read(self, book):
        print(f'技术人读{book.name} 一书后的感受: 能抓住模式的核心思想，深入浅出，很有见地！')


class ProductManager(Reader):
    """产品经理"""

    def read(self, book):
        print(f'产品经理读{book.name} 一书后的感受: 配图非常有趣，文章很有层次感！')


class OtherFriend(Reader):
    """IT圈外的朋友"""

    def read(self, book):
        print(f'IT圈外的朋友读{book.name} 一书后的感受: 技术的内容一脸懵，但故事很精彩，想看小说或故事集！')


if __name__ == '__main__':
    book = DesignPatternBook()
    fans = [Engineer(), ProductManager(), OtherFriend()]
    for fan in fans:
        fan.read(book)
