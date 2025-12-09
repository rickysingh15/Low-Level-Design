from better.foodKartService import FoodKartService

service = FoodKartService()


user1 = service.register_user(1, "tushar", "male", "1234", "delhi", "110001")
user2 = service.register_user(2, "shubham", "male", "7890", "delhi", "110003")
user3 = service.register_user(3, "vishal", "male", "7891", "noida", "201304")
user4 = service.register_user(4, "dikesh", "male", "7390", "ghaziabad", "201009")

user1.describeUser()
user2.describeUser()
user3.describeUser()
user4.describeUser()

service.login_user("1234")

rest1 = service.register_restaurant("Athekya", "MasalaDosa", 100, 10, [["noida", "201304"],["delhi", "110001"]] )
# rest1.describeRestaurant()

service.login_user("7890")
rest2 = service.register_restaurant("Galaxy", "Pizza", 250, 5, [["noida", "201304"],["delhi", "110001"],["ghaziabad", "201009"]] )
# rest2.describeRestaurant()

service.login_user("7390")
rest3 = service.register_restaurant("Chayos", "Chai", 50, 15, [["delhi", "110001"],["ghaziabad", "201009"]] )
# rest3.describeRestaurant()

lis = service.showRestaurants("ratings", "asc")
print("len of lis is ", len(lis))
for restaurant in lis:
    restaurant.describeRestaurant()


order1 = service.orderOnline("Galaxy", 3)
order1.rateOrder(4, "Good food but quantity was less")
order1.describeOrder()

order2 = service.orderOnline("Galaxy", 3)
order2.rateOrder(5, "Excellent!")
order2.describeOrder()

rest2.describeRestaurant()

service.login_user("7890")
service.updateQuantity("Galaxy", 5)


rest2.describeRestaurant()