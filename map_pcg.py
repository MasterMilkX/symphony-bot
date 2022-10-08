import random
import sys
import numpy as np
from map_constants import CHARACTERS, LIMITS, PROBABILITIES, CARDINALS


class SongMap:
    empty_spots = []

    def __init__(self, width, height):
        self.ascii_map = []
        self.width = width
        self.height = height
        self.create_all_empty()

    # create a list of all empty spots on the map
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
                row.append(CHARACTERS["grass"])
            self.ascii_map.append(row)

    # get a random empty spot on the map
    def get_empty_spot(self):
        empty_index = random.randint(0, len(self.empty_spots) - 1)
        empty_spot = self.empty_spots.pop(empty_index)
        return empty_spot

    # place the player on the map
    def place_player(self):
        # get a random position
        empty_pos = self.get_empty_spot()
        self.ascii_map[empty_pos[1]][empty_pos[0]] = CHARACTERS["player"]

    # place a random number of items on the map
    def place_items(self):
        # get a random position
        character_limit = LIMITS["items"]
        for i in range(random.randint(character_limit[0], character_limit[1])):
            empty_pos = self.get_empty_spot()
            self.ascii_map[empty_pos[1]][empty_pos[0]] = CHARACTERS["item"]

    #place a random number of trainers on the map
    def place_trainers(self):
        # get a random position
        character_limit = LIMITS["trainers"]
        for i in range(random.randint(character_limit[0], character_limit[1])):
            empty_pos = self.get_empty_spot()
            self.ascii_map[empty_pos[1]][empty_pos[0]] = CHARACTERS["trainer"]

    #place a random number of trees on the map
    def place_trees(self):
        rand_tree_prob = random.uniform(LIMITS["trees"][0], LIMITS["trees"][1])
        
        # get a random position
        for i in self.empty_spots:
            if random.random() < rand_tree_prob:
                self.empty_spots.remove(i)
                self.ascii_map[i[1]][i[0]] = CHARACTERS["tree"]

                
    #place a random wild grass patches on the map
    def place_wild_grass(self):
        # get a random position
        for i in self.empty_spots:
            #randomly place wild grass based on the probability
            if random.random() < PROBABILITIES["wild_grass"]["spawn"]:
                self.ascii_map[i[1]][i[0]] = CHARACTERS["wild_grass"]
                self.empty_spots.remove(i)
                grown = self.grow_grass(i[0],i[1])

                # remove the spot if it didn't grow
                if not grown:
                    self.ascii_map[i[1]][i[0]] = CHARACTERS["grass"]
                    self.empty_spots.append(i)
                    
        
    #grows a wild grass spot with the cardinal directions based on the probability
    def grow_grass(self,x,y):
        growth = False
        for c in CARDINALS:
            print
            x2 = x + c[0]
            y2 = y + c[1]
            if ((x2,y2) in self.empty_spots) and (random.random() < PROBABILITIES["wild_grass"]["grow"]):
                growth = True
                self.empty_spots.remove((x2,y2))
                self.ascii_map[y2][x2] = CHARACTERS["wild_grass"]
                self.grow_grass(x2,y2)
        return growth

    #populate the map with the player, items, and trainers
    def generate_map(self):
        self.init_rand_map()
        self.place_player()
        self.place_items()
        self.place_trainers()
        self.place_trees()
        self.place_wild_grass()

    # print the map to the console
    def print_map(self):
        for row in self.ascii_map:
            print("".join([x[0] for x in row]))
