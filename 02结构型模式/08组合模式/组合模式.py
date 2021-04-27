from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    """组件"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def is_composite(self):
        return False

    @abstractmethod
    def feature(self, indent):
        pass


class Composite(Component):
    """复合组件"""

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def is_composite(self):
        return True

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        self._components.remove(component)

    def feature(self, indent):
        indent += '\t'
        for component in self._components:
            component.feature(indent)
