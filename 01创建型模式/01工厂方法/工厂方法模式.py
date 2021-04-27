from abc import ABCMeta, abstractmethod


class Coffee(metaclass=ABCMeta):
    """咖啡"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def get_taste(self):
        pass


class LatteCoffee(Coffee):
    """拿铁咖啡"""

    def get_taste(self):
        return '轻柔而香醇'


class MochaCoffee(Coffee):
    """摩卡咖啡"""

    def get_taste(self):
        return '丝滑与醇厚'


class Coffeemaker(metaclass=ABCMeta):
    """咖啡机抽象类"""

    @staticmethod
    @abstractmethod
    def make_coffee(coffee_bean):
        pass


class LatteCoffeemaker(Coffeemaker):
    """拿铁咖啡机"""

    @staticmethod
    def make_coffee():
        return LatteCoffee('拿铁咖啡')


class MochaCoffeemaker(Coffeemaker):
    """摩卡咖啡机"""

    @staticmethod
    def make_coffee():
        return MochaCoffee('摩卡咖啡')


if __name__ == '__main__':
    latte = LatteCoffeemaker.make_coffee()
    print(f'{latte.name} 已为您准备好了, 口感: {latte.get_taste()}。请慢慢享用!')
    mocha = MochaCoffeemaker.make_coffee()
    print(f'{mocha.name} 已为您准备好了, 口感: {mocha.get_taste()}。请慢慢享用!')
