from functions.read_data import read_data
from optimizers.genetic import genetic_algorthm
import matplotlib.pyplot as plt
import numpy as np

data = read_data("C")

best_solution , error_cost = genetic_algorthm(data, n_airports = 2, boundries = (300, 250), n_children = 800, iterations = 10, mutation_rate = 0.3, mutation_strength_perc = 0.2)


# visualization

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

# πόλεις
plt.scatter(
    cities[:, 0],
    cities[:, 1],
    label="Cities",
    s=80
)

# αεροδρόμια
plt.scatter(
    airports[:, 0],
    airports[:, 1],
    marker="X",
    s=250,
    label="Airports"
)

# σύνδεση κάθε πόλης με το κοντινότερο αεροδρόμιο
for city in cities:

    distances = np.linalg.norm(
        airports - city,
        axis=1
    )

    nearest = np.argmin(distances)

    plt.plot(
        [city[0], airports[nearest, 0]],
        [city[1], airports[nearest, 1]],
        alpha=0.5
    )

plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()
    
