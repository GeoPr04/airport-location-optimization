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


# visualization

# new_data = [t[:-1] for t in cities]
# cities = np.array(new_data)
# airports = np.array(best_solution[0])


# print("best cost:", error_cost[-1])
# plt.figure()
# plt.xlabel("Iteration")
# plt.ylabel("Best cost")
# plt.title("PSO convergence")
# plt.grid(True)
# plt.plot(error_cost)


# # print(cities)
# # print(airports)

# # ======================
# # PLOT
# # ======================

# plt.figure(figsize=(8, 6))

# # cities
# plt.scatter(cities[:, 0], cities[:, 1], label="Cities", s=80)

# # airports
# plt.scatter(airports[:, 0], airports[:, 1], marker="X", s=250, label="Airports")

# # connect each city with its closest airport
# for city in cities:
#     distances = np.linalg.norm(airports - city, axis=1)

#     nearest = np.argmin(distances)

#     plt.plot(
#         [city[0], airports[nearest, 0]], [city[1], airports[nearest, 1]], alpha=0.5
#     )

# plt.grid(True)
# plt.legend()
# plt.axis("equal")
# plt.show()
