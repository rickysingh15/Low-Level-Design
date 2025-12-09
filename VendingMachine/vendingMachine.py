
import threading
from inventoryService import InventoryService
from state import State
from concreteState import IdleState, DispensingState

class VendingMachineInstance:

    def __init__(self, inventory_service: InventoryService):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.balance = 0
            self.inventory_service = inventory_service
            self.state = IdleState(self)
            self.selected_product = None

    def update_product(self, product_name: str, inc_count: int = None, dec_count: int = None, price: int = None):
        return self.inventory_service.update_inventory(product_name, inc_count, dec_count, price)

    def get_inventory(self):
        return self.inventory_service

    def create_product(self, name: str, inventory_count: int, price: int, isle_map_number: int):
        return self.inventory_service.create_inventory(name, inventory_count, price, isle_map_number)

    def get_product(self, isle_map_number: int):
        return self.inventory_service.get_product_from_isle(isle_map_number)

    def set_state(self, state: State):
        self.state = state

    def insert_coin(self, value: int):
        self.state.insert_coin(value)
        if isinstance(self.state, DispensingState):
            self.dispense_item()

    def calculate_change(self):
        return -1*(self.selected_product.price - self.balance)

    def select_number(self, isle_number: int):
        self.state.select_number(isle_number)

    def dispense_item(self):
        return self.state.dispense_item()