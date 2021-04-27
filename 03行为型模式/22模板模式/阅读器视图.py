from abc import ABCMeta, abstractmethod


class ReaderView(metaclass=ABCMeta):
    """阅读器视图"""

    def __init__(self):
        self.__page_num = 1

    def get_page(self, page_num):
        self.__page_num = page_num
        return f'第 {page_num} 页的内容'

    def pre_page(self):
        """模板方法，往前翻一页"""
        content = self.get_page(self.__page_num - 1)
        self._display_page(content)

    def next_page(self):
        """模板方法，往后翻一页"""
        content = self.get_page(self.__page_num + 1)
        self._display_page(content)

    @abstractmethod
    def _display_page(self, content):
        """翻页效果"""
        pass


class SmoothView(ReaderView):
    """左右平滑的视图"""

    def _display_page(self, content):
        print(f'左右平滑: {content}')


class SimulationView(ReaderView):
    """仿真翻页的视图"""

    def _display_page(self, content):
        print(f'仿真翻页: {content}')


if __name__ == '__main__':
    smooth_view = SmoothView()
    smooth_view.next_page()
    smooth_view.pre_page()

    simulation_view = SimulationView()
    simulation_view.next_page()
    simulation_view.pre_page()
