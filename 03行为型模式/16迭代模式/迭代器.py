class BaseIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.__idx = -1

    def to_begin(self):
        """将指针移至起始位置"""
        self.__idx = -1

    def to_end(self):
        """将指针移至结尾位置"""
        self.__idx = len(self.__data)

    def next(self):
        """移动至下一个元素"""
        if self.__idx < len(self.__data) - 1:
            self.__idx += 1
            return True
        else:
            return False

    def previous(self):
        """移动至上一个元素"""
        if self.__idx > 0:
            self.__idx -= 1
            return True
        else:
            return False

    def current(self):
        """获取当前位置的元素"""
        if 0 <= self.__idx < len(self.__data):
            return self.__data[self.__idx]
        else:
            return None


if __name__ == '__main__':
    iterator = BaseIterator(range(10))

    print('从前往后遍历:')
    while iterator.next():
        print(iterator.current(), end='\t')
    print()

    print('从后往前遍历:')
    iterator.to_end()
    while iterator.previous():
        print(iterator.current(), end='\t')
    print()
