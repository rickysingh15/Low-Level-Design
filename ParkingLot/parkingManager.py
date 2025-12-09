from paymentManager import PaymentManager
from spotManager import SpotManager
from spot import Spot
from ticket import Ticket
from vehicle import Vehicle
from pricingStrategy import SimplePricingStrategy, HourlyPricingStrategy

class ParkingManager:
    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.pricing_strategy = SimplePricingStrategy()

    def create_ticket(self, vehicle: Vehicle, spot: Spot) -> Ticket:
        ticket = Ticket(vehicle, spot)
        return ticket

    def process_ticket(self, ticket: Ticket) -> Ticket:
        ticket.process()
        self.pricing_strategy.calculate_price(ticket)
        return ticket