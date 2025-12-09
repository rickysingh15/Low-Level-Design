
from ticket import Ticket
from concrete.paymentMethods import CreditCard, DebitCard, UPI, Cash
class PaymentManager:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.strategy_map = {
                    "credit_card": CreditCard(),
                    "debit_card": DebitCard(),
                    "upi": UPI(),
                    "cash": Cash()
                }

    def generate_receipt(self):
        pass

    def process_payment(self, ticket: Ticket, payment_type: str):
        payment_method = self.strategy_map.get(payment_type.lower(), None)
        if payment_method is None:
            print("Invalid payment method")
        print("Amount to be paid is ", ticket.amount)
        payment_method.pay(ticket.amount)
        return True
        