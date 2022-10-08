import random
import sys
import numpy as np
from map_constants import characters, limits


class SongMap:
    empty_spots = []

    def __init__(self, width, height):
        self.ascii_map = []
        self.width = width
        self.height = height
        self.create_all_empty()

    def create_all_empty(self):
        # self.empty_spots = [[(x, y) for y in range(self.height)] for x in range(self.width)][0]
        for x in range(self.width):
            for y in range(self.height):
                self.empty_spots.append((x, y))

    # create a map of the given size
    def init_rand_map(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(characters["grass"])
            self.ascii_map.append(row)

    def get_empty_spot(self):
        empty_index = random.randint(0, len(self.empty_spots) - 1)
        empty_spot = self.empty_spots.pop(empty_index)
        return empty_spot

    # place the player on the map
    def place_player(self):
        # get a random position
        empty_pos = self.get_empty_spot()
        self.ascii_map[empty_pos[1]][empty_pos[0]] = characters["player"]

    def place_items(self):
        # get a random position
        character_limit = limits["items"]
        for i in range(random.randint(character_limit[0], character_limit[1])):
            empty_pos = self.get_empty_spot()
            self.ascii_map[empty_pos[1]][empty_pos[0]] = characters["item"]

    def place_trainers(self):
        # get a random position
        character_limit = limits["trainers"]
        for i in range(random.randint(character_limit[0], character_limit[1])):
            empty_pos = self.get_empty_spot()
            self.ascii_map[empty_pos[1]][empty_pos[0]] = characters["trainer"]

    def generate_map(self):
        self.init_rand_map()
        self.place_player()
        self.place_items()
        self.place_trainers()

    def print_map(self):
        for row in self.ascii_map:
            print("".join([x[0] for x in row]))
