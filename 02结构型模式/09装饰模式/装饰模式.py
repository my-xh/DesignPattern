from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    """人"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def wear(self):
        print('着装: ')


class Engineer(Person):
    """工程师"""

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    def wear(self):
        print(f'我是 {self.skill}工程师 {self.name}', end=', ')
        super().wear()


class Teacher(Person):
    """教师"""

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    @property
    def title(self):
        return self.__title

    def wear(self):
        print(f'我是 {self.name} {self.title}', end=', ')
        super().wear()


class ClothingDecorator(Person, metaclass=ABCMeta):
    """服装装饰器的基类"""

    def __init__(self, person):
        self.__decorated = person

    def wear(self):
        self.__decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    """休闲裤装饰器"""

    # def __init__(self, person):
    #     super().__init__(person)

    def decorate(self):
        print('一条卡其色休闲裤')


class BeltDecorator(ClothingDecorator):
    """腰带装饰器"""

    def decorate(self):
        print('一条银色针扣头的黑色腰带')


class LeatherShoesDecorator(ClothingDecorator):
    """皮鞋装饰器"""

    def decorate(self):
        print('一双深色休闲皮鞋')


class KnittedSweaterDecorator(ClothingDecorator):
    """针织毛衣装饰器"""

    def decorate(self):
        print('一件紫红色针织毛衣')


class WhiteShirtDecorator(ClothingDecorator):
    """白色衬衫装饰器"""

    def decorate(self):
        print('一件白色衬衫')


class GlassesDecorator(ClothingDecorator):
    """眼镜装饰器"""

    def decorate(self):
        print("一副方形黑框眼镜")


if __name__ == '__main__':
    tony = Engineer('Tony', '客户端')
    tony = CasualPantDecorator(tony)
    tony = BeltDecorator(tony)
    tony = LeatherShoesDecorator(tony)
    tony = KnittedSweaterDecorator(tony)
    tony = WhiteShirtDecorator(tony)
    tony = GlassesDecorator(tony)
    tony.wear()

    print()

    wells = GlassesDecorator(WhiteShirtDecorator(
        LeatherShoesDecorator(Teacher('wells', '教授'))))
    wells.wear()
