from abc import ABCMeta, abstractmethod


class ComputerComponent(metaclass=ABCMeta):
    """组件，所有子配件的基类"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def is_composite(self):
        return False

    @abstractmethod
    def show_info(self, indent):
        pass

    def startup(self, indent):
        print(f'{indent}{self.name} 准备开始工作...')

    def shutdown(self, indent):
        print(f'{indent}{self.name} 即将结束工作...')


class CPU(ComputerComponent):
    """中央处理器"""

    def show_info(self, indent):
        print(f'{indent}CPU: {self.name}, 可以进行高速计算。')


class MemoryCard(ComputerComponent):
    """内存条"""

    def show_info(self, indent):
        print(f'{indent}内存: {self.name}, 可以缓存数据, 读写速度快。')


class HardDisk(ComputerComponent):
    """硬盘"""

    def show_info(self, indent):
        print(f'{indent}硬盘: {self.name}, 可以永久存储数据, 容量大。')


class GraphicsCard(ComputerComponent):
    """显卡"""

    def show_info(self, indent):
        print(f'{indent}显卡: {self.name}, 可以高速计算和处理图形图像。')


class Battery(ComputerComponent):
    """电源"""

    def show_info(self, indent):
        print(f'{indent}电源: {self.name}, 可以持续给主板和外接配件供电。')


class Fan(ComputerComponent):
    """风扇"""

    def show_info(self, indent):
        print(f'{indent}风扇: {self.name}, 辅助 CPU 散热')


class Displayer(ComputerComponent):
    """显示器"""

    def show_info(self, indent):
        print(f'{indent}显示器: {self.name}, 负责内容的显示。')


class ComputerComposite(ComputerComponent):
    """配件组合器"""

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def is_composite(self):
        return True

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        self._components.remove(component)

    def show_info(self, indent):
        print(f'{self.name}, 由以下部件组成:')
        indent += '\t'
        for component in self._components:
            component.show_info(indent)

    def startup(self, indent=''):
        super().startup(indent)
        indent += '\t'
        for component in self._components:
            component.startup(indent)

    def shutdown(self, indent=''):
        super().shutdown(indent)
        indent += '\t'
        for component in self._components:
            component.shutdown(indent)


class MainBoard(ComputerComposite):
    """主板"""

    def show_info(self, indent):
        print(f'{indent}主板: ', end='')
        super().show_info(indent)


class ComputerCase(ComputerComposite):
    """机箱"""

    def show_info(self, indent):
        print(f'{indent}机箱: ', end='')
        super().show_info(indent)


class Computer(ComputerComposite):
    """电脑"""

    def show_info(self, indent=''):
        print(f'{indent}电脑: ', end='')
        super().show_info(indent)


if __name__ == '__main__':
    main_board = MainBoard('GIGABYTE Z170M M-ATX')
    main_board.add_component(CPU('Intel Core i5-6600K'))
    main_board.add_component(MemoryCard('Kingston Fury DDR4'))
    main_board.add_component(HardDisk('Kingston V300'))
    main_board.add_component(GraphicsCard('Colorful iGame750'))

    computer_case = ComputerCase('SAMA MATX')
    computer_case.add_component(main_board)
    computer_case.add_component(Battery('Antec VP 450P'))
    computer_case.add_component(Fan('DEEPCOOL 120T'))

    computer = Computer('Tony DIY 电脑')
    computer.add_component(computer_case)
    computer.add_component(Displayer('AOC LV243XIP'))

    computer.show_info()
    print()

    print('开机过程')
    computer.startup()
    print()

    print('关机过程:')
    computer.shutdown()
