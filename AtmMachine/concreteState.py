
from transactionType import TransactionType
from denomination import Denomination
from state import State
from card import Card
class IdleState(State):

    def __init__(self, machine):
        self.machine = machine

    def insertCard(self, card: Card):
        print("State changed to --> CardInsertedState")
        self.machine.state = CardInsertedState(self.machine)
        return
    
    def filInventory(self, cash_dict):
        print("Enter maintenance mode")

    def pressMaintenanceButton(self):
        self.machine.state = MaintenanceState(self.machine)

    def enterPin(self, pin: str):
        print("Please insert card first")

    def depositCash(self, cash_dict: dict):
        print("Not authenticated")

    def getCash(self, amount: int):
        print("Not authenticated")

    def checkBalance(self):
        print("Not authenticated")


class CardInsertedState(State):

    def __init__(self, machine):
        self.machine = machine

    def insertCard(self, card: Card):
        print("Card already inserted")

    def pressMaintenanceButton(self):
        pass

    def filInventory(self, cash_dict):
        print("Enter maintenance mode")

    def enterPin(self, pin: str):
        if self.machine.auth_service.authenticateUser(self.machine.card, pin):
            print("Authentication passed")
            print("State changed to --> AuthenticatedState")
            self.machine.state = AuthenticatedState(self.machine)
        else:
            print("Authentication failed")
            print("State changed to --> IdleState")
            self.machine.state = IdleState(self.machine)


    def depositCash(self, cash_dict: dict):
        print("Not authenticated")

    def getCash(self, amount: int):
        print("Not authenticated")

    def checkBalance(self):
        print("Not authenticated")



class AuthenticatedState(State):

    def __init__(self, machine):
        self.machine = machine

    def insertCard(self, card: Card):
        print("Card already inserted")

    def pressMaintenanceButton(self):
        pass

    def filInventory(self, cash_dict):
        print("Enter maintenance mode")
        
    def enterPin(self, pin: str):
        print("Already authenticated")

    def depositCash(self, cash_dict: dict):
        self.machine.inventory_service.depositCash(cash_dict)
        print("State changed to --> IdleState")
        self.machine.state = IdleState(self.machine)

    def getCash(self, amount: int):
        cash = None
        account = self.machine.account_service.getAccount(self.machine.card)
        if account.get_balance < amount:
            print("Insufficient balance in account")
            self.machine.state = IdleState(self.machine)
            return None
        cash = self.machine.inventory_service.fetchAmount(amount)
        if cash is not None:
            print("State changed to --> IdleState")
        self.machine.state = IdleState(self.machine)
        return cash

    def checkBalance(self):
        balance = self.machine.account_service.getBalance(self.machine.card)
        print("State changed to --> IdleState")
        self.machine.state = IdleState(self.machine)
        return balance
        


class MaintenanceState(State):

    def __init__(self, machine):
        self.machine = machine

    def filInventory(self, cash_dict):
        self.machine.inventory_service.depositCash(cash_dict)
        self.machine.state = IdleState(self.machine)

    def insertCard(self):
        print("Maintenance mode")

    def pressMaintenanceButton(self):
        print("Maintenance mode")

    def enterPin(self, pin: str):
        print("Maintenance mode")

    def depositCash(self, cash_dict: dict):
        print("Maintenance mode")

    def getCash(self, amount: int):
        print("Maintenance mode")

    def checkBalance(self):
        print("Maintenance mode")