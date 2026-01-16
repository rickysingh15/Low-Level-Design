
from denomination import Denomination
from machine import AtmMachine

machine = AtmMachine()

card_tushar = machine.addAccount("tushar", "1234", 2000)

machine.pressMaintenanceButton()
machine.fillInventory({Denomination.ONETHOUSAND.value: 10,
                        Denomination.FIVEHUNDRED.value: 4,
                        Denomination.ONEHUNDRED.value: 5,
                        Denomination.FIFTY.value: 2})

machine.insertCard(card_tushar)
machine.enterPin("1234")
cash = machine.getCash(500)
print(cash)

machine.insertCard(card_tushar)
machine.enterPin("1234")
cash = machine.getCash(2000)
print(cash)

# machine.insertCard(card_tushar)
# machine.enterPin("1234")
# cash = machine.depositCash(4000)
# print(cash)