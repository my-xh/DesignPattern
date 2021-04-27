from abc import ABCMeta, abstractmethod
from enum import Enum


class PenType(Enum):
    """画笔类型"""
    PenTypeLine = 0
    PenTypeRect = 1
    PenTypeEllipse = 2


class Pen(metaclass=ABCMeta):
    """画笔"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def get_type(self):
        pass


class LinePen(Pen):
    """直线画笔"""

    def get_type(self):
        return PenType.PenTypeLine


class RectPen(Pen):
    """矩形画笔"""

    def get_type(self):
        return PenType.PenTypeRect


class EllipsePen(Pen):
    """椭圆画笔"""

    def get_type(self):
        return PenType.PenTypeEllipse


class PenFactory:
    """画笔工厂类"""

    def __init__(self):
        """{key: PenType, value: Pen}"""
        self.__pens = {}

    def create_pen(self, pen_type):
        """创建画笔"""
        if self.__pens.get(pen_type) is None:
            if pen_type == PenType.PenTypeLine:
                pen = LinePen('直线画笔')
            elif pen_type == PenType.PenTypeRect:
                pen = RectPen('矩形画笔')
            elif pen_type == PenType.PenTypeEllipse:
                pen = EllipsePen('椭圆画笔')
            else:
                pen = Pen('')
            self.__pens[pen_type] = pen

        return self.__pens[pen_type]


if __name__ == '__main__':
    factory = PenFactory()

    line_pen = factory.create_pen(PenType.PenTypeLine)
    print(f'创建了 {line_pen.name}, 对象id: {id(line_pen)}, 类型: {line_pen.get_type()}')

    rect_pen_1 = factory.create_pen(PenType.PenTypeRect)
    print(f'创建了 {rect_pen_1.name}, 对象id: {id(rect_pen_1)}, 类型: {rect_pen_1.get_type()}')

    rect_pen_2 = factory.create_pen(PenType.PenTypeRect)
    print(f'创建了 {rect_pen_2.name}, 对象id: {id(rect_pen_2)}, 类型: {rect_pen_2.get_type()}')

    ellipse_pen = factory.create_pen(PenType.PenTypeEllipse)
    print(f'创建了 {ellipse_pen.name}, 对象id: {id(ellipse_pen)}, 类型: {ellipse_pen.get_type()}')
