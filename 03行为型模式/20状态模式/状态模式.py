from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    """状态类"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def is_match(self, state_info):
        """状态的属性state_info是否在当前的状态范围内"""
        return False

    @abstractmethod
    def behavior(self, context):
        pass


class Context:
    """上下文环境类"""

    def __init__(self):
        self.__states = []
        self.__cur_state = None
        self.__state_info = 0       # 状态发生变化依赖的属性

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self, state):
        if state is None:
            return False
        if self.__cur_state is None:
            print(f'初始化为 {state.name}')
        else:
            print(f'由 {self.__cur_state.name} 变为 {state.name}')
        self.__cur_state = state
        self.add_state(state)
        return True

    @property
    def state(self):
        return self.__cur_state

    @property
    def state_info(self):
        return self.__state_info

    @state_info.setter
    def state_info(self, info):
        self.__state_info = info
        for state in self.__states:
            if state.is_match(info):
                self.change_state(state)


# 单例装饰器
def singleton(cls):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState(State):
    """固态"""

    def __init__(self, name='固态'):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info <= 0

    def behavior(self, context):
        print(f'我性格高冷，当前体温{context.state_info}，我坚如钢铁，彷如一冷血动物，请用我砸人，嘻嘻……')


@singleton
class LiquidState(State):
    """液态"""

    def __init__(self, name='液态'):
        super().__init__(name)

    def is_match(self, state_info):
        return 0 < state_info < 100

    def behavior(self, context):
        print(f'我性格温和，当前体温{context.state_info}，我可滋润万物，饮用我可让你活力倍增……')


@singleton
class GaseousState(State):
    """气态"""

    def __init__(self, name='气态'):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info >= 100

    def behavior(self, context):
        print(f'我性格热烈，当前体温{context.state_info}，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将到达无我的境界……')


class Water(Context):
    """水（H2O）"""

    def __init__(self):
        super().__init__()
        self.add_state(SolidState())
        self.add_state(LiquidState())
        self.add_state(GaseousState())
        self.set_temperature(25)

    @property
    def temperature(self):
        return self.state_info

    def set_temperature(self, temperature):
        self.state_info = temperature

    def rise_temperature(self, step):
        self.state_info += step

    def reduce_temperature(self, step):
        self.state_info -= step

    def behavior(self):
        state = self.state
        if isinstance(state, State):
            state.behavior(self)


if __name__ == '__main__':
    water = Water()
    water.behavior()
    water.reduce_temperature(30)
    water.behavior()
    water.rise_temperature(18)
    water.behavior()
    water.rise_temperature(110)
    water.behavior()
