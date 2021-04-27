from 过滤器模式 import Filter, FilterChain
import re


class SensitiveFilter(Filter):
    """敏感词过滤"""

    def __init__(self):
        self.__sensitive = ['黄色', '反动', '贪污']

    def do_filter(self, elements):
        new_elements = []
        regex = '|'.join(self.__sensitive)

        for element in elements:
            item, _ = re.subn(regex, '', element)
            new_elements.append(item)

        return new_elements


class HtmlFilter(Filter):
    """HTML特殊字符转换"""

    def __init__(self):
        self.__word_map = {
            '&': '&amp;',
            "'": ' &apos;',
            '>': '&gt;',
            '<': '&lt;',
            '"': ' &quot;',
        }

    def do_filter(self, elements):
        new_elements = []
        regex = '|'.join(self.__word_map.keys())

        for element in elements:
            item, _ = re.subn(regex, lambda match: self.__word_map[
                              match.group()], element)
            new_elements.append(item)

        return new_elements


if __name__ == '__main__':
    contents = [
        '有人出售黄色书: <黄情味道>',
        '有人企图搞反动活动, ——"造谣资讯"',
    ]
    print(f'过滤前: {contents}')
    filter_chain = FilterChain()
    filter_chain.add_filter(SensitiveFilter())
    filter_chain.add_filter(HtmlFilter())
    new_contents = filter_chain.do_filter(contents)
    print(f'过滤后: {new_contents}')
