from abc import ABCMeta, abstractmethod


class Template(metaclass=ABCMeta):
    """模板类"""

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

    def template_method(self):
        """模板方法"""
        self.step_one()
        self.step_two()
        self.step_three()


class TemplateImplA(Template):
    """模板实现类A"""

    def step_one(self):
        print('步骤一')

    def step_two(self):
        print('步骤二')

    def step_three(self):
        print('步骤三')


class TemplateImplB(Template):
    """模板实现类B"""

    def step_one(self):
        print('Step one')

    def step_two(self):
        print('Step two')

    def step_three(self):
        print('Step three')


if __name__ == '__main__':
    TemplateImplA().template_method()
    print()
    TemplateImplB().template_method()
