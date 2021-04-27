class Customer:
    """客户"""

    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinic = None

    @property
    def name(self):
        return self.__name

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def clinic(self):
        return self.__clinic

    @clinic.setter
    def clinic(self, clinic):
        self.__clinic = clinic

    def register(self, system):
        system.push_customer(self)


class NumeralIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.__idx = -1

    def next(self):
        """移动至下一个元素"""
        if self.__idx < len(self.__data) - 1:
            self.__idx += 1
            return True
        else:
            return False

    def current(self):
        """获取当前的元素"""
        if 0 <= self.__idx < len(self.__data):
            return self.__data[self.__idx]
        else:
            return None


class NumeralSystem:
    """排号系统"""

    __clinics = ('1号诊室', '2号诊室', '3号诊室')

    def __init__(self, name):
        self.__customers = []
        self.__cur_num = 0
        self.__name = name

    def push_customer(self, customer):
        customer.num = self.__cur_num + 1
        customer.clinic = NumeralSystem.__clinics[
            self.__cur_num % len(NumeralSystem.__clinics)]
        self.__customers.append(customer)
        self.__cur_num += 1
        print(f'{customer.name} 您好! 您已在 {self.__name} 成功挂号, 序号: {customer.num:04}, 请耐心等待!')

    def get_iterator(self):
        return NumeralIterator(self.__customers)


if __name__ == '__main__':
    numeral_system = NumeralSystem('挂号台')
    lily = Customer('Lily')
    lily.register(numeral_system)
    pony = Customer('Pony')
    pony.register(numeral_system)
    nick = Customer('Nick')
    nick.register(numeral_system)
    tony = Customer('Tony')
    tony.register(numeral_system)
    print()

    iterator = numeral_system.get_iterator()
    while iterator.next():
        customer = iterator.current()
        print(f'下一位病人 {customer.num:04}({customer.name}) 请到 {customer.clinic} 就诊。')
