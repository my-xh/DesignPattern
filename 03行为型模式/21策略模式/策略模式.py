from abc import ABCMeta, abstractmethod


class IVehicle(metaclass=ABCMeta):
    """交通工具的抽象类"""

    @abstractmethod
    def running(self):
        pass


class SharedBicycle(IVehicle):
    """共享单车"""

    def running(self):
        print('骑共享单车(轻快便捷)', end='')


class ExpressBus(IVehicle):
    """快速公交"""

    def running(self):
        print('坐快速公交(经济绿色)', end='')


class Express(IVehicle):
    """快车"""

    def running(self):
        print('打快车(快速方便)', end='')


class Subway(IVehicle):
    """地铁"""

    def running(self):
        print('坐地铁(高效安全)', end='')


class Classmate:
    """来聚餐的同学"""

    def __init__(self, name, vehicle):
        self.__name = name
        self.__vehicle = vehicle

    def attend_the_dinner(self):
        print(f'{self.__name} ', end='')
        self.__vehicle.running()
        print(' 来聚餐!')


if __name__ == '__main__':
    joe = Classmate('Joe', SharedBicycle())
    joe.attend_the_dinner()
    helen = Classmate('Helen', Subway())
    helen.attend_the_dinner()
    henry = Classmate('Henry', ExpressBus())
    henry.attend_the_dinner()
    ruby = Classmate('Ruby', Express())
    ruby.attend_the_dinner()
