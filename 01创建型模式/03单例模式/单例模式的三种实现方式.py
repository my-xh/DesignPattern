# 重写__new__和__init__方法
class Singleton1:
    __instance = None
    __name = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__name:
            self.__name = name

    @property
    def name(self):
        return self.__name


# 自定义metaclass的方法
class SingletonMeta(type):

    def __init__(cls, name, bases=None, attrs=None):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Singleton2(metaclass=SingletonMeta):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


# 装饰器的方法
def singleton(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


@singleton
class Singleton3:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

if __name__ == '__main__':
    tony = Singleton1('tony')
    karry = Singleton1('karry')
    print(tony.name, karry.name)
    print(f'id(tony): {id(tony)}, id(karry): {id(karry)}')
    print(f'tony == karry: {tony == karry}')

    print()

    tony = Singleton2('tony')
    karry = Singleton2('karry')
    print(tony.name, karry.name)
    print(f'id(tony): {id(tony)}, id(karry): {id(karry)}')
    print(f'tony == karry: {tony == karry}')

    print()

    tony = Singleton3('tony')
    karry = Singleton3('karry')
    print(tony.name, karry.name)
    print(f'id(tony): {id(tony)}, id(karry): {id(karry)}')
    print(f'tony == karry: {tony == karry}')
