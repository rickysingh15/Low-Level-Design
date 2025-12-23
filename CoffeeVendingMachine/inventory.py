
import threading
from ingredient import Ingredient
from ingredientEnum import IngredientType
from recipe import Recipe
import copy
class MachineInventory:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.ingredients = {
                IngredientType.MILK.value: None,
                IngredientType.BEANS.value: None,
                IngredientType.SUGAR.value: None,
                IngredientType.WATER.value: None
            }

    def add_ingredient(self, name: IngredientType, count: int):
        ingredient = Ingredient(name, count)
        self.ingredients[name] = ingredient

    def can_fulfill(self, recipe: Recipe):
        print("Check fulfill")
        for ingredient, count in recipe.get_recipe().items():
            ing = self.ingredients.get(ingredient, None)
            if ing and ing.get_count() < count:
                return False
        return True

    def consume_recipe(self, recipe: Recipe):
        with MachineInventory._lock:
            if not self.can_fulfill(recipe):
                print("can't Fulfill")
                return False
            print("can Fulfill")
            for ingredient, count in recipe.get_recipe().items():
                ing = self.ingredients.get(ingredient, None)
                if ing and ing.get_count() >= count:
                    ing.decrement_count(count)
                    self.ingredients[ingredient] = ing
            return True

    def update_count(self, name: IngredientType, count: int):
        ingredient = self.ingredients.get(name, None)
        if ingredient:
            ingredient.update_count(count)
        self.ingredients[name] = ingredient