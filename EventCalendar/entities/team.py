from EventCalendar.entities.user import User
from EventCalendar.entities.participant import Participant
from EventCalendar.entities.event import Event
from EventCalendar.entities.subject import Subject
import copy

class Team(Participant):

    def __init__(self, name: str, id: int, members: list[User] = None):
        super().__init__(name, id)
        self._members = members or []

    def add_member(self, user: User):
        self._members.append(user)

    def update(self, day: int, start_time: str, end_time: str, title: str, required: int = 0) -> bool:
        return True

    def get_availability(self,  event: Event) -> bool:
        print("Checking availability for team ", self.name)
        required = copy.deepcopy(event.required)
        for p in self._members:
            if p.get_availability(event):
                required -= 1
                if required == 0:
                    return True
        return False
    
    def add_event(self, event: Event) -> bool:
        required = copy.deepcopy(event.required)
        if self.get_availability(event):
            for p in self._members:
                if p.add_event(event):
                    required -= 1
                    if required == 0:
                        break
            return True
        return False