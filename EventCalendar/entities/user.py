from EventCalendar.entities.event import Event
from EventCalendar.entities.participant import Participant

class User(Participant):

    def __init__(self, name: str, id: int, start_work: str, end_work: str):
        super().__init__(name, id)
        self._events = []
        self._start_work = start_work
        self._end_work = end_work

    @property
    def name(self) -> str:
        return self._name
    @property
    def id(self) -> int:    
        return self._id
    
    @property
    def events(self) -> list[Event]:
        return self._events

    @property
    def start_work(self) -> str:
        return self._start_work
    @property
    def end_work(self) -> str:
        return self._end_work
    
    def update(self, day: int, start_time: str, end_time: str, title: str, required: int = 0) -> bool:
        return True
    
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
    
    def find_event_insert_index(self, event_start, event_end):
        n = len(self._events)
        l = 0
        r = n-1
        mid = int(l+(r-l)/2)
        maxIndex = -1
        maxS = -1
        while l<=r:
            mid = int(l+(r-l)/2)
            if event_start > self._events[mid].start_time:
                if maxS < self._events[mid].start_time:
                    maxS = self._events[mid].start_time
                    maxIndex = mid
                l = mid+1
            else:
                r = mid-1
        return maxIndex
    
    def check_overlap(self, event: Event, new_event_start: int, new_event_end: int):
        if max(event.start_time, new_event_start) < min(event.end_time, new_event_end):
            return True
        return False

    def get_availability(self, event: Event) -> bool:
        print("Checking availability for user ", self.name, " for event ", event.title)
        start = event.start_time
        end = event.end_time
        work_start = self.get_norm_time(event.day, self._start_work)
        work_end = self.get_norm_time(event.day, self._end_work)

        print(self.name, " working hourse are ", work_start, " to ", work_end, " and event time is ", start, " to ", end)
        if max(start, work_start) >= min(end, work_end):
            print("Outside ", self.name , "'s working hours")
            return False

        print("User ", self.name, " is part of events ", self._events)

        n = len(self._events)
        if n == 0:
            print(" participant added with name ", self.name, " with id ", self.id)
            return True
        insert_index = self.find_event_insert_index(start, end)
        if insert_index == -1:
            if self.check_overlap(self._events[0], start, end):
                print("Overlap found")
                return False
        elif insert_index >= 0 and insert_index <= len(self._events)-1:
            if self.check_overlap(self._events[insert_index], start, end) or self.check_overlap(self._events[insert_index+1], start, end):
                print("Overlap found")
                return False
        else:
            if self.check_overlap(self._events[n-1], start, end):
                print("Overlap found")
                return False
            
        print(" participant added with name ", self.name, " with id ", self.id)
        return True
    
    def add_event(self, event: Event) -> bool:
        new_events = []
        n = len(self._events)
        if self.get_availability(event):
            get_insert_index = self.find_event_insert_index(event.start_time, event.end_time)
            i = 0
            while i < n and self._events[i].end_time < event.start_time:
                new_events.append(self._events[i])
                i += 1
            new_events.append(event)
            while i < n:
                new_events.append(self._events[i])
                i += 1
            self._events = new_events
            return True
        return False
       
