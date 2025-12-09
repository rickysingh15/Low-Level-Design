
from entities.interfaces import Dish


class DalMakhani(Dish):
    def __init__(self):
        self.name = "Dal Makhani"

class PaneerMasala(Dish):
    def __init__(self):
        self.name = "Paneer Masala"


class VegBiryani(Dish):
    def __init__(self):
        self.name = "Veg Biryani"


class ChickenBiryani(Dish):
    def __init__(self):
        self.name = "Chicken Biryani"


class PaneerBiryani(Dish):
    def __init__(self):
        self.name = "Paneer Biryani"

class CholeBhature(Dish):
    def __init__(self):
        self.name = "Chole Bhature"

class speghetti(Dish):
    def __init__(self):
        self.name = "Spaghetti"

class englishBreakfast(Dish):
    def __init__(self):
        self.name = "English Breakfast"

class frenchToast(Dish):
    def __init__(self):
        self.name = "French Toast"

class omelette(Dish):
    def __init__(self):
        self.name = "Omelette"

class pancakes(Dish):
    def __init__(self):
        self.name = "Pancakes"