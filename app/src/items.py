from abc import ABCMeta, abstractmethod


class Items(metaclass=ABCMeta):
    def __init__(self):
        pass


class CookinItem(Items):
    def __init__(self):
        super().__init__()
