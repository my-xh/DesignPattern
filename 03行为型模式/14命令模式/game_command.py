import time
from abc import ABCMeta, abstractmethod


class GameRole:
    """游戏角色"""

    # 每次移动的步距
    STEP = 5

    def __init__(self, name):
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def left_move(self):
        self.__x -= self.STEP

    def right_move(self):
        self.__x += self.STEP

    def up_move(self):
        self.__y += self.STEP

    def down_move(self):
        self.__y -= self.STEP

    def jump_move(self):
        self.__z += self.STEP

    def squat_move(self):
        self.__z -= self.STEP

    def attack(self):
        print(f'{self.__name} 发动攻击...')

    def show_position(self):
        print(f'{self.__name} 的位置: (x: {self.__x}, y: {self.__y}, z: {self.__z})')


class GameCommand(metaclass=ABCMeta):
    """游戏角色的命令类"""

    def __init__(self, role: GameRole):
        self._role = role

    def set_role(self, role):
        self._role = role

    @abstractmethod
    def execute(self):
        pass


class Left(GameCommand):
    """左移命令"""

    def execute(self):
        self._role.left_move()
        self._role.show_position()


class Right(GameCommand):
    """右移命令"""

    def execute(self):
        self._role.right_move()
        self._role.show_position()


class Up(GameCommand):
    """上移命令"""

    def execute(self):
        self._role.up_move()
        self._role.show_position()


class Down(GameCommand):
    """下移命令"""

    def execute(self):
        self._role.down_move()
        self._role.show_position()


class Jump(GameCommand):
    """弹跳命令"""

    def execute(self):
        self._role.jump_move()
        self._role.show_position()
        # 跳起后空中停留0.5秒
        time.sleep(0.5)


class Squat(GameCommand):
    """下蹲命令"""

    def execute(self):
        self._role.squat_move()
        self._role.show_position()
        # 下蹲后伏地半秒
        time.sleep(0.5)


class Attack(GameCommand):
    """攻击命令"""

    def execute(self):
        self._role.attack()


class MacroCommand(GameCommand):
    """宏命令，也就是组合命令"""

    def __init__(self, role=None):
        super().__init__(role)
        self.__commands = []

    def add_command(self, command):
        self.__commands.append(command)

    def remove_command(self, command):
        self.__commands.remove(command)

    def execute(self):
        for cmd in self.__commands:
            cmd.execute()


class GameInvoker:
    """命令调度者"""

    def __init__(self):
        self.__command = None

    def set_command(self, command):
        self.__command = command
        return self

    def action(self):
        if self.__command is not None:
            self.__command.execute()


def test_game():
    """在控制台用字符模拟命令"""
    role = GameRole('常山赵子龙')
    invoker = GameInvoker()

    while True:
        str_cmd = input('请输入命令: ')
        str_cmd = str_cmd.upper()

        if str_cmd == 'L':
            cmd = Left(role)
        elif str_cmd == 'R':
            cmd = Right(role)
        elif str_cmd == 'U':
            cmd = Up(role)
        elif str_cmd == 'D':
            cmd = Down(role)
        elif str_cmd == 'A':
            cmd = Attack(role)
        elif str_cmd == 'LU':
            cmd = MacroCommand()
            cmd.add_command(Left(role))
            cmd.add_command(Up(role))
        elif str_cmd == 'LD':
            cmd = MacroCommand()
            cmd.add_command(Left(role))
            cmd.add_command(Down(role))
        elif str_cmd == 'RU':
            cmd = MacroCommand()
            cmd.add_command(Right(role))
            cmd.add_command(Up(role))
        elif str_cmd == 'RD':
            cmd = MacroCommand()
            cmd.add_command(Right(role))
            cmd.add_command(Down(role))
        elif str_cmd == 'LA':
            cmd = MacroCommand()
            cmd.add_command(Left(role))
            cmd.add_command(Attack(role))
        elif str_cmd == 'RA':
            cmd = MacroCommand()
            cmd.add_command(Right(role))
            cmd.add_command(Attack(role))
        elif str_cmd == 'UA':
            cmd = MacroCommand()
            cmd.add_command(Up(role))
            cmd.add_command(Attack(role))
        elif str_cmd == 'DA':
            cmd = MacroCommand()
            cmd.add_command(Down(role))
            cmd.add_command(Attack(role))
        elif str_cmd == 'JP':
            cmd = MacroCommand()
            cmd.add_command(Jump(role))
            cmd.add_command(Squat(role))
        elif str_cmd == 'JA':
            cmd = MacroCommand()
            cmd.add_command(Jump(role))
            cmd.add_command(Attack(role))
            cmd.add_command(Squat(role))
        elif str_cmd == 'Q':
            break
        else:
            print(f'不存在的命令: {str_cmd}, 请重新输入!')
            continue

        invoker.set_command(cmd).action()


if __name__ == '__main__':
    test_game()
