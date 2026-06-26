import time

import matplotlib.pyplot as plt
import numpy as np

from functions.make_cities import make_cities
from functions.visualization import plot_interactive_dashboard
from optimizers.genetic_lab_implementation import genetic_algorithm
from optimizers.pso import pso_airport_optimization

# Παράμετροι Προβλήματος
boundries = [500, 500]
n_cities = 20
n_airports = 6
population_min = 40000
population_max = 140000
iterations = 100


cities = make_cities(
    n_cities,
    boundries,
    population_min=population_min,
    population_max=population_max,
    min_distance=60,
)

# Genetic
start_genetic = time.perf_counter()
best_solution_genetic, error_cost_genetic = genetic_algorithm(
    cities,
    n_airports=n_airports,
    boundries=boundries,
    n_children=800,
    iterations=iterations,
    mutation_rate=0.3,
    mutation_strength_perc=0.2,
)
time_genetic = time.perf_counter() - start_genetic


# PSO
start_pso = time.perf_counter()
best_airports_pso, best_cost_pso, assignments_pso, cost_history = (
    pso_airport_optimization(
        cities=cities,
        n_airports=n_airports,
        x_bounds=None,
        y_bounds=None,
        n_particles=50,
        iterations=iterations,
    )
)
time_pso = time.perf_counter() - start_pso


print("Για 6 αεροδρόμια")
print(
    f"Γενετικός Αλγόριθμος -> Χρόνος: {time_genetic:.2f}s | Κόστος: {error_cost_genetic[-1]:,.2f}"
)
print(f"PSO Αλγόριθμος       -> Χρόνος: {time_pso:.2f}s | Κόστος: {best_cost_pso:,.2f}")
print("=" * 50 + "\n")


# Σύγκριση Καμπυλών Σύγκλισης
plt.figure(figsize=(8, 5))
plt.plot(cost_history, label="PSO", color="orange", linewidth=2)
plt.plot(error_cost_genetic, label="Genetic", color="blue", linewidth=2)
plt.xlabel("Iteration")
plt.ylabel("Best Cost")
plt.title("Algorithm Convergence Comparison")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

# 2d Map
plot_interactive_dashboard(cities)
