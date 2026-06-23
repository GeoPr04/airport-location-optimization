from optimizers.pso import pso_airport_optimization
from functions.make_cities import make_cities
import matplotlib.pyplot as plt
import random
import numpy as np


boundries = [500, 500]
n_cities = 20 # random.randint(3, 30)
n_airports = 6 # random.randint(1, 8)
population_min = 40000
population_max = 140000


cities = make_cities(n_cities, boundries)
# print(cities)
best_airports, best_cost, assignments, cost_history = pso_airport_optimization(cities=cities, n_airports=n_airports)



# visualization

cities_np = np.array(cities)

city_x = cities_np[:, 0]
city_y = cities_np[:, 1]
city_pop = cities_np[:, 2]


plt.figure()
plt.plot(cost_history)
plt.xlabel("Iteration")
plt.ylabel("Best cost")
plt.title("PSO convergence")
plt.grid(True)

plt.figure(figsize=(10, 8))

# Χρωματίζουμε κάθε πόλη ανάλογα με το αεροδρόμιο που εξυπηρετείται
colors = plt.cm.tab10(assignments)

# Πόλεις
plt.scatter(
    city_x,
    city_y,
    s=city_pop / 1000,  # μέγεθος ανάλογο πληθυσμού
    c=colors,
    alpha=0.7,
    label="Cities"
)

# Αεροδρόμια
plt.scatter(
    best_airports[:, 0],
    best_airports[:, 1],
    marker="X",
    s=400,
    color="red",
    label="Airports"
)

# Γραμμές πόλης -> αεροδρομίου
for i in range(len(cities_np)):
    airport_id = assignments[i]

    plt.plot(
        [city_x[i], best_airports[airport_id, 0]],
        [city_y[i], best_airports[airport_id, 1]],
        linestyle="--",
        linewidth=1,
        alpha=0.5
    )

# Labels πόλεων
for i in range(len(cities_np)):
    plt.annotate(
        f"C{i}",
        (city_x[i], city_y[i]),
        xytext=(5, 5),
        textcoords="offset points"
    )

# Labels αεροδρομίων
for i in range(len(best_airports)):
    plt.annotate(
        f"A{i}",
        (best_airports[i, 0], best_airports[i, 1]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=12,
        fontweight="bold"
    )

plt.title(
    f"Airport Optimization (n={len(best_airports)})\nCost = {best_cost:.2f}"
)

plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)
plt.legend()

plt.axis("equal")

plt.show()