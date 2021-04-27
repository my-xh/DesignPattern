from abc import ABCMeta, abstractmethod


class Label:

    def __init__(self, name, text='', **attrs):
        self.__name = name
        self.__text = text
        self.__attrs = attrs
        self.__components = []

    @property
    def name(self):
        return self.__name

    @property
    def text(self):
        return self.__text

    @property
    def attrs(self):
        return self.__attrs

    def add_component(self, component):
        if isinstance(component, Label):
            self.__components.append(component)

    def element(self, indent=''):
        attrs = ' '.join(f'{k}="{v}"' for k, v in self.attrs.items())
        if attrs:
            attrs = ' ' + attrs
        e_begin = f'{indent}<{self.name}{attrs}>'

        e_content = self.text
        if self.__components:
            for component in self.__components:
                e_content += '\n'
                e_content += component.element(indent + '\t')
            e_end = f'\n{indent}</{self.name}>'
        else:
            e_end = f'</{self.name}>'

        return e_begin + e_content + e_end


class LabelBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_label(self):
        pass


class BookBuilder(LabelBuilder):

    def build_label(self):
        book = Label('book', id='book1')
        book.add_component(Label('title', 'Design Pattern'))
        book.add_component(Label('author', 'Tony'))
        book.add_component(
            Label('description', 'How to comprehend Design Patterns from daily life.'))
        return book


class OutlineBuilder(LabelBuilder):

    def build_label(self):
        outline = Label('outline')
        chapter = Label('chapter')
        section = Label('section')
        keywords = Label('keywords')
        keywords.add_component(Label('keyword', 'design pattern'))
        keywords.add_component(Label('keyword', 'daily life'))
        section.add_component(Label('title', 'section 1'))
        section.add_component(keywords)
        chapter.add_component(Label('title', 'Chapter 1'))
        chapter.add_component(section)
        outline.add_component(chapter)
        return outline


if __name__ == '__main__':
    book_builder = BookBuilder()
    book = book_builder.build_label()
    print(book.element())
    print()

    outline_builder = OutlineBuilder()
    outline = outline_builder.build_label()
    print(outline.element())
