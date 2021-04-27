from abc import ABCMeta, abstractmethod


class HomeAppliances(metaclass=ABCMeta):
    """家电抽象类"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def running(self):
        pass


class Refrigerator(HomeAppliances):
    """冰箱"""

    def running(self):
        print(f'{self.name} 可以冷藏食物...')


class EfficientRefrigerator(Refrigerator):
    """高效型冰箱"""

    def running(self):
        print('(高效型)', end='')
        super().running()


class EnergySavingRefrigerator(Refrigerator):
    """节能型冰箱"""

    def running(self):
        print('(节能型)', end='')
        super().running()


class AppliancesFactory(metaclass=ABCMeta):
    """家电工厂抽象类"""

    @staticmethod
    @abstractmethod
    def create_refrigerator():
        pass

    @staticmethod
    @abstractmethod
    def create_air_conditioner():
        pass

    @staticmethod
    @abstractmethod
    def create_washing_machine():
        pass


class EfficientFactory(AppliancesFactory):
    """高效型家电工厂"""

    @staticmethod
    def create_refrigerator():
        return EfficientRefrigerator('冰箱')

    @staticmethod
    def create_air_conditioner():
        pass

    @staticmethod
    def create_washing_machine():
        pass


class EnergySavingFactory(AppliancesFactory):
    """节能型家电工厂"""

    @staticmethod
    def create_refrigerator():
        return EnergySavingRefrigerator('冰箱')

    @staticmethod
    def create_air_conditioner():
        pass

    @staticmethod
    def create_washing_machine():
        pass


if __name__ == '__main__':
    efficient_refrigerator = EfficientFactory.create_refrigerator()
    efficient_refrigerator.running()
    print()
    energy_saving_regrigerator = EnergySavingFactory.create_refrigerator()
    energy_saving_regrigerator.running()
