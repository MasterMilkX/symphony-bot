from map_pcg import GameMap


def main():
    # create a map
    gameMap = GameMap(20, 10)
    gameMap.generate_map()
    gameMap.print_map()


if __name__ == "__main__":
    main()
