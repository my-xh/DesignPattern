from abc import ABCMeta, abstractmethod


class Request:
    """请假内容"""

    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason

    @property
    def name(self):
        return self.__name

    @property
    def dayoff(self):
        return self.__dayoff

    @property
    def reason(self):
        return self.__reason


class Responsible(metaclass=ABCMeta):
    """责任人抽象类"""

    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._next_handler = None

    @property
    def name(self):
        return self.__name

    @property
    def title(self):
        return self.__title

    @property
    def next_handler(self):
        return self._next_handler

    @next_handler.setter
    def next_handler(self, handler):
        self._next_handler = handler

    def handle_request(self, request):
        """处理请求"""
        self._handle(request)
        if self.next_handler is not None:
            self.next_handler.handle_request(request)

    @abstractmethod
    def _handle(self, request):
        """真正处理请求的方法"""
        pass


class Person:
    """请假人"""

    def __init__(self, name):
        self.__name = name
        self.__leader = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def leader(self):
        return self.__leader

    @leader.setter
    def leader(self, leader):
        self.__leader = leader

    def send_request(self, request):
        print(f'{self.__name} 申请请假 {request.dayoff} 天。请假事由: {request.reason}')
        if self.leader is not None:
            self.leader.handle_request(request)


class Supervisor(Responsible):
    """主管"""

    def _handle(self, request):
        if request.dayoff <= 2:
            print(f'同意 {request.name} 请假, 签字人: {self.name}({self.title})')


class DepartmentManager(Responsible):
    """部门总监"""

    def _handle(self, request):
        if 2 < request.dayoff <= 5:
            print(f'同意 {request.name} 请假, 签字人: {self.name}({self.title})')


class CEO(Responsible):
    """CEO"""

    def _handle(self, request):
        if 5 < request.dayoff <= 22:
            print(f'同意 {request.name} 请假, 签字人: {self.name}({self.title})')


class Administrator(Responsible):
    """行政人员"""

    def _handle(self, request):
        print(f'{request.name} 的请假申请已审核, 情况属实! 已备案处理。处理人: {self.name}({self.title})')


if __name__ == '__main__':
    direct_leader = Supervisor('Eren', '客户端研发部经理')
    department_leader = DepartmentManager('Eric', '技术研发中心总监')
    ceo = CEO('Helen', '创新文化公司 CEO')
    administrator = Administrator('Nina', '行政中心总监')
    direct_leader.next_handler = department_leader
    department_leader.next_handler = ceo
    ceo.next_handler = administrator

    sunny = Person('Sunny')
    sunny.leader = direct_leader
    sunny.send_request(Request(sunny.name, 1, '参加 MDCC 大会。'))
    tony = Person('Tony')
    tony.leader = direct_leader
    tony.send_request(Request(tony.name, 5, '家里有紧急事情!'))
    pony = Person('Pony')
    pony.leader = direct_leader
    pony.send_request(Request(pony.name, 15, '出国深造。'))
