import random
import numpy as np

def calc_dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calc_cost(data, list_children):
    list_children_cost = []
    for child in list_children:
        cost = 0

        for j in data:
            closest_aiport = min(range(len(child)), key=lambda k: calc_dist(child[k][0], child[k][1], j[0], j[1]))

            cost += j[2] * calc_dist(child[closest_aiport][0], child[closest_aiport][1], j[0], j[1])

        list_children_cost.append((child, cost))

    return list_children_cost


def initialize(data, n_children, n_airports, boundries):

    list_children_cost = [] # [aiports, cost]
    for _ in range(n_children):
        cost = 0

        list_airports = [] # [(x,y),...]
        for _ in range(n_airports):
            x = random.randint(0, boundries[0])
            y = random.randint(0, boundries[1])
            list_airports.append((x, y))

        for j in data:
            
            closest_aiport = min(range(len(list_airports)), key=lambda k: calc_dist(list_airports[k][0], list_airports[k][1], j[0], j[1]))

            cost += j[2] * calc_dist(list_airports[closest_aiport][0], list_airports[closest_aiport][1], j[0], j[1])
        
        list_children_cost.append((list_airports, cost))

    return list_children_cost

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


def mutation(child, mutation_rate, mutation_strength_perc, boundries):
    mutated_child = []

    for airport in child:
        if random.random() < mutation_rate:
            new_airport = (airport[0]+random.uniform(-mutation_strength_perc*boundries[0], mutation_strength_perc*boundries[0]), airport[1]+random.uniform(-mutation_strength_perc*boundries[1], mutation_strength_perc*boundries[1]))
            mutated_child.append(new_airport)
        else:
            mutated_child.append(airport)
    return mutated_child


def next_gen(best_2_parents, n_children, mutation_rate, mutation_strength_perc, boundries):

    list_children = []
    for _ in range(n_children-2):

        child = crossover(best_2_parents[0], best_2_parents[1])
        child = mutation(child, mutation_rate, mutation_strength_perc, boundries)
        list_children.append(child)

    return list_children



def genetic_algorithm(data,
                     n_airports = 2,
                     boundries = (300, 250),
                     n_children = 800,
                     iterations = 20,
                     mutation_rate = 0.3,
                     mutation_strength_perc = 0.2):


    list_children_cost = initialize(data, n_children, n_airports, boundries)

    best_2_parents = find_best_parents(list_children_cost)

    error_cost = [best_2_parents[0][1]]

    for _ in range(iterations): # iterations

        list_children = next_gen(best_2_parents, n_children, mutation_rate, mutation_strength_perc, boundries)
        list_children.append(best_2_parents[0][0])
        list_children.append(best_2_parents[1][0])

        list_children_cost = calc_cost(data, list_children)

        best_2_parents = find_best_parents(list_children_cost)

        error_cost.append(best_2_parents[0][1])

    return best_2_parents[0], error_cost




