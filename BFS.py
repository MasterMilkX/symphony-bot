from map_constants import CARDINALS

#runs a BFS algorithm on the map to ensure all points are reachable
def can_reach_points(m,reach_points,start_point):
    visited = []
    queue = [start_point]
    while len(queue) > 0:
        point = queue.pop(0)
        if point not in visited:
            visited.append(point)
            for c in CARDINALS:
                x = point[0] + c[0]
                y = point[1] + c[1]
                if (y>=0 and y<len(m) and x>=0 and x<len(m[0])):
                    if m[y][x][1]:   #if the spot is walkable
                        queue.append((x,y))
    for point in reach_points:
        if point not in visited:
            return False
    return True
