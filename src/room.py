# Implement a class to hold room information. This should have name and
# description attributes.


# ROOM CLASS
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Room name is {self.name}, Room description is {self.description}'
