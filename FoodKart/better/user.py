from better.location import Location

class User:

    def __init__(self, id: int, name: str, gender: str, phone: str, location: Location):
        self.id = id
        self.name = name
        self.gender = gender
        self.phone = phone
        self.location = location

    def describeUser(self):
        print(f"User ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Phone: {self.phone}")
        print(f"Location: {self.location.name}, {self.location.pincode}")
        print("\n")
