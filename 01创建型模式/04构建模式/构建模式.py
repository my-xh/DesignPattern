from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    """玩具"""

    def __init__(self, name):
        self.__name = name
        self.__components = []

    @property
    def name(self):
        return self.__name

    def add_component(self, component, count=1, unit='个'):
        self.__components.append([component, count, unit])
        print(f'{self.name} 增加了 {count} {unit}{component}')

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """小车"""

    def feature(self):
        print(f'我是 {self.name}, 我可以快速奔跑...')


class Manor(Toy):
    """庄园"""

    def feature(self):
        print(f'我是 {self.name}, 我可供观赏, 也可用来游玩!')


class ToyBuilder(metaclass=ABCMeta):
    """玩具构建者"""

    @abstractmethod
    def build_product(self):
        pass


class CarBuilder(ToyBuilder):
    """小车构建者"""

    def build_product(self):
        car = Car('迷你小车')
        print(f'正在构建 {car.name}......')
        car.add_component('轮子', 4)
        car.add_component('车身')
        car.add_component('发动机')
        car.add_component('方向盘')
        return car


class ManorBuilder(ToyBuilder):
    """庄园构建者"""

    def build_product(self):
        manor = Manor('淘淘小庄园')
        print(f'正在构建 {manor.name}......')
        manor.add_component('客厅', 1, '间')
        manor.add_component('卧室', 2, '间')
        manor.add_component('书房', 1, '间')
        manor.add_component('厨房', 1, '间')
        manor.add_component('花园')
        manor.add_component('围墙', 1, '堵')
        return manor


class BuilderManager:
    """构建管理类"""

    def __init__(self):
        self.__car_builder = CarBuilder()
        self.__manor_builder = ManorBuilder()

    def build_car(self, num):
        products = []
        for i in range(num):
            car = self.__car_builder.build_product()
            products.append(car)
            print(f'构建完成第 {i + 1} 个 {car.name}')
        return products

    def build_manor(self, num):
        products = []
        for i in range(num):
            manor = self.__manor_builder.build_product()
            products.append(manor)
            print(f'构建完成第 {i + 1} 个 {manor.name}')
        return products


if __name__ == '__main__':
    builder_mgr = BuilderManager()
    builder_mgr.build_manor(2)
    print()
    builder_mgr.build_car(4)
