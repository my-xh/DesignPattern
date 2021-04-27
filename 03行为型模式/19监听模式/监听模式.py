from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    """热水器：战胜寒冬的有力武器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    @property
    def temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print(f'当前温度是：{temperature}℃')
        self.notify_observers()


class WashingMode(Observer):
    """该模式用于洗澡"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and 50 <= observable.temperature < 70:
            print('水已烧好！温度正好，可以用来洗澡了。')


class DrinkingMode(Observer):
    """该模式用于饮用"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.temperature >= 100:
            print('水已烧开！可以用来饮用了。')


if __name__ == '__main__':
    heater = WaterHeater()
    heater.add_observer(WashingMode())
    heater.add_observer(DrinkingMode())
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(100)
