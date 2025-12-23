
from concreteState import IdleState
from concreteCoffeeFactory import CappuccinoCoffeeFactory, EspressoCoffeeFactory, LatteCoffeeFactory
from concretePayStrategy import UpiStategy, CashStategy, CreditCardStategy, DebitCardStategy
from payEnum import PayType
from inventory import MachineInventory

class VendingMachine:

    def __init__(self, inventory: MachineInventory):
        self.state = IdleState(self)
        self.coffee_factory = None
        self.selected_product = None
        self.inventory = inventory

    def set_factory(self, coffee_factory):
        self.coffee_factory = coffee_factory

    def select_coffee(self, coffee_type: str):
        self.state.select_coffee(coffee_type)

    def pay(self, pay_type: str):
        pay_strategy = None
        if pay_type == PayType.UPI.value:
            pay_strategy = UpiStategy()
        elif pay_type == PayType.CREDIT_CARD.value:
            pay_strategy = CreditCardStategy()
        elif pay_type == PayType.DEBIT_CARD.value:
            pay_strategy = DebitCardStategy()
        elif pay_type == PayType.CASH.value:
            pay_strategy = CashStategy()
        else:
            print("Invalid pay strategy")
            return None
        self.state.pay(pay_strategy)

    def dispense(self):
        return self.state.dispense()