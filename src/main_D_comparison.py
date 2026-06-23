from optimizers.genetic_lab_implementation import genetic_algorithm
from optimizers.pso import pso_airport_optimization
from functions.make_cities import make_cities
import matplotlib.pyplot as plt
import random
import numpy as np
import time


boundries = [500, 500]
n_cities = 20 # random.randint(3, 30)
n_airports = 6 # random.randint(1, 8)
population_min = 40000
population_max = 140000
iterations = 100

cities = make_cities(n_cities, boundries, population_min = population_min, population_max = population_max)


start = time.perf_counter()
best_solution_genetic , error_cost_genetic = genetic_algorithm(cities,
                                              n_airports=n_airports,
                                              boundries=boundries,
                                              n_children = 800,
                                              iterations = iterations,
                                              mutation_rate = 0.3,
                                              mutation_strength_perc = 0.2)
time_genetic = time.perf_counter() - start



best_airports_pso, best_cost_pso, assignments_pso, cost_history = pso_airport_optimization(cities=cities, 
                                                                                           n_airports=n_airports,
                                                                                           x_bounds=None,
                                                                                           y_bounds=None,
                                                                                           n_particles=50,
                                                                                           iterations=iterations)
time_pso = time.perf_counter() - time_genetic



new_data = [t[:-1] for t in cities]
cities = np.array(new_data)
airports = np.array(best_solution_genetic[0])

for i in range(len(error_cost_genetic)):
    error_difference = np.abs(error_cost_genetic[i] - cost_history)


print(f"Genetic algorithm ran for: {time_genetic:.2f}s")
print(f"PSO algorithm ran for: {time_pso:.2f}s")

plt.figure()
plt.xlabel("Iteration")
plt.ylabel("Best cost")
plt.title("Comparison")
plt.grid(True)

plt.plot(cost_history, label="PSO")
plt.plot(error_cost_genetic, label="Genetic")
# plt.plot(error_difference, label = "Difference")
plt.legend()
plt.show()





