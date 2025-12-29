
from abc import ABC, abstractmethod
from task import Task

class SortStrategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def sort(self, tasks: list[Task]):
        pass


class PrioritySortStrategy(SortStrategy):

    def __init__(self):
        pass

    def sort(self, tasks: list[Task]):
        pass
    


class DueDateSortStrategy(SortStrategy):

    def __init__(self):
        pass

    def sort(self, tasks: list[Task]):
        pass