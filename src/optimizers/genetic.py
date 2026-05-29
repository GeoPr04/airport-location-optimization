import numpy as np
from functions.distance import calc_dist
import random


def initialize(data, n_children, n_airports, boundries):

    list_children = [] # [aiports, cost]
    for i in range(n_children):
        cost = 0

        list_airports = [] # [(x,y),...]
        for n in range(n_airports):
            x = random.randint(0, boundries[0])
            y = random.randint(0, boundries[1])
            list_airports.append((x, y))

        for j in data:
            
            closest_aiport = min(range(len(list_airports)), key=lambda k: calc_dist(list_airports[k][0], list_airports[k][1], j[0], j[1]))

            cost += j[2] * calc_dist(list_airports[closest_aiport][0], list_airports[closest_aiport][1], j[0], j[1])
        
        list_children.append((list_airports, cost))

    return list_children

def find_best_parents(list_children):
    
    sorted_parents = sorted(list_children, key=lambda i: i[-1])
    best_2_parents =  [sorted_parents[0], sorted_parents[1]]
    
    return best_2_parents


def crossover(parent1, parent2):

    child = []
    for gene1, gene2 in zip(parent1[0], parent2[0]):
        alpha = random.random()

        x = alpha * gene1[0] + (1 - alpha) * gene2[0]
        y = alpha * gene1[1] + (1 - alpha) * gene2[1]

        child.append((x, y))

    return child


def mutation():
    pass


def next_gen(data, n_children, n_airports, boundries):
    pass



def genetic_algorthm(data):
    n_airports = 2
    boundries = (300, 250)
    n_children = 10
    generations = 10

    
    list_children = initialize(data, n_children, n_airports, boundries)




    for i in range(1):
        best_2_parents = find_best_parents(list_children)
        child = crossover(best_2_parents[0], best_2_parents[1])
        print("\n", best_2_parents[0])
        print("\n", best_2_parents[1])
        print("\n", child, "\n")




