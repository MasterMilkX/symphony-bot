from audioop import cross
import random
from re import L
import sys
import numpy as np
from map_constants import CHARACTERS, LIMITS, PROBABILITIES, CARDINALS
from BFS import can_reach_points


class GameMap:
    empty_spots = []

    def __init__(self, width, height):
        self.ascii_map = []
        self.width = width
        self.height = height
        self.create_all_empty()

    # create a list of all empty spots on the map
    def create_all_empty(self):
        for x in range(self.width):
            for y in range(self.height):
                self.empty_spots.append((x, y))

    # create a map of the given size
    def init_rand_map(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(CHARACTERS["path"])
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

    # place a random number of trainers on the map
    def place_trainers(self):
        # get a random position
        character_limit = LIMITS["trainers"]
        for i in range(random.randint(character_limit[0], character_limit[1])):
            empty_pos = self.get_empty_spot()
            self.ascii_map[empty_pos[1]][empty_pos[0]] = CHARACTERS["trainer"]

    # add a town to the map
    def construct_town(self):
        random_w = random.randint(LIMITS["town"][0], LIMITS["town"][1])
        random_h = random.randint(LIMITS["town"][0], LIMITS["town"][1])

        boundaries_x = random.randint(0-random_w, self.width)
        boundaries_y = random.randint(0-random_h, self.height)

        for i in range(random_w):
            for j in range(random_h):
                town_x = boundaries_x + i
                town_y = boundaries_y + j
                if (town_x, town_y) in self.empty_spots:
                    self.ascii_map[town_y][town_x] = CHARACTERS["town"]
                    self.empty_spots.remove((town_x, town_y))

    # place a random number of trees on the map
    def place_trees(self):
        rand_tree_prob = random.uniform(LIMITS["trees"][0], LIMITS["trees"][1])

        # get a random position
        for i in self.empty_spots:
            if random.random() < rand_tree_prob:
                self.empty_spots.remove(i)
                self.ascii_map[i[1]][i[0]] = CHARACTERS["tree"]

    # place a random wild grass patches on the map
    def place_wild_grass(self):
        # get a random position
        for i in self.empty_spots:
            # randomly place wild grass based on the probability
            if random.random() < PROBABILITIES["wild_grass"]["spawn"]:
                self.ascii_map[i[1]][i[0]] = CHARACTERS["wild_grass"]
                self.empty_spots.remove(i)
                grown = self.grow_grass(i[0], i[1])

                # remove the spot if it didn't grow
                if not grown:
                    self.ascii_map[i[1]][i[0]] = CHARACTERS["grass"]
                    self.empty_spots.append(i)

    # grows a wild grass spot with the cardinal directions based on the probability
    def grow_grass(self, x, y):
        growth = False
        for c in CARDINALS:
            x2 = x + c[0]
            y2 = y + c[1]
            if ((x2, y2) in self.empty_spots) and (random.random() < PROBABILITIES["wild_grass"]["grow"]):
                growth = True
                self.empty_spots.remove((x2, y2))
                self.ascii_map[y2][x2] = CHARACTERS["wild_grass"]
                self.grow_grass(x2, y2)
        return growth

    # populate the map with the player, items, and trainers
    def generate_map(self):
        self.init_rand_map()
        self.drawPath()
        # self.construct_town()
        # self.place_player()
        # self.place_items()
        # self.place_trainers()
        # self.place_trees()
        # self.place_wild_grass()

    # make a path on the map
    def drawPath(self):
        #pick some random points on the edge of the map
        crosspoints = []
        for i in range(LIMITS["path"][0],LIMITS["path"][1]):
            side = "x" if random.random() < 0.5 else "y"
            if side == "x":
                point = ((random.randint(0,self.width-1),0) if random.random() < 0.5 else (random.randint(0,self.width-1),self.height-1)) 
                crosspoints.append(point)
            else:
                point = ((0,random.randint(0,self.height-1)) if random.random() < 0.5 else (self.width-1,random.randint(0,self.height-1)))
                crosspoints.append(point)

        print(crosspoints)

        #define all of the path spots on the map
        path_spots = []
        for x in range(self.width):
            for y in range(self.height):
                path_spots.append((x, y))

        visited = []
        m2 = self.ascii_map.copy()   #make a copy of the make that has untraversed spots

        #add grass until cannot reach any more points
        while len(visited) != len(path_spots):
            #randomize the path spots
            random.shuffle(path_spots)

            #try to remove from the map
            spot = path_spots[0]
            m2[spot[1]][spot[0]] = CHARACTERS["tree"]

            #check if the spot is reachable
            if can_reach_points(m2, crosspoints, crosspoints[0]):
                path_spots.remove(spot)
                self.ascii_map[spot[1]][spot[0]] = CHARACTERS["grass"]
                self.empty_spots.append(spot)
                visited = []
            #put it back if it is not reachable
            else:
                m2[spot[1]][spot[0]] = CHARACTERS["path"]
                visited.append(spot)

        #print the fake map
        for i in m2:
            print("".join([x[0] for x in i]))


    # print the map to the console
    def print_map(self):
        for row in self.ascii_map:
            print("".join([x[0] for x in row]))
 