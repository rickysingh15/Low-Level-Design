
from payStrategy import PayStrategy

class UpiStategy(PayStrategy):

    def __init__(self):
        pass

    def pay(self, amount: int):
        print("Paid amount ", amount, " using upi")

class CreditCardStategy(PayStrategy):

    def __init__(self):
        pass

    def pay(self, amount: int):
        print("Paid amount ", amount, " using credit card")

class DebitCardStategy(PayStrategy):

    def __init__(self):
        pass

    def pay(self, amount: int):
        print("Paid amount ", amount, " using debit card")

class CashStategy(PayStrategy):

    def __init__(self):
        pass

    def pay(self, amount: int):
        print("Paid amount ", amount, " using cash")