from abc import ABC, abstractmethod

class PricingStrategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def calculate_price(self):
        pass

class SimplePricingStrategy(PricingStrategy):
    def calculate_price(self, ticket):
        total_time_in_mins = (ticket.exit_time - ticket.issue_time).total_seconds() // 60 
        print("total time in mins is ", total_time_in_mins)
        ticket.amount = float(ticket.spot.rate) * total_time_in_mins
        return ticket.amount


class HourlyPricingStrategy(PricingStrategy):
    def calculate_price(self, ticket):
        total_time_in_mins = (ticket.exit_time - ticket.issue_time).total_seconds() // 60 * 60
        print("total time in mins is ", total_time_in_mins)
        ticket.amount = float(ticket.spot.rate) * total_time_in_mins
        return ticket.amount