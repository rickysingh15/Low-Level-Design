

from machineManager import MachineManager

manager = MachineManager(total_slots=5)
machine = manager.get_vending_machine()
print("machine is ", machine)
machine.create_product("coke", 1, 16, 1)
machine.create_product("juice", 1, 10, 3)
machine.create_product("cake", 5, 12, 2)


machine.insert_coin(5)
machine.select_number(2)
machine.insert_coin(5)
machine.insert_coin(5)


machine1 = manager.get_vending_machine()
print("machine is ", machine1)
machine1.select_number(1)
machine1.insert_coin(5)
machine1.insert_coin(5)
machine1.insert_coin(5)
machine1.insert_coin(2)

# machine.select_number(1)

# machine.update_product(product_name="coke", inc_count=2)