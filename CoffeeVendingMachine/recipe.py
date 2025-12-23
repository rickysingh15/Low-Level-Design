
from ingredientEnum import IngredientType
class Recipe:

    def __init__(self):
        self.recipe = dict()

    def add_ingredient(self, ingredient: IngredientType, amount: int):
        self.recipe[ingredient] = amount

    def get_recipe(self):
        return self.recipe
