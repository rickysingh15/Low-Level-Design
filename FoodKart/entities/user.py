from entities.location import Location

class User:

    def __init__(self, id: int, name: str, gender: str, phone: str, location: Location):
        self.id = id
        self.name = name
        self.gender = gender
        self.phone = phone
        self.location = location

    @staticmethod
    def createUser(id, name, gender, phone, location_name, pincode):
        location = Location(location_name, pincode)
        user = User(id, name, gender, phone, location)
        return user