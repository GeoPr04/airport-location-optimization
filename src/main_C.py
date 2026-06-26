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

# Γράφημα Α: Καμπύλη Σύγκλισης
plt.figure(figsize=(6, 4))
plt.plot(error_cost, color="blue", linewidth=2, label="Genetic Convergence")
plt.xlabel("Iteration")
plt.ylabel("Best Cost")
plt.title("Genetic Algorithm Convergence (Stage C)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

# Γράφημα Β
best_airports = best_solution[0]
plot_airport_system(data, best_airports, title="Στάδιο Γ - Δίκτυο Δύο Αεροδρομίων")
