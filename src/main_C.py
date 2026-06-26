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
    iterations=50,
    mutation_rate=0.3,
    mutation_strength_perc=0.2,
)

# Γράφημα Α: Καμπύλη Σύγκλισης του Γενετικού Αλγορίθμου
plt.figure(figsize=(6, 4))
plt.plot(error_cost, color="blue", linewidth=2, label="Genetic Convergence")
plt.xlabel("Iteration")
plt.ylabel("Best Cost")
plt.title("Genetic Algorithm Convergence (Stage C)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

# Γράφημα Β: Ο 2D Χάρτης με τα 2 Βέλτιστα Αεροδρόμια
best_airports = best_solution[0]
plot_airport_system(data, best_airports, title="Στάδιο Γ - Δίκτυο Δύο Αεροδρομίων")
"""
# ======================
# OLD PLOT
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
"""
