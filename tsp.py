import itertools
import math


def euclidean_distance(p1, p2):
    """Calculates euclidean distance between 2 points"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def total_distance(route):
    """Calculates total distance of a route"""
    return sum(
            euclidean_distance(route[i], route[i + 1])
            for i in range(len(route) - 1)
        ) + euclidean_distance(route[-1], route[0])


def brute_force_tsp(points):
    """Brute force solution for Travelling Salesman Problem"""
    best_route = None
    min_distance = float("inf")

    for perm in itertools.permutations(points):
        dist = total_distance(perm)
        if dist < min_distance:
            min_distance = dist
            best_route = perm

    return best_route, min_distance
