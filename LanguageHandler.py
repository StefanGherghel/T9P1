import abc
from abc import ABC


class LanguageHandler(ABC):

    exec: str

    def __init__(self, succesor=None):
        self.__succesor = succesor

    @abc.abstractmethod
    def handle_it(self, file: str):
        pass
