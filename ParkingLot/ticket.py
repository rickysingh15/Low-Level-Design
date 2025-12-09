
from uuid import uuid4
from datetime import datetime, timedelta
from vehicle import Vehicle
from spot import Spot

class Ticket:

    def __init__(self, vehicle: Vehicle, spot: Spot):
        self.id = str(uuid4())
        self.issue_time = datetime.utcnow()
        self.exit_time = None
        self.spot = spot
        self.vehicle = vehicle
        self.amount = None

    def process(self):
        self.exit_time = self.issue_time + timedelta(minutes=45)


    def print_ticket(self):
        print("id -> ", self.id, "\n")
        print("issue time -> ", self.issue_time, "\n")
        print("exit time -> ", self.exit_time, "\n")
        self.spot.describe()
        self.vehicle.describe()

