from entities.registerService import RegisterService
from entities.loginService import LoginService
from entities.restaurantService import RestaurantService
from entities.user import User

registerService = RegisterService()
loginService = LoginService()
newLoginService = LoginService()
restaurantService = RestaurantService()

if loginService is newLoginService:
    print("same object")

















user1 = registerService.register_user(1, "tushar", "male", "1234567890", "delhi", "110001")
user2 = registerService.register_user(2, "shubham", "male", "1234567890", "delhi", "110003")
user3 = registerService.register_user(3, "vishal", "male", "1234567890", "noida", "201304")
user4 = registerService.register_user(4, "dikesh", "male", "1234567890", "ghaziabad", "201009")

user5 = User.createUser(5, "sahil", "male", "1234567890", "delhi", "110002")

status = loginService.loginUser(2)
print("login status is ", status)

rest1 = registerService.register_restaurant("Athekya", "MasalaDosa", 100, 10, [["noida", "201304"],["delhi", "110001"]] )
rest1.describeRestaurant()

rest2 = registerService.register_restaurant("Galaxy", "Pizza", 250, 5, [["noida", "201304"],["delhi", "110001"],["ghaziabad", "201009"]] )

status = newLoginService.loginUser(4)
rest3 = registerService.register_restaurant("Chayos", "Chai", 50, 15, [["delhi", "110001"],["ghaziabad", "201009"]] )
status = loginService.loginUser(3)
logged_user = newLoginService.getLoggedInUser()
print("logged user is ", logged_user.name)


available_restaurants = restaurantService.getAvailableRestaurants()
print("available restaurants are ", available_restaurants)
for re in available_restaurants:
    re.describeRestaurant()
    print("\n\n")
# print("available restaurants are ", [rest.describeRestaurant() for rest in available_restaurants])

# order1 = restaurantService.orderOnline("Chayos", 10)
# order1.describeOrder()
# order1.rateRestaurant(4, "I liked the tea")

# order2 = restaurantService.orderOnline("Chayos", 3)
# order2.describeOrder()
# order2.rateRestaurant(2, "I did not like the tea")

# order3 = restaurantService.orderOnline("Galaxy", 6)
# order3.describeOrder()
# order3.rateRestaurant(4, "what a fucking pizza")

# rest3.describeRestaurant()
# rest2.describeRestaurant()

