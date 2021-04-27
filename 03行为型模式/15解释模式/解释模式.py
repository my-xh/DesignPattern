from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    """抽象表达式"""

    @abstractmethod
    def interpreter(self, var):
        pass


class VarExpression(Expression):
    """变量解析器"""

    def __init__(self, key):
        self.__key = key

    def interpreter(self, var):
        return var.get(self.__key)


class SymbolExpression(Expression):
    """运算符解析器，运算符的抽象类"""

    def __init__(self, left: VarExpression, right: VarExpression):
        self._left = left
        self._right = right


class AddExpression(SymbolExpression):
    """加法解析器"""

    def interpreter(self, var):
        return self._left.interpreter(var) + self._right.interpreter(var)


class SubExpression(SymbolExpression):
    """减法解析器"""

    def interpreter(self, var):
        return self._left.interpreter(var) - self._right.interpreter(var)


class Stack:
    """栈"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


class Calculator:
    """计算器类"""

    def __init__(self, exp):
        self.__expression = self.parse_text(exp)

    def parse_text(self, exp):
        stack = Stack()
        left = right = None
        idx = 0

        while idx < len(exp):
            if exp[idx] == '+':
                left = stack.pop()
                idx += 1
                right = VarExpression(exp[idx])
                stack.push(AddExpression(left, right))
            elif exp[idx] == '-':
                left = stack.pop()
                idx += 1
                right = VarExpression(exp[idx])
                stack.push(SubExpression(left, right))
            else:
                stack.push(VarExpression(exp[idx]))
            idx += 1

        return stack.pop()

    def run(self, var):
        return self.__expression.interpreter(var)


def get_map_value(exp_str):
    pre_idx = 0
    new_exp = []
    expression_map = {}

    for i in range(len(exp_str)):
        if exp_str[i] in {'+', '-'}:
            key = exp_str[pre_idx: i].strip()
            new_exp.append(key)
            new_exp.append(exp_str[i])
            value = input(f'请输入参数{key}的值: ').strip()
            expression_map[key] = float(value)
            pre_idx = i + 1
    key = exp_str[pre_idx:].strip()
    new_exp.append(key)
    value = input(f'请输入参数{key}的值: ').strip()
    expression_map[key] = float(value)

    return new_exp, expression_map


def test_calculator():
    exp_str = input('请输入表达式: ')
    new_exp, expression_map = get_map_value(exp_str)
    calculator = Calculator(new_exp)
    print(f'运算结果为: {exp_str} = {calculator.run(expression_map)}')


if __name__ == '__main__':
    test_calculator()
