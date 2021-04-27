class MyBeautifulGril:
    """我的漂亮女神"""
    __instance = None
    __name = None

    def __new__(cls, name):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__name:
            self.__name = name
            print(f'遇见 {name}, 我一见钟情!')
        else:
            print(f'遇见 {name}, 我置若罔闻!')

    def show_myheart(self):
        print(f'{self.__name} 就是我心中的唯一!')


# 单例模式装饰器
def singleton(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


@singleton
class MyBeautifulGril2:

    def __init__(self, name):
        self.__name = name
        if self.__name == name:
            print(f'遇见 {name}, 我一见钟情!')
        else:
            print(f'遇见 {name}, 我置若罔闻!')

    def show_myheart(self):
        print(f'{self.__name} 就是我心中的唯一!')


if __name__ == '__main__':
    jenny = MyBeautifulGril('jenny')
    jenny.show_myheart()

    kimi = MyBeautifulGril('kimi')
    kimi.show_myheart()

    print(f'id(jenny): {id(jenny)}, id(kimi): {id(kimi)}')

    print('-' * 20)

    jenny = MyBeautifulGril2('jenny')
    jenny.show_myheart()

    kimi = MyBeautifulGril2('kimi')
    kimi.show_myheart()

    print(f'id(jenny): {id(jenny)}, id(kimi): {id(kimi)}')
