class Employee:
    """公司员工"""

    def __init__(self, name):
        self.__name = name

    def do_performance(self, skill):
        print(f'{self.__name} 的表演: ', end='')
        skill()


def sing():
    print('唱一首歌')


def dling():
    print('弹一首 Ukulele 曲子')


def joke():
    print('说一个搞笑段子')


def perform_magic_tricks():
    print('神秘魔术')


def skateboarding():
    print('炫酷滑板')


if __name__ == '__main__':
    helen = Employee('Helen')
    helen.do_performance(sing)
    frank = Employee('Frank')
    frank.do_performance(dling)
    jacky = Employee('Jacky')
    jacky.do_performance(joke)
    chork = Employee('Chork')
    chork.do_performance(perform_magic_tricks)
    kerry = Employee('Kerry')
    kerry.do_performance(skateboarding)
