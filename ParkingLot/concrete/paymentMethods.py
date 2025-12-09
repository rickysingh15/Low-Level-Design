
from paymentMethod import PaymentMethod

class CreditCard(PaymentMethod):

    def __init__(self):
        pass

    def pay(self, amount: float):
        print("paid using credit card")


class DebitCard(PaymentMethod):

    def __init__(self):
        pass

    def pay(self, amount: float):
        print("paid using debit card")


class UPI(PaymentMethod):

    def __init__(self):
        pass

    def pay(self, amount: float):
        print("paid using upi")


class Cash(PaymentMethod):

    def __init__(self):
        pass

    def pay(self, amount: float):
        print("paid using cash")