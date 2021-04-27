from abc import ABCMeta, abstractmethod


class SocketEntity:
    """接口类型定义"""

    def __init__(self, num_of_pin, type_of_pin):
        self.__num_of_pin = num_of_pin
        self.__type_of_pin = type_of_pin

    @property
    def num_of_pin(self):
        return self.__num_of_pin

    @num_of_pin.setter
    def num_of_pin(self, num):
        self.__num_of_pin = num

    @property
    def type_of_pin(self):
        return self.__type_of_pin

    @type_of_pin.setter
    def type_of_pin(self, _type):
        self.__type_of_pin = _type


class ISocket(metaclass=ABCMeta):
    """插座类型"""

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_socket(self):
        pass


class ChineseSocket(ISocket):
    """国标插座"""

    def get_name(self):
        return '国标插座'

    def get_socket(self):
        return SocketEntity(3, '八字扁型')


class BritishSocket:
    """英标插座"""

    def name(self):
        return '英标插座'

    def socket_interface(self):
        return SocketEntity(3, 'T字方形')


class AdapterSocket(ISocket):
    """插座转换器"""

    def __init__(self, british_socket):
        self.__british_socket = british_socket

    def get_name(self):
        return self.__british_socket.name() + '转换器'

    def get_socket(self):
        socket = self.__british_socket.socket_interface()
        socket.type_of_pin = '八字扁型'
        return socket


def can_charge_for_digital_device(name, socket):
    if socket.num_of_pin == 3 and socket.type_of_pin == '八字扁型':
        is_standard = '符合'
        can_charge = '可以'
    else:
        is_standard = '不符合'
        can_charge = '不能'

    print(f'[{name}]:\n针脚数量: {socket.num_of_pin}, 针脚类型: {socket.type_of_pin}; {is_standard}中国标准, {can_charge}给中国内地的电子设备充电!')


if __name__ == '__main__':
    chinese_socket = ChineseSocket()
    can_charge_for_digital_device(
        chinese_socket.get_name(), chinese_socket.get_socket())

    british_socket = BritishSocket()
    can_charge_for_digital_device(
        british_socket.name(), british_socket.socket_interface())

    adapter_socket = AdapterSocket(british_socket)
    can_charge_for_digital_device(
        adapter_socket.get_name(), adapter_socket.get_socket())
