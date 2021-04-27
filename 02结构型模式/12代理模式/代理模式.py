from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    """主题类"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def request(self, content=''):
        pass


class RealSubject(Subject):
    """真实主题类"""

    def request(self, content):
        print('RealSubject todo something...')


class ProxySubject(Subject):
    """代理主题类"""

    def __init__(self, name, subject=None):
        super().__init__(name)
        self._real_subject = subject

    def _pre_request(self):
        print('preRequest')

    def _after_request(self):
        print('afterRequest')

    def request(self, content=''):
        self._pre_request()
        if self._real_subject is not None:
            self._real_subject.request(content)
        self._after_request()


class TonyReception(Subject):
    """Tony接收"""

    def __init__(self, name, phone_num):
        super().__init__(name)
        self.__phone_num = phone_num

    @property
    def phone_num(self):
        return self.__phone_num

    def request(self, content):
        print(f'货物主人: {self.name}, 手机号: {self.phone_num}')
        print(f'接收到一个包裹, 包裹内容: {str(content)}')


class WendyReception(ProxySubject):
    """Wendy代收"""

    def _pre_request(self):
        print(f'我是 {self._real_subject.name} 的朋友, 我来帮他代收快递')

    def _after_request(self):
        print(f'代收人: {self.name}')


if __name__ == '__main__':
    # real = RealSubject('RealSubject')
    # proxy = ProxySubject('ProxySubject', real)
    # proxy.request()

    print('Tony接收:')
    tony = TonyReception('Tony', 18512345678)
    tony.request('雪地靴')
    print()

    print('Wendy代收:')
    wendy = WendyReception('Wendy', tony)
    wendy.request('雪地靴')
