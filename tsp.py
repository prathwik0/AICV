import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor(points):
    n = len(points)
    tour = [0]
    unvisited = set(range(n))
    unvisited.remove(0)

    while unvisited:
        current = tour[-1]
        near = min(unvisited, key=lambda x:distance(points[current], points[x]))
        tour.append(near)
        unvisited.remove(near)


    return tour

points = [(0,0), (1,2), (2,3), (3,4), (4,2)]
tour = nearest_neighbor(points)
print("Optimal Tour: ", tour)
