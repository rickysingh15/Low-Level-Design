
from concreteState import IdleState

class AtmMachine:

    def __init__(self):
        self.state = IdleState(self)
        self.card = None

    def insertCard(self, card):
        self.card = card
        self.state.insertCard(card)     

    def pressMaintenanceButton(self):
        self.state.pressMaintenanceButton()      

    def fillInventory(self, cash_dict):
        self.state.filInventory(cash_dict)

    def depositCash(self):
        self.state.depositCash()

    def getCash(self, amount: int):
        return self.state.getCash(amount)

    def checkBalance(self):
        self.state.checkBalance()

    def enterPin(self, pin: str):
        self.state.enterPin(pin)

    def addAccount(self, name: str, pin: str, balance: int = None):
        card = self.account_service.addAccount(name, pin, balance)
        return card