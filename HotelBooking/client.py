from Entities.BookingPlatform import BookingPlatform

platform1 = BookingPlatform()


user1 = platform1.register_user("tushar", "abc", "1234", "Noida", "201304")
platform1.login_user("1234")

platform1.register_hotel("Hilton", "Noida", "201304")

platform1.add_room_to_hotel("Hilton", "single", 5, 5000, 2)
# platform1.add_room_to_hotel("Hilton", "double", 5, 8000, 4)
# # platform.add_room_to_hotel("Hilton", "suite", 2, 15000, 6)


platform2 = BookingPlatform()
user2 = platform2.register_user("Alice", "dbc", "1421", "Delhi", "110001")

platform2.login_user("1421")

platform2.register_hotel("Hill_View", "Delhi", "110001")
platform2.add_room_to_hotel("Hill_View", "single", 10, 2000, 2)



print("Checking availability -----------------------------------")
hotels1 = platform1.get_available_hotels(1, 5, 2, "Delhi", "110001")
for hotel_name, hotel in hotels1.items():
    print(hotel.describe_hotel())


platform3 = BookingPlatform()
user3 = platform3.register_user("Frankie", "obc", "1481", "Mumbai", "411001")
platform3.login_user("1481")

platform3.register_hotel("Sea_View", "Mumbai", "411001")
platform3.add_room_to_hotel("Sea_View", "double", 4, 3400, 4)



platform3.register_hotel("BeachPort", "Mumbai", "411001")
platform3.add_room_to_hotel("BeachPort", "single", 2, 2500, 2)
platform3.add_room_to_hotel("BeachPort", "suite", 1, 7500, 4)

print("Checking availability -----------------------------------")
hotels3 = platform3.get_available_hotels(6, 10, 3, "Mumbai", "411001")
for hotel_name, hotel in hotels3.items():
    print(hotel.describe_hotel())


rooms = platform3.get_available_rooms("BeachPort", 6, 10)
print(rooms)
booking3 = platform3.book_hotel("BeachPort", "single", 6, 10, 2)
print(booking3.describe_booking())


booking4 = platform3.book_hotel("BeachPort", "single", 11, 15, 2)
print(booking4.describe_booking())


booking5 = platform3.book_hotel("BeachPort", "single", 11, 13, 2)
print(booking5.describe_booking())


booking6 = platform3.book_hotel("BeachPort", "single", 11, 13, 2)
print(booking6.describe_booking())