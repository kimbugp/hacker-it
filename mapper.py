"""
Find connected cities from the origin to destinations 
given that the greated common divisor is greater than the threshold value
"""
import math
from graph import Graph


def connectedCities(n, g, originCities, destinationCities):
    """Get connected cities
    
    Args:
        n (int ): number of cities
        g (int): threshold value 
        originCities (list): [description]
        destinationCities (list): [description]
    """
    graph = Graph()
    all_cities = originCities + destinationCities

    for city in all_cities:
        for destination in all_cities:
            divisor = math.gcd(city, destination)
            if divisor > g:
                graph.addEdge(city, destination)
    result = list()
    for origin, destination in zip(originCities, destinationCities):
        path = graph.find_path(origin, destination)
        if path:
            print(path)
            result.append(1)
        else:
            result.append(0)
    return result


result = connectedCities(10, 1, [10, 4, 3, 6, 4, 2, 4, 64, 3, 2, 35],
                         [3, 6, 2, 9, 3, 6, 75, 43])
print(result)
