from copy import copy, deepcopy


class Clone:
    """克隆的基类"""

    def clone(self):
        """浅拷贝"""
        return copy(self)

    def deep_clone(self):
        """深拷贝"""
        return deepcopy(self)


class Person(Clone):
    """人"""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_myself(self):
        print(f'我是 {self.__name}, 年龄 {self.__age} .')

    def coding(self):
        print('我是码农，我用程序改变世界，Coding......')

    def reading(self):
        print('阅读使我快乐! 知识使我成长! 如饥似渴地阅读是生活的一部分......')

    def fall_in_love(self):
        print('春风吹, 月亮明, 花前月下好相约......')


if __name__ == '__main__':
    tony = Person('tony', 27)
    tony.show_myself()
    tony.coding()
    print()

    tony1 = tony.clone()
    tony1.show_myself()
    tony1.reading()
    print()

    tony2 = tony.deep_clone()
    tony2.show_myself()
    tony2.fall_in_love()
