class TodoList:
    """待办清单"""

    def __init__(self):
        self.__work_items = []

    def write_work_item(self, item):
        self.__work_items.append(item)

    def get_work_items(self):
        return self.__work_items


class TodoListCaretaker:
    """ToDoList管理类"""

    def __init__(self):
        self.__todo_list = None

    def set_todo_list(self, todo_list):
        self.__todo_list = todo_list

    def get_todo_list(self):
        return self.__todo_list


class Engineer:
    """工程师"""

    def __init__(self, name):
        self.__name = name
        self.__work_items = []

    def add_work_item(self, item):
        self.__work_items.append(item)

    def forget(self):
        self.__work_items.clear()
        print(f'{self.__name} 工作太忙了，都忘记要做什么了!')

    def write_todo_list(self):
        """将工作项记录到TodoList"""
        todo_list = TodoList()
        for item in self.__work_items:
            todo_list.write_work_item(item)
        return todo_list

    def retrospect(self, todo_list):
        """回忆工作项"""
        self.__work_items = todo_list.get_work_items()
        print(f'{self.__name} 想起要做什么了!')

    def show_work_item(self):
        if len(self.__work_items):
            print(f'{self.__name} 的工作项:')
            for i in range(len(self.__work_items)):
                print(f'{i + 1}. {self.__work_items[i]};')
        else:
            print(f'{self.__name} 暂无工作项!')


if __name__ == '__main__':
    tony = Engineer('Tony')
    tony.add_work_item('解决线上部分用户因昵称太长而无法显示全的问题')
    tony.add_work_item('完成PDF的解析')
    tony.add_work_item('在阅读器中显示PDF第一页的内容')
    tony.show_work_item()

    caretaker = TodoListCaretaker()
    caretaker.set_todo_list(tony.write_todo_list())
    print()

    tony.forget()
    tony.show_work_item()
    print()

    tony.retrospect(caretaker.get_todo_list())
    tony.show_work_item()
