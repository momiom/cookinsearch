from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    def __init__(self, values):
        self.url = values['url']
        self.title = values['title']
        self.img = values['img']
        self.tags = values['tags']


class CookinItem(Item):
    def __init__(self, values):
        super().__init__(values)
        self.cooking_methods = values['cooking_methods']
