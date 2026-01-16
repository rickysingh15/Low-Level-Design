
from user import User
from uuid import uuid4
from card import Card

class Account:

    def __init__(self, user: User, card: Card, pin: str, balance: int):
        self._id = str(uuid4())
        self._user = user
        self._card = card
        self._pin = pin
        self._balance = balance

    @property
    def get_id(self):
        return self._id
    
    @property
    def get_user(self):
        return self._user
    
    @property
    def get_card(self):
        return self._card
    
    @property
    def get_pin(self):
        return self._pin
    
    @property
    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount: int):
        self._balance = amount
    