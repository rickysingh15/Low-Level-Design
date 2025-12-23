
from vendingMachine import VendingMachine
from inventory import MachineInventory
from ingredientEnum import IngredientType

class VendingMachineManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.inventory = MachineInventory()

    def get_machine(self):
        return VendingMachine(self.inventory)
    
    def add_ingredient(self, name: IngredientType, count: int):
        self.inventory.add_ingredient(name, count)