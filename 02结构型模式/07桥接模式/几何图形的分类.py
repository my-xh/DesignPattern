from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """形状"""

    def __init__(self, color):
        self._color = color

    def get_shape_info(self):
        return f'{self._color}的{self.shape_type}'

    @abstractmethod
    def shape_type(self):
        pass


class Rectangle(Shape):
    """矩形"""

    @property
    def shape_type(self):
        return '矩形'


class Ellipse(Shape):
    """椭圆"""

    @property
    def shape_type(self):
        return '椭圆'


class Color(metaclass=ABCMeta):
    """颜色"""

    def __str__(self):
        return self.color

    @abstractmethod
    def color(self):
        pass


class Red(Color):
    """红色"""

    @property
    def color(self):
        return '红色'


class Green(Color):
    """绿色"""

    @property
    def color(self):
        return '绿色'


if __name__ == '__main__':
    red_rect = Rectangle(Red())
    print(red_rect.get_shape_info())
    green_rect = Rectangle(Green())
    print(green_rect.get_shape_info())
    red_ellipse = Ellipse(Red())
    print(red_ellipse.get_shape_info())
    green_ellipse = Ellipse(Green())
    print(green_ellipse.get_shape_info())
