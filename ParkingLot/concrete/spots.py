from spot import Spot

class Compact(Spot):
    def __init__(self, rate_per_min: int):
        super().__init__(rate_per_min)

    def is_empty(self):
        return self.vehicle is None


class Regular(Spot):
    def __init__(self, rate_per_min: int):
        super().__init__(rate_per_min)

    def is_empty(self):
        return self.vehicle is None

class Oversize(Spot):
    def __init__(self, rate_per_min: int):
        super().__init__(rate_per_min)

    def is_empty(self):
        return self.vehicle is None