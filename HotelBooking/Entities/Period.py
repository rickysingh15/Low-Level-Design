

class Period:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def get_duration_in_days(self):
        return self.end - self.start + 1
