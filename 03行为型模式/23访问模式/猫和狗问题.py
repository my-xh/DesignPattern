from 访问模式 import DataNode, Visitor, ObjectStructure
from abc import abstractmethod


class Animal(DataNode):
    """动物类"""

    def __init__(self, name, is_male, age, weight):
        self.__name = name
        self.__is_male = is_male
        self.__age = age
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def is_male(self):
        return self.__is_male

    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight


class Cat(Animal):
    """猫"""

    def speak(self):
        print('miao~')


class Dog(Animal):
    """狗"""

    def speak(self):
        print('wang~')


class Counter(Visitor):
    """统计类"""

    def count(self, animals: ObjectStructure):
        animals.action(self)
        self.show_info()

    @abstractmethod
    def show_info(self):
        pass


class GenderCounter(Counter):
    """性别统计"""

    def __init__(self):
        self.__male_cat = 0
        self.__female_cat = 0
        self.__male_dog = 0
        self.__female_dog = 0

    def visit(self, animal: Animal):
        if isinstance(animal, Cat):
            if animal.is_male:
                self.__male_cat += 1
            else:
                self.__female_cat += 1
        elif isinstance(animal, Dog):
            if animal.is_male:
                self.__male_dog += 1
            else:
                self.__female_dog += 1
        else:
            print('Not support this type')

    def show_info(self):
        print(f'{self.__male_cat}只雄猫, {self.__female_cat}只雌猫, {self.__male_dog}只雄狗, {self.__female_dog}只雌狗。')


class WeightCounter(Counter):
    """体重统计"""

    def __init__(self):
        self.__cat_num = 0
        self.__cat_weight = 0
        self.__dog_num = 0
        self.__dog_weight = 0

    def visit(self, animal: Animal):
        if isinstance(animal, Cat):
            self.__cat_num += 1
            self.__cat_weight += animal.weight
        elif isinstance(animal, Dog):
            self.__dog_num += 1
            self.__dog_weight += animal.weight
        else:
            print('Not support this type')

    def show_info(self):
        print(f'猫的平均体重是: {self.__cat_weight/self.__cat_num:.2f}kg, 狗的平均体重是: {self.__dog_weight/self.__dog_num:.2f}kg。')


class AgeCounter(Counter):
    """年龄统计"""

    def __init__(self):
        self.__cat_age = 0
        self.__dog_age = 0

    def visit(self, animal: Animal):
        if isinstance(animal, Cat):
            if self.__cat_age < animal.age:
                self.__cat_age = animal.age
        elif isinstance(animal, Dog):
            if self.__dog_age < animal.age:
                self.__dog_age = animal.age
        else:
            print('Not support this type')

    def show_info(self):
        print(f'猫的最大年龄是: {self.__cat_age}, 狗的最大年龄是: {self.__dog_age}')

if __name__ == '__main__':
    animals = ObjectStructure()
    animals.add(Cat('Cat1', True, 1, 5))
    animals.add(Cat('Cat2', False, 0.5, 3))
    animals.add(Cat('Cat3', False, 1.2, 4.2))
    animals.add(Dog('Dog1', True, 0.5, 8))
    animals.add(Dog('Dog2', True, 3, 52))
    animals.add(Dog('Dog3', False, 1, 21))
    animals.add(Dog('Dog4', False, 2, 25))

    GenderCounter().count(animals)
    print()
    WeightCounter().count(animals)
    print()
    AgeCounter().count(animals)
