
from coffeeBuilder import CoffeeBuilder

class CoffeeDirector:

    def __init__(self, builder: CoffeeBuilder, inventory = None):
        self.builder = builder
        self.inventory = inventory

    def make_coffee(self):
        self.builder.roast_beans()
        self.builder.brew_coffee()
        self.builder.put_milk()
        self.builder.put_suger()
        return self.builder.get_coffee()

    def get_coffee(self):
        return self.make_coffee()


