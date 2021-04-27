class PowerBank:
    """移动电源"""

    def __init__(self, serial_num, electric_quantity):
        self.__serial_num = serial_num
        self.__electric_quantity = electric_quantity
        self.__user = ''

    @property
    def serial_num(self):
        return self.__serial_num

    @property
    def electric_quantity(self):
        return self.__electric_quantity

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    def show_info(self):
        print(f'序列号: {self.__serial_num} 电量: {self.__electric_quantity}% 使用者: {self.__user}')


class ObjectPack:
    """对象的包装类，封装指定的对象是否正在被使用中"""

    def __init__(self, obj, in_using=False):
        self.__obj = obj
        self.__in_using = in_using

    @property
    def in_using(self):
        return self.__in_using

    @in_using.setter
    def in_using(self, in_using):
        self.__in_using = in_using

    @property
    def obj(self):
        return self.__obj


class PowerBankBox:
    """存放移动电源的智能箱盒"""

    def __init__(self):
        self.__pools = {}
        self.__pools['0001'] = ObjectPack(PowerBank('0001', 100))
        self.__pools['0002'] = ObjectPack(PowerBank('0002', 100))

    def borrow(self, serial_num):
        """借用移动电源"""
        res = None
        item = self.__pools.get(serial_num)

        if item is None:
            print(f'没有可用的电源!')
        elif item.in_using:
            print(f'{serial_num} 电源 已被借用!')
        else:
            item.in_using = True
            res = item.obj

        return res

    def give_back(self, serial_num):
        """归还移动电源"""
        item = self.__pools.get(serial_num)
        if item is not None:
            item.in_using = False
            print(f'{serial_num} 电源 已归还!')


if __name__ == '__main__':
    box = PowerBankBox()
    power_bank_1 = box.borrow('0001')
    if power_bank_1 is not None:
        power_bank_1.user = 'Tony'
        power_bank_1.show_info()
    power_bank_2 = box.borrow('0002')
    if power_bank_2 is not None:
        power_bank_2.user = 'Sam'
        power_bank_2.show_info()
    power_bank_3 = box.borrow('0001')
    box.give_back('0001')
    power_bank_3 = box.borrow('0001')
    if power_bank_3 is not None:
        power_bank_3.user = 'Aimee'
        power_bank_3.show_info()
