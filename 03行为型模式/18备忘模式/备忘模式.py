from copy import deepcopy


class Memento:
    """备忘录"""

    def set_attributes(self, dict):
        self.__dict__ = deepcopy(dict)

    def get_attributes(self):
        return self.__dict__


class Caretaker:
    """备忘录管理类"""

    def __init__(self):
        self._mementos = {}

    def add_memento(self, name, memento):
        self._mementos[name] = memento

    def get_memento(self, name):
        return self._mementos[name]


class Originator:
    """备份发起人"""

    def create_memento(self):
        memento = Memento()
        memento.set_attributes(self.__dict__)
        return memento

    def restore_from_memento(self, memento):
        self.__dict__.update(memento.get_attributes())


if __name__ == '__main__':
    o = Originator()
    caretaker = Caretaker()
    o.x = 1
    print(o.__dict__)

    caretaker.add_memento('1', o.create_memento())
    o.__dict__.clear()
    print(o.__dict__)

    o.restore_from_memento(caretaker.get_memento('1'))
    print(o.__dict__)
