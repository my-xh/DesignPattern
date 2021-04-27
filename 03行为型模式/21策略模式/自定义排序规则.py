from abc import ABCMeta, abstractmethod


class Person:
    """人类"""

    def __init__(self, name, age, weight, height):
        self.__name = name
        self.age = age
        self.weight = weight
        self.height = height

    def show_myself(self):
        print(f'{self.__name} 年龄: {self.age} 岁, 体重: {self.weight:.2f}kg, 身高: {self.height:.2f}m')


class ICompare(metaclass=ABCMeta):
    """比较算法"""

    @abstractmethod
    def comparable(self, person_1, person_2):
        pass


class CompareByAge(ICompare):
    """通过年龄排序"""

    def comparable(self, person_1, person_2):
        return person_1.age - person_2.age


class CompareByHeight(ICompare):
    """通过身高排序"""

    def comparable(self, person_1, person_2):
        return person_1.height - person_2.height


class CompareByHeightAndWeight(ICompare):
    """根据身高和体重的综合情况来排序"""

    def comparable(self, person_1, person_2):
        value_1 = person_1.height * 0.6 + person_1.weight * 0.4
        value_2 = person_2.height * 0.6 + person_2.weight * 0.4
        return value_1 - value_2


class SortPerson:
    """Person的排序类"""

    def __init__(self, compare):
        self.__compare = compare

    def sort(self, person_list):
        """排序算法"""
        n = len(person_list)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.__compare.comparable(person_list[j], person_list[j + 1]) > 0:
                    person_list[j], person_list[
                        j + 1] = person_list[j + 1], person_list[j]


if __name__ == '__main__':
    person_list = [
        Person('Tony', 2, 54.5, 0.82),
        Person('Jack', 31, 74.5, 1.8),
        Person('Nick', 54, 44.5, 1.59),
        Person('Eric', 23, 62, 1.78),
        Person('Helen', 16, 45.7, 1.6),
    ]
    age_sorter = SortPerson(CompareByAge())
    age_sorter.sort(person_list)
    for person in person_list:
        person.show_myself()

    print()

    height_sorter = SortPerson(CompareByHeight())
    height_sorter.sort(person_list)
    for person in person_list:
        person.show_myself()

    print()

    height_and_weight_sorter = SortPerson(CompareByHeightAndWeight())
    height_and_weight_sorter.sort(person_list)
    for person in person_list:
        person.show_myself()
