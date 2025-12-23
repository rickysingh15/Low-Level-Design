
from coffee import Coffee
from coffeeFactory import CoffeeFactory
from concreteCoffee import EspressoCoffee, CappuccinoCoffee, LatteCoffee
from inventory import MachineInventory
from recipe import Recipe
from ingredientEnum import IngredientType

class EspressoCoffeeFactory(CoffeeFactory):

    def __init__(self, inventory: MachineInventory, ):
        self.inventory = inventory
        self.recipe = Recipe()
        self.recipe.add_ingredient(IngredientType.MILK.value, 1)
        self.recipe.add_ingredient(IngredientType.SUGAR.value, 2)
        self.recipe.add_ingredient(IngredientType.BEANS.value, 4)
        self.coffee = EspressoCoffee(self.recipe)

    def prepare(self) -> Coffee:
        if self.inventory.consume_recipe(self.coffee.get_recipe()):
            print("Can consume")
            return self.coffee
        print("Insufficient resources")
        return None


class CappuccinoCoffeeFactory(CoffeeFactory):

    def __init__(self, inventory: MachineInventory):
        self.inventory = inventory
        self.recipe = Recipe()
        self.recipe.add_ingredient(IngredientType.MILK.value, 3)
        self.recipe.add_ingredient(IngredientType.SUGAR.value, 2)
        self.recipe.add_ingredient(IngredientType.BEANS.value, 1)
        self.coffee = CappuccinoCoffee(self.recipe)

    def prepare(self) -> Coffee:
        if self.inventory.consume_recipe(self.coffee.get_recipe()):
            print("Can consume")
            return self.coffee
        print("Insufficient resources")
        return None



class LatteCoffeeFactory(CoffeeFactory):

    def __init__(self, inventory: MachineInventory):
        self.inventory = inventory
        self.recipe = Recipe()
        self.recipe.add_ingredient(IngredientType.MILK.value, 3)
        self.recipe.add_ingredient(IngredientType.SUGAR.value, 1)
        self.recipe.add_ingredient(IngredientType.BEANS.value, 2)
        self.coffee = LatteCoffee(self.recipe)

    def prepare(self) -> Coffee:
        if self.inventory.consume_recipe(self.coffee.get_recipe()):
            print("Can consume")
            return self.coffee
        print("Insufficient resources")
        return None
