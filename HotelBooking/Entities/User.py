from Entities.Location import Location

class User:

    def __init__(self, name: str, email: str, phone: str, location_name: str, pincode: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.location = Location(location_name, pincode)

    def describe(self):
        return f"User(Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Location: {self.location.name}, Pincode: {self.location.pincode})"