from abc import ABC, abstractmethod

class Participant(ABC):

    def __init__(self, name: str, id: int):
        self._name = name
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> int:
        return self._id
    

    @abstractmethod
    def get_availability(self):
        pass

    @abstractmethod
    def update(self, day: int, start_time: str, end_time: str, title: str, required: int = 0) -> bool:
        pass