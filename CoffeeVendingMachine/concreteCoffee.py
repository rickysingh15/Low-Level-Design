
from coffee import Coffee
from coffeeEnum import CoffeeType
from ingredientEnum import IngredientType
from recipe import Recipe

class EspressoCoffee(Coffee):

    def __init__(self, recipe: Recipe = None):
        super().__init__()
        self.coffee_name = CoffeeType.ESPRESSO.value
        self.recipe = recipe
        self.price = 250

    def get_recipe(self):
        return self.recipe


class CappuccinoCoffee(Coffee):

    def __init__(self, recipe: Recipe = None):
        super().__init__()
        self.coffee_name = CoffeeType.CAPPUCCINO.value
        self.recipe = recipe
        self.price = 100

    def get_recipe(self):
        return self.recipe

class LatteCoffee(Coffee):

    def __init__(self, recipe: Recipe = None):
        super().__init__()
        self.coffee_name = CoffeeType.LATTE.value
        self.recipe = recipe
        self.price = 275

    def get_recipe(self):
        return self.recipe