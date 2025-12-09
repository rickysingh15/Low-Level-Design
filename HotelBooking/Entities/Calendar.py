from Entities.Period import Period

class Calendar:

    def __init__(self, per_day_max_booking: int, capacity_of_room: int, calendar: list[Period] = None):
        self.per_day_max_booking = per_day_max_booking
        self.capacity_of_room = capacity_of_room    
        self.calendar = calendar or []
    
    def insert_slot(self, start: int, end: int):
        self.calendar.append(Period(start, end))


    def get_availability(self, start: int, end: int):
        count_booking = [0]*(end-start+1)
        print("Traversing the periods |------|------|")
        for period in self.calendar:
            print("period is ", period.start, ", ", period.end)
            if period.end < start or period.start > end:
                print("outside the our desired range")
                continue
            else:
                s = max(period.start, start)
                e = min(period.end, end)
                for i in range(s, e+1):
                    count_booking[i-start] += 1

        print("count booking is ", count_booking)
        min_booking = self.per_day_max_booking+100
        for day in count_booking:
            min_booking = min(min_booking, self.per_day_max_booking-day)
            if day >= self.per_day_max_booking:
                return False, min_booking
            
        return True, min_booking

    def book_slot(self, start: int, end: int, no_of_rooms: int):

        status, max_booking = self.get_availability(start, end)
        if max_booking < no_of_rooms:
            print("Not enough rooms available !!!!!!!")
            return False

        self.insert_slot(start, end)
        return True

