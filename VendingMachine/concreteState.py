from state import State
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vendingMachine import VendingMachine

class IdleState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self, value: int):
        print("Select an item first")
        self.machine.balance += value

    def select_number(self, isle_number: int):
        product = self.machine.get_product(isle_number)
        if product and product.count > 0:
            self.machine.selected_product = product
            print("item selected going to state ", SelectItemState)
            self.machine.set_state(SelectItemState(self.machine))
        else:
            print("Invalid selection or Insufficient inventory")

    def dispense_item(self):
        print("please select an item first")
        return None, None


class CoinInsertedState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self, value: int):
        self.machine.balance += value
        if self.machine.balance >= self.machine.selected_product.price:
            print("funds sufficient going to state ", DispensingState)
            self.machine.set_state(DispensingState(self.machine))

    def select_number(self, isle_number: int):
        print("Item already selected")

    def dispense_item(self):
        print("Please insert the required funds")
        return None, None


class SelectItemState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self, value: int):
        self.machine.balance += value
        print("coin inserted going to ", CoinInsertedState)
        self.machine.set_state(CoinInsertedState(self.machine))

    def select_number(self, isle_number: int):
        print("Item already selected")

    def dispense_item(self):
        print("please pay the required funds")
        return None, None


class DispensingState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self, value: int):
        self.machine.balance += value
        print("Item is being dispensed")

    def select_number(self, isle_number: int):
        print("Item is being dispensed, please wait")

    def dispense_item(self):
        print("Dispensing item ", self.machine.selected_product.name)
        change = 0
        self.machine.update_product(self.machine.selected_product.name, dec_count=1)
        change = self.machine.calculate_change()
        print("item dispensed, please collect your change: ", change)
        self.machine.balance = 0
        self.machine.state = IdleState(self.machine)
        return self.machine.selected_product, change