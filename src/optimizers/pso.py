import numpy as np
import pyswarms as ps


def pso_airport_optimization(
    cities, n_airports, x_bounds=None, y_bounds=None, n_particles=50, iterations=200
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
                city_positions[:, None, :] - airports[None, :, :], axis=2
            )

            nearest_distances = np.min(distances, axis=1)

            cost = np.sum(populations * nearest_distances)

            costs.append(cost)

        return np.array(costs)

    options = {
        "c1": 1.5,  # προσωπική εμπειρία particle
        "c2": 1.5,  # εμπειρία σμήνους
        "w": 0.7,  # inertia
    }

    optimizer = ps.single.GlobalBestPSO(
        n_particles=n_particles,
        dimensions=dimensions,
        options=options,
        bounds=bounds,
    )

    best_cost, best_position = optimizer.optimize(
        objective_function, iters=iterations, verbose=False
    )

    best_airports = best_position.reshape(n_airports, 2)

    # Ανάθεση κάθε πόλης στο κοντινότερο αεροδρόμιο
    distances = np.linalg.norm(
        city_positions[:, None, :] - best_airports[None, :, :], axis=2
    )

    assignments = np.argmin(distances, axis=1)
    cost_history = optimizer.cost_history

    return best_airports, best_cost, assignments, cost_history
