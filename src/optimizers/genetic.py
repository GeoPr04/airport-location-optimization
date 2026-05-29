import numpy as np
from functions.distance import calc_dist
import random


def initialize(data, n_children, n_airports, boundries):

    list_children = [] # (aiports, cost)
    for i in range(n_children):
        cost = 0

        list_airports = []
        for n in range(n_airports):
            x = random.randint(0, boundries[0])
            y = random.randint(0, boundries[1])
            list_airports.append((x, y))

        for j in data:
            
            closest_aiport = min(range(len(list_airports)), key=lambda k: calc_dist(list_airports[k][0], list_airports[k][1], j[0], j[1]))

            cost += j[2] * calc_dist(list_airports[closest_aiport][0], list_airports[closest_aiport][1], j[0], j[1])
        
        list_children.append((list_airports, cost))

    return list_children


def genetic_algorthm(data):
    n_airports = 2
    boundries = (300, 250)
    n_children = 10
    generations = 10

    
    list_children = initialize(data, n_children, n_airports, boundries)




    for i in range(generations):
        pass





