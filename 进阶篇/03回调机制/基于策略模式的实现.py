from abc import ABCMeta, abstractmethod


class Skill(metaclass=ABCMeta):
    """技能的抽象类"""

    @abstractmethod
    def performance(self):
        pass


class Employee:
    """公司新员工"""

    def __init__(self, name):
        self.__name = name

    def do_performance(self, skill: Skill):
        print(f'{self.__name} 的表演: ', end='')
        skill.performance()


class Sing(Skill):
    """唱歌"""

    def performance(self):
        print('唱一首歌')


class Dling(Skill):
    """拉 Ukulele"""

    def performance(self):
        print('弹一首 Ukulele 曲子')


class Joke(Skill):
    """说段子"""

    def performance(self):
        print('说一个搞笑段子')


class PerformMagicTricks(Skill):
    """表演魔术"""

    def performance(self):
        print('神秘魔术')


class Skateboarding(Skill):
    """玩滑板"""

    def performance(self):
        print('炫酷滑板')


if __name__ == '__main__':
    helen = Employee('Helen')
    helen.do_performance(Sing())
    frank = Employee('Frank')
    frank.do_performance(Dling())
    jacky = Employee('Jacky')
    jacky.do_performance(Joke())
    chork = Employee('Chork')
    chork.do_performance(PerformMagicTricks())
    kerry = Employee('Kerry')
    kerry.do_performance(Skateboarding())
