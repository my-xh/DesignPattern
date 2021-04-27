import logging


class Pigment:
    """颜料"""

    def __init__(self, color):
        self.__color = color
        self.__user = None

    @property
    def color(self):
        return self.__color

    def set_user(self, user):
        self.__user = user
        return self

    def show_info(self):
        print(f'{self.__user} 取得 {self.__color}色颜料')


class PigmentFactory:
    """颜料工厂"""

    def __init__(self):
        self.__pigments = {
            '红': Pigment('红'),
            '黄': Pigment('黄'),
            '蓝': Pigment('蓝'),
            '绿': Pigment('绿'),
            '紫': Pigment('紫'),
        }

    def get_pigment(self, color):
        pigment = self.__pigments.get(color)
        if pigment is None:
            logging.error(f'没有{color} 颜色的颜料!')
        return pigment


if __name__ == '__main__':
    factory = PigmentFactory()
    pigment_red = factory.get_pigment('红').set_user('梦之队')
    pigment_red.show_info()
    pigment_yellow = factory.get_pigment('黄').set_user('梦之队')
    pigment_yellow.show_info()
    pigment_blue_1 = factory.get_pigment('蓝').set_user('梦之队')
    pigment_blue_1.show_info()
    pigment_blue_2 = factory.get_pigment('蓝').set_user('和平队')
    pigment_blue_2.show_info()
