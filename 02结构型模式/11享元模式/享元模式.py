from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):
    """享元类"""

    @abstractmethod
    def operation(self, extrinsic_state):
        pass


class Pigment(Flyweight):
    """享元类的具体实现类"""

    def __init__(self, color):
        self.__color = color

    def operation(self, extrinsic_state):
        print(f'{extrinsic_state} 取得 {self.__color}色颜料')


class FlyweightFactory:
    """享元工厂"""

    def __init__(self):
        self.__flyweights = {}

    def get_flyweight(self, color):
        if color not in self.__flyweights:
            self.__flyweights[color] = Pigment(color)
        return self.__flyweights[color]


if __name__ == '__main__':
    factory = FlyweightFactory()
    factory.get_flyweight('红').operation('梦之队')
    factory.get_flyweight('黄').operation('梦之队')
    factory.get_flyweight('蓝').operation('梦之队')
    factory.get_flyweight('蓝').operation('和平队')
