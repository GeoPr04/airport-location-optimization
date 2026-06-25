import matplotlib.pyplot as plt
import numpy as np

from functions.read_data import read_data
from functions.visualization import plot_airport_system

# from optimizers.genetic import genetic_algorthm
from optimizers.genetic_lab_implementation import genetic_algorithm

data = read_data("C")

best_solution, error_cost = genetic_algorithm(
    data,
    n_airports=2,
    boundries=(300, 250),
    n_children=800,
    iterations=10,
    mutation_rate=0.3,
    mutation_strength_perc=0.2,
)
# plot_airport_system(data, best_airports, title="Stage C")

# old visualization

print("best cost:", error_cost[-1])
plt.plot(error_cost)

new_data = [t[:-1] for t in data]
cities = np.array(new_data)
airports = np.array(best_solution[0])

# print(cities)
# print(airports)

# ======================
# PLOT
# ======================

plt.figure(figsize=(8, 6))

# cities
plt.scatter(cities[:, 0], cities[:, 1], label="Cities", s=80)

# airports
plt.scatter(airports[:, 0], airports[:, 1], marker="X", s=250, label="Airports")

# connect each city with its closest airport
for city in cities:
    distances = np.linalg.norm(airports - city, axis=1)

    nearest = np.argmin(distances)

    plt.plot(
        [city[0], airports[nearest, 0]], [city[1], airports[nearest, 1]], alpha=0.5
    )

plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()
