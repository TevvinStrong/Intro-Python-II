# Write a class to hold player information, e.g. what room they are in
# currently.


# PLAYER CLASS
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        f'{self.name} is in {self.room}'
