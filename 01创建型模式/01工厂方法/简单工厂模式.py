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


class Coffeemaker:
    """咖啡机"""

    @staticmethod
    def make_coffee(coffee_bean):
        if coffee_bean == '拿铁咖啡豆':
            coffee = LatteCoffee('拿铁咖啡')
        elif coffee_bean == '摩卡咖啡豆':
            coffee = MochaCoffee('摩卡咖啡')
        else:
            raise ValueError(f'不支持的参数: {coffee_bean}')

        return coffee


if __name__ == '__main__':
    latte = Coffeemaker.make_coffee('拿铁咖啡豆')
    print(f'{latte.name} 已为您准备好了, 口感: {latte.get_taste()}。请慢慢享用!')
    mocha = Coffeemaker.make_coffee('摩卡咖啡豆')
    print(f'{mocha.name} 已为您准备好了, 口感: {mocha.get_taste()}。请慢慢享用!')
