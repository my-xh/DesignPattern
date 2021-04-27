from abc import ABCMeta, abstractmethod


class Filter(metaclass=ABCMeta):
    """过滤器"""

    @abstractmethod
    def do_filter(self, elements):
        pass


class FilterChain(Filter):
    """过滤器链"""

    def __init__(self):
        self.__filters = []

    def add_filter(self, filter):
        self.__filters.append(filter)

    def remove_filter(self, filter):
        self.__filters.remove(filter)

    def do_filter(self, elements):
        for _filter in self.__filters:
            elements = _filter.do_filter(elements)
        return elements


class FilterScreen(Filter):
    """过滤网"""

    def do_filter(self, elements):
        n = len(elements)
        for i in range(n):
            idx = n - 1 - i
            material = elements[idx]
            if material == '豆渣':
                elements.pop(idx)
        return elements


if __name__ == '__main__':
    raw_materials = ['豆渣', '豆浆']
    print(f'过滤前: {raw_materials}')
    filter_screen = FilterScreen()
    filtered_material = filter_screen.do_filter(raw_materials)
    print(f'过滤后: {filtered_material}')
