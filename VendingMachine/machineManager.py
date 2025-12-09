
from inventoryService import InventoryService
from vendingMachine import VendingMachineInstance

class MachineManager:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, total_slots: int):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.total_slots = total_slots
            self.inventory_service = InventoryService(self.total_slots)

    def get_vending_machine(self):
        return VendingMachineInstance(self.inventory_service)
