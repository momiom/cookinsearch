from abc import ABCMeta, abstractmethod
from const import *
import logging


class Item(metaclass=ABCMeta):
    def __init__(self, values):
         # Flaskのロガーを取得
        self.logger = logging.getLogger('flask.app')
        self.url = values['url']
        self.title = values['title']
        self.img = values['img']
        self.tags = values['tags']


class CookinItem(Item):
    def __init__(self, values):
        super().__init__(values)
        cooking_methods = values['cooking_methods']
        self.cooking_methods = []
        for m in cooking_methods:
            self.cooking_methods.append({
                'name': m,
                'icon': COOKING_METHOD_ICONS.get(m, 'default')
            })
        self.logger.debug(cooking_methods)