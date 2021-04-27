from abc import ABCMeta, abstractmethod


class Abstraction(metaclass=ABCMeta):
    """抽象化角色"""

    def __init__(self, implementor):
        self._implementor = implementor

    @abstractmethod
    def operation(self):
        pass


class RefinedAbstraction(Abstraction):
    """抽象化角色的具体实现类"""

    def operation(self):
        self._implementor.operation_impl()
        print('抽象化角色的方法')


class Implementor(metaclass=ABCMeta):
    """实现化角色"""

    @abstractmethod
    def operation_impl(self):
        pass


class ImplementorImpl(Implementor):
    """具体的实现化角色"""

    def operation_impl(self):
        print('实现化角色的方法')


if __name__ == '__main__':
    obj = RefinedAbstraction(ImplementorImpl())
    obj.operation()
