# from optimizers.genetic import genetic_algorithm
import random

import matplotlib.pyplot as plt
import numpy as np

from functions.make_cities import make_cities
from functions.visualization import plot_airport_system
from optimizers.genetic_lab_implementation import genetic_algorithm

boundries = [500, 500]
n_cities = 20  # random.randint(3, 30)
n_airports = 6  # random.randint(1, 8)
population_min = 40000
population_max = 140000


cities = make_cities(
    n_cities, boundries, population_min=population_min, population_max=population_max
)

best_solution, error_cost = genetic_algorithm(
    cities,
    n_airports=n_airports,
    boundries=boundries,
    n_children=800,
    iterations=100,
    mutation_rate=0.3,
    mutation_strength_perc=0.2,
)

best_airports = best_solution[0]
plot_airport_system(
    cities, best_airports, title="Stage D: Genetic Algorithm Optimization"
)
