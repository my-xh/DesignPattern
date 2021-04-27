from abc import ABCMeta, abstractmethod
from enum import Enum


class DeviceType(Enum):
    """设备类型"""
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3


class DeviceItem:
    """设备项"""

    def __init__(self, id, name, type, is_default=False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__is_default = is_default

    def __str__(self):
        return f'name: {self.name}, id: {self.id}, type: {self.type}, is_default: {self.is_default}'

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def is_default(self):
        return self.__is_default


class DeviceList:
    """设备列表"""

    def __init__(self):
        self.__devices = []

    def add(self, device_item):
        self.__devices.append(device_item)

    def get_count(self):
        return len(self.__devices)

    def get_by_index(self, ind):
        if ind < 0 or ind >= self.get_count():
            return None
        return self.__devices[ind]

    def get_by_id(self, id):
        for item in self.__devices:
            if item.id == id:
                return item
        return None


class DeviceMgr(metaclass=ABCMeta):
    """设备管理器抽象类"""

    @abstractmethod
    def enumerate(self):
        """枚举设备列表"""
        pass

    @abstractmethod
    def active(self, device_id):
        """激活指定的设备作为当前要用的设备"""
        pass

    @abstractmethod
    def get_cur_device_id(self):
        """获取当前正在使用的设备ID"""
        pass


class SpeakerMgr(DeviceMgr):
    """扬声器设备管理器"""

    def __init__(self):
        self.__cur_device_id = None

    def enumerate(self):
        devices = DeviceList()
        devices.add(DeviceItem('369dd760-893b-4fe0-89b1-671eca0f0224',
                               'Realtek High Definition Audio', DeviceType.TypeSpeaker))
        devices.add(DeviceItem('59357639-6a43-4b79-8184-f79aed9a0dfc',
                               'NVIDIA High Definition Audio', DeviceType.TypeSpeaker))
        return devices

    def active(self, device_id):
        self.__cur_device_id = device_id

    def get_cur_device_id(self):
        return self.__cur_device_id


class DeviceUtil:
    """设备工具类"""

    def __init__(self):
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()

    @property
    def device_mgrs(self):
        return self.__mgrs

    def get_device_list(self, type):
        return self.device_mgrs[type].enumerate()

    def active(self, type, device_id):
        self.device_mgrs[type].active(device_id)

    def get_cur_device_id(self, type):
        return self.device_mgrs[type].get_cur_device_id()


if __name__ == '__main__':
    device_util = DeviceUtil()
    device_list = device_util.get_device_list(DeviceType.TypeSpeaker)
    print('扬声器设备列表：')
    if device_list.get_count() > 0:
        device_util.active(DeviceType.TypeSpeaker,
                           device_list.get_by_index(0).id)
    for ind in range(0, device_list.get_count()):
        device = device_list.get_by_index(ind)
        print(device)
    print(f'当前使用的设备：{device_list.get_by_id(device_util.get_cur_device_id(DeviceType.TypeSpeaker)).name}')
