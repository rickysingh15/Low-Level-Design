
from machineState import MachineState
from coffeeEnum import CoffeeType
from concreteCoffeeFactory import CappuccinoCoffeeFactory, EspressoCoffeeFactory, LatteCoffeeFactory
from payStrategy import PayStrategy

class IdleState(MachineState):

    def __init__(self, machine, factory = None):
        self.coffee_machine = machine
        self.coffee_factory = factory

    def select_coffee(self, coffee_type: str):
        if coffee_type == CoffeeType.ESPRESSO.value:
            self.coffee_factory = EspressoCoffeeFactory(self.coffee_machine.inventory)
        elif coffee_type == CoffeeType.CAPPUCCINO.value:
            self.coffee_factory = CappuccinoCoffeeFactory(self.coffee_machine.inventory)
        elif coffee_type == CoffeeType.LATTE.value:
            self.coffee_factory = LatteCoffeeFactory(self.coffee_machine.inventory)
        else:
            print("Invalid Coffee type")
            return None
        coffee = self.coffee_factory.prepare()
        if coffee:
            self.coffee_machine.selected_product = coffee    
            print("Machine state change from Idle -------> CoffeeSelectedState")
            self.coffee_machine.state = CoffeeSelectedState(self.coffee_machine, self.coffee_factory)

    def pay(self, pay_strategy: PayStrategy):
        print("Please select a coffee")

    def dispense(self):
        print("Please select a coffee")


class CoffeeSelectedState(MachineState):

    def __init__(self, machine, factory = None):
        self.coffee_machine = machine
        self.coffee_factory = factory

    def select_coffee(self, coffee_type: str):
        print("Wait for coffee to dispense")

    def pay(self, pay_strategy: PayStrategy):
        pay_strategy.pay(self.coffee_machine.selected_product.price)
        print("Machine state change from CoffeeSelectedState -------> Dispense")
        self.coffee_machine.state = DispenseState(self.coffee_machine, self.coffee_factory)
       

    def dispense(self):
        pass


class DispenseState(MachineState):

    def __init__(self, machine, factory = None):
        self.coffee_machine = machine
        self.coffee_factory = factory

    def select_coffee(self, coffee_type: str):
        print("Wait for coffee to dispense")

    def pay(self, pay_strategy: PayStrategy):
        print("Wait for coffee to dispense")

    def dispense(self):
        print("Machine state change from Dispense -------> Idle")
        self.coffee_machine.state = IdleState(self.coffee_machine)
        return self.coffee_machine.selected_product