from abc import ABCMeta, abstractmethod
import logging
import time

logging.basicConfig(level=logging.INFO)


class PooledObject:
    """池(化)对象"""

    def __init__(self, obj):
        self.__obj = obj
        self.__is_busy = False

    @property
    def is_busy(self):
        return self.__is_busy

    @is_busy.setter
    def is_busy(self, is_busy):
        self.__is_busy = is_busy

    @property
    def obj(self):
        return self.__obj


class ObjectPool(metaclass=ABCMeta):
    """对象池"""

    # 对象池初始化大小
    InitialNumOfObjects = 10
    # 对象池最大的大小
    MaxNumOfObjects = 50

    def __init__(self):
        self.__pools = []
        for i in range(ObjectPool.InitialNumOfObjects):
            obj = self.create_pooled_object()
            self.__pools.append(obj)

    @abstractmethod
    def create_pooled_object(self):
        pass

    def borrow_object(self):
        """借用对象"""
        obj = self._find_free_object()
        if obj is None:
            if len(self.__pools) < ObjectPool.MaxNumOfObjects:
                obj = self.add_object()
            else:
                return None

        logging.info(f'{id(obj)}对象已被借用, time: {time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))}')
        return obj

    def return_object(self, obj):
        """归还对象"""
        for pooled_obj in self.__pools:
            if pooled_obj.obj == obj:
                pooled_obj.is_busy = False
                logging.info(f'{id(obj)} 对象已归还, time: {time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))}')

    def add_object(self):
        """添加新对象"""
        pooled_obj = self.create_pooled_object()
        self.__pools.append(pooled_obj)
        logging.info(f'添加新对象{id(pooled_obj.obj)}, time: {time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))}')
        pooled_obj.is_busy = True
        return pooled_obj.obj

    def clear(self):
        """清空对象池"""
        self.__pools.clear()

    def _find_free_object(self):
        """查找空闲的对象"""
        obj = None
        for pooled_obj in self.__pools:
            if not pooled_obj.is_busy:
                pooled_obj.is_busy = True
                obj = pooled_obj.obj
                break
        return obj


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
        print(f'序列号: {self.__serial_num:03} 电量: {self.__electric_quantity}% 使用者: {self.__user}')


class PowerBankPool(ObjectPool):
    """存放移动电源的智能箱盒"""

    __serial = 0

    @classmethod
    def get_serial(cls):
        cls.__serial += 1
        return cls.__serial

    def create_pooled_object(self):
        power_bank = PowerBank(PowerBankPool.get_serial(), 100)
        return PooledObject(power_bank)


if __name__ == '__main__':
    power_bank_pool = PowerBankPool()
    power_bank_1 = power_bank_pool.borrow_object()
    if power_bank_1:
        power_bank_1.user = 'Tony'
        power_bank_1.show_info()
    power_bank_2 = power_bank_pool.borrow_object()
    if power_bank_2:
        power_bank_2.user = 'Sam'
        power_bank_2.show_info()
    power_bank_pool.return_object(power_bank_1)
    power_bank_3 = power_bank_pool.borrow_object()
    if power_bank_3:
        power_bank_3.user = 'Aimee'
        power_bank_3.show_info()
    power_bank_pool.return_object(power_bank_2)
    power_bank_pool.return_object(power_bank_3)
    power_bank_pool.clear()
