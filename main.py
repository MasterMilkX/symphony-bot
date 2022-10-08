from map_pcg import SongMap


def main():
    # create a map
    gameMap = SongMap(20, 10)
    gameMap.generate_map()
    gameMap.print_map()


if __name__ == "__main__":
    main()
