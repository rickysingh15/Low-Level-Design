from machineManager import VendingMachineManager
from coffeeEnum import CoffeeType
from payEnum import PayType
from ingredientEnum import IngredientType

manager = VendingMachineManager()
manager.add_ingredient(IngredientType.MILK.value, 5)
manager.add_ingredient(IngredientType.SUGAR.value, 5)
manager.add_ingredient(IngredientType.BEANS.value, 4)
machine = manager.get_machine()

machine.select_coffee(CoffeeType.CAPPUCCINO.value)
machine.pay(PayType.UPI.value)
coffee1 = machine.dispense()

print(coffee1)

machine.select_coffee(CoffeeType.ESPRESSO.value)
machine.pay(PayType.UPI.value)
coffee2 = machine.dispense()

print(coffee2)
