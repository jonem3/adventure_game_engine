#!python
from enum import Enum


class Direction(Enum):
    north = 1
    east = 2
    south = 3
    west = 4


class Item:

    def __init__(self, name, description, object_found_in, object_used_in, object_destination):
        self.name = name
        self.description = description
        self.object_found_in = object_found_in
        self.object_used_in = object_used_in
        self.object_destination = object_destination

    def can_use_here(self, place):
        return self.object_used_in == place


class Place:
    def __init__(self, name, description, death=False, won=False):
        self.name = name
        self.description = description
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.items = []
        self.death = death
        self.won = won

    def add_item(self, item):
        self.items.append(item)

    def add_place(self, direction, place):
        if direction.__class__.__name__ != "Direction":
            raise ValueError("You have not passed a direction to the move direction method")

        if place.__class__.__name__ != "Place":
            raise ValueError("You have not passed a Place")

        if direction == Direction.north:
            self.north = place
        elif direction == Direction.east:
            self.east = place
        elif direction == Direction.south:
            self.south = place
        else:
            self.west = place

    def move_direction(self, direction):
        if direction.__class__.__name__ != "Direction":
            raise ValueError("You have not passed a direction to the move direction method")

        new_place = None

        if direction == Direction.north:
            new_place = self.north
        elif direction == Direction.east:
            new_place = self.east
        elif direction == Direction.south:
            new_place = self.south
        else:
            new_place = self.west

        if new_place is None:
            print("You cannot move that way!")
        else:
            print("You have moved "+direction.name)
            return new_place
