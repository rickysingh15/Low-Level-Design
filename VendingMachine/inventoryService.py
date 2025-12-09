
import threading
from product import Product

class InventoryService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, total_slots: int):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.products = dict()
            self.total_slots = total_slots
            self.isle_mapping = {i:None for i in range(self.total_slots+1)}

    def get_product_from_isle(self, isle_map_number: int):
        if isle_map_number not in self.isle_mapping:
            print("Incorrect Isle number provided")
            return None
        return self.isle_mapping.get(isle_map_number)

    def create_inventory(self, name: str, inventory_count: int, price: int, isle_map_number: int):
        if isle_map_number > self.total_slots or self.isle_mapping.get(isle_map_number, None) is not None:
            print("Invalid isle mapping number")
            return None
        if price < 0 or inventory_count < 0:
            print("Invalid price")
            return None
        for pid, p in self.products.items():
            if p.name == name:
                print("Product with same name already exists")
                return None
        product = Product(name, inventory_count, price)
        self.isle_mapping[isle_map_number] = product
        if product.id not in self.products:
            self.products[product.id] = product
        return product
    
    def update_inventory(self, product_name: str, inc_count: int = None, dec_count: int = None, new_price: int = None):
        for pid, p in self.products.items():
            if p.name == product_name:
                if inc_count:
                    p.update_count(inc_count,0)
                if dec_count:
                    p.update_count(0,dec_count)
                if new_price:
                    p.update_price(new_price)
                print("updated")
                print(p.name ," , ", p.count, ", ", p.price)
                return True
        return False