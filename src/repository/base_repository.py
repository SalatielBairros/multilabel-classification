from abc import ABCMeta, abstractmethod

class BaseRepository(metaclass=ABCMeta):
    def __init__(self):
        pass

    # @abstractmethod
    # def save_original_file(self, content) -> None:
    #     ...

    # @abstractmethod
    # def has_saved_questions(self) -> bool:
    #     ...