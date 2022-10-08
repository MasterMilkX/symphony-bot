from map_pcg import SongMap

def main():
    #create a map
    map = SongMap(10,10)
    map.init_rand_map()
    map.place_player()
    map.print_map()

if __name__ == "__main__":
    main()
