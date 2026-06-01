from functions.read_data import read_data
import matplotlib.pyplot as plt
import numpy as np
import pyswarms as ps

def pso_airport_optimization(
    cities,
    n_airports,
    x_bounds=None,
    y_bounds=None,
    n_particles=50,
    iterations=200
):
    """
    cities: [(x, y, population), ...]
    n_airports: αριθμός αεροδρομίων
    """

    cities = np.array(cities, dtype=float)

    city_positions = cities[:, :2]
    populations = cities[:, 2]

    # Αυτόματα όρια, αν δεν δοθούν
    if x_bounds is None:
        x_bounds = (np.min(city_positions[:, 0]), np.max(city_positions[:, 0]))

    if y_bounds is None:
        y_bounds = (np.min(city_positions[:, 1]), np.max(city_positions[:, 1]))

    dimensions = 2 * n_airports

    lower_bounds = []
    upper_bounds = []

    for _ in range(n_airports):
        lower_bounds.extend([x_bounds[0], y_bounds[0]])
        upper_bounds.extend([x_bounds[1], y_bounds[1]])

    bounds = (np.array(lower_bounds), np.array(upper_bounds))

    def objective_function(particles):
        """
        particles shape:
        (n_particles, 2 * n_airports)
        """

        costs = []

        for particle in particles:
            airports = particle.reshape(n_airports, 2)

            distances = np.linalg.norm(
                city_positions[:, None, :] - airports[None, :, :],
                axis=2
            )

            nearest_distances = np.min(distances, axis=1)

            cost = np.sum(populations * nearest_distances)

            costs.append(cost)

        return np.array(costs)

    options = {
        "c1": 1.5,  # προσωπική εμπειρία particle
        "c2": 1.5,  # εμπειρία σμήνους
        "w": 0.7    # inertia
    }

    optimizer = ps.single.GlobalBestPSO(
        n_particles=n_particles,
        dimensions=dimensions,
        options=options,
        bounds=bounds
    )

    best_cost, best_position = optimizer.optimize(
        objective_function,
        iters=iterations
    )

    best_airports = best_position.reshape(n_airports, 2)

    # Ανάθεση κάθε πόλης στο κοντινότερο αεροδρόμιο
    distances = np.linalg.norm(
        city_positions[:, None, :] - best_airports[None, :, :],
        axis=2
    )

    assignments = np.argmin(distances, axis=1)

    return best_airports, best_cost, assignments


data = read_data("C")
cities = data
best_airports, best_cost, assignments = pso_airport_optimization(cities=data, n_airports=2)


# visualization

cities_np = np.array(cities)

city_x = cities_np[:, 0]
city_y = cities_np[:, 1]
city_pop = cities_np[:, 2]

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