from uuid import uuid4
from EventCalendar.entities.participant import Participant
from EventCalendar.entities.subject import Subject

class Event(Subject):

    def __init__(self, title: str, day: int, start_time: str, end_time: str, required: int = 0):
        self.title = title
        self.event_id = str(uuid4())
        self.day = day
        self.start_time = self.get_norm_time(day, start_time)
        self.end_time = self.get_norm_time(day, end_time)
        self.participants = []
        self.required = required
        print("Event created with id ", self.event_id, " title ", self.title, " day ", self.day, " start_time ", self.start_time, " end_time ", self.end_time, " required ", self.required)

    def get_norm_time(self, day: int, time_str: str) -> str:        
        day_hrs = day*24
        offset = 0
        if "am" in time_str:
            time = time_str.split("am")[0]
        elif "pm" in time_str: 
            offset = 12
            time = time_str.split("pm")[0]
        else:
            print("Error in normalizing time")
            return -1
        hrs = time.split(":")[0]
        if len(hrs) == 2 and hrs[0] == '0':
            hrs = hrs[1]
        hrs = int(hrs)
        mins = time.split(":")[1]
        if len(mins) == 2 and mins[0] == '0':
            mins = mins[1]
        mins = int(mins)
        return (day_hrs + offset + hrs)*60 + mins

    def notify(self):
        for p in self.participants:
            p.update(self)

    def change_event(self, title: str = None, day: str = None, start_time: str = None, end_time: str = None, required: int = None):
        if title:
            self.title = title
        if day:
            self.day = day
        if start_time:
            self.start_time = start_time
        if end_time:
            self.end_time = end_time
        if required is not None:
            self.required = required
        self.notify()

    def addParticipant(self, participant: Participant) -> bool:
        print("Adding participant ", participant.name)
        if participant.add_event(self):
            self.participants.append(participant)
            return True
        return False

    def removeParticipant(self, participant: Participant):
        for p in self.participants:
            if p.id == participant.id:
                self.participants.remove(p)
                break

    def addMultipleParticipants(self, candidates: list[Participant]):
        for candidate in candidates:
            self.addParticipant(candidate)
        pass
