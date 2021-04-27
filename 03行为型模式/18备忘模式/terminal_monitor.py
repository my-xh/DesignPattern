from 备忘模式 import Originator, Caretaker
import logging


class TerminalCmd(Originator):
    """终端命令"""

    def __init__(self, text=''):
        self.__cmd_name = ''
        self.__cmd_args = []
        self.parse_cmd(text)

    def parse_cmd(self, text):
        """从字符串中解析命令"""
        sub_strs = self.get_arguments_from_string(text, ' ')
        if len(sub_strs) > 0:
            self.__cmd_name = sub_strs[0]
            self.__cmd_args = sub_strs[1:] if len(sub_strs) > 1 else []
            return True
        return False

    def get_arguments_from_string(self, text, split_flag):
        """通过split_flag进行分割，获得参数数组"""
        if split_flag == '':
            logging.warning('split_flag 不能为空!')
            return ''
        data = text.split(split_flag)
        res = []

        for i in data:
            i = i.strip()
            if i != '':
                res.append(i)

        return res

    def show_cmd(self):
        print(self.__cmd_name, self.__cmd_args)


class TerminalCaretaker(Caretaker):
    """终端命令的备忘录管理类"""

    def __init__(self):
        super().__init__()
        self._originator = TerminalCmd.__name__

    def show_history_cmds(self):
        for key, obj in self._mementos.items():
            cmd_name = getattr(obj, f'_{self._originator}__cmd_name', '')
            cmd_args = getattr(obj, f'_{self._originator}__cmd_args', [])
            print(f'{key}: {cmd_name} {cmd_args}')


def test_terminal():
    cmd_idx = 0
    caretaker = TerminalCaretaker()
    cur_cmd = TerminalCmd()

    while True:
        str_cmd = input('请输入指令: ')
        str_cmd = str_cmd.lower()

        if str_cmd.startswith('q'):
            break
        elif str_cmd.startswith('h'):
            caretaker.show_history_cmds()
        elif str_cmd.startswith('!'):
            idx = int(str_cmd[1:])
            try:
                cur_cmd.restore_from_memento(caretaker.get_memento(idx))
                cur_cmd.show_cmd()
            except KeyError:
                print(f'不存在的序号: {idx}')
        else:
            if cur_cmd.parse_cmd(str_cmd):
                cur_cmd.show_cmd()
                caretaker.add_memento(cmd_idx, cur_cmd.create_memento())
                cmd_idx += 1


if __name__ == '__main__':
    test_terminal()
