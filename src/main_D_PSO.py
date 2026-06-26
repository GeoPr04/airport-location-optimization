import random

import matplotlib.pyplot as plt
import numpy as np

from functions.make_cities import make_cities
from functions.visualization import plot_airport_system
from optimizers.pso import pso_airport_optimization

boundries = [500, 500]
n_cities = 20  # random.randint(3, 30)
n_airports = 6  # random.randint(1, 8)
population_min = 40000
population_max = 140000


cities = make_cities(n_cities, boundries)

best_airports, best_cost, assignments, cost_history = pso_airport_optimization(
    cities=cities, n_airports=n_airports
)


plot_airport_system(cities, best_airports, title="Stage D: PSO Algorithm Optimization")
