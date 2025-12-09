from abc import ABC, abstractmethod
from EventCalendar.entities.participant import Participant

class Subject(ABC):

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def addParticipant(self, participant: Participant):
        pass

    @abstractmethod
    def removeParticipant(self, participant: Participant):
        pass
