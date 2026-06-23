import random
import numpy as np


def calc_dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def _normalize_boundries(boundries):
    if len(boundries) != 2:
        raise ValueError("boundries must be (max_x, max_y) or ((min_x, max_x), (min_y, max_y))")

    if isinstance(boundries[0], (list, tuple)) and isinstance(boundries[1], (list, tuple)):
        x_min, x_max = boundries[0]
        y_min, y_max = boundries[1]
    else:
        x_min, x_max = 0, boundries[0]
        y_min, y_max = 0, boundries[1]

    x_min, x_max = float(x_min), float(x_max)
    y_min, y_max = float(y_min), float(y_max)

    if x_min >= x_max or y_min >= y_max:
        raise ValueError("boundries min values must be smaller than max values")

    return (x_min, x_max), (y_min, y_max)


def _clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def calc_solution_cost(data, airports):
    if not airports:
        raise ValueError("at least one airport is required")

    cost = 0
    for city_x, city_y, population in data:
        closest_distance = min(
            calc_dist(airport_x, airport_y, city_x, city_y)
            for airport_x, airport_y in airports
        )
        cost += population * closest_distance

    return cost


def calc_cost(data, list_children):
    return [(child, calc_solution_cost(data, child)) for child in list_children]


def initialize(data, n_children, n_airports, boundries):
    x_bounds, y_bounds = _normalize_boundries(boundries)
    population = []

    for _ in range(n_children):
        airports = [
            (
                random.uniform(x_bounds[0], x_bounds[1]),
                random.uniform(y_bounds[0], y_bounds[1]),
            )
            for _ in range(n_airports)
        ]
        population.append((airports, calc_solution_cost(data, airports)))

    return population


def find_best_parents(list_children_cost, n_parents=2):
    return sorted(list_children_cost, key=lambda child_cost: child_cost[1])[:n_parents]


def selection(list_children_cost, tournament_size=3):
    tournament_size = min(tournament_size, len(list_children_cost))
    candidates = random.sample(list_children_cost, tournament_size)
    return min(candidates, key=lambda child_cost: child_cost[1])


def crossover(parent1, parent2):
    child = []

    for airport1, airport2 in zip(parent1[0], parent2[0]):
        alpha = random.random()
        x = alpha * airport1[0] + (1 - alpha) * airport2[0]
        y = alpha * airport1[1] + (1 - alpha) * airport2[1]
        child.append((x, y))

    return child


def mutation(child, mutation_rate, mutation_strength_perc, boundries):
    x_bounds, y_bounds = _normalize_boundries(boundries)
    x_strength = mutation_strength_perc * (x_bounds[1] - x_bounds[0])
    y_strength = mutation_strength_perc * (y_bounds[1] - y_bounds[0])
    mutated_child = []

    for airport_x, airport_y in child:
        if random.random() < mutation_rate:
            airport_x += random.uniform(-x_strength, x_strength)
            airport_y += random.uniform(-y_strength, y_strength)
            airport_x = _clamp(airport_x, x_bounds[0], x_bounds[1])
            airport_y = _clamp(airport_y, y_bounds[0], y_bounds[1])

        mutated_child.append((airport_x, airport_y))

    return mutated_child


def next_gen(list_children_cost, n_children, mutation_rate, mutation_strength_perc, boundries):
    elite_count = min(2, len(list_children_cost), n_children)
    elites = find_best_parents(list_children_cost, elite_count)
    next_population = [airports for airports, _ in elites]

    while len(next_population) < n_children:
        parent1 = selection(list_children_cost)
        parent2 = selection(list_children_cost)
        child = crossover(parent1, parent2)
        child = mutation(child, mutation_rate, mutation_strength_perc, boundries)
        next_population.append(child)

    return next_population


def genetic_algorithm(
    data,
    n_airports=2,
    boundries=(300, 250),
    n_children=800,
    iterations=20,
    mutation_rate=0.3,
    mutation_strength_perc=0.2,
    seed=None,
):
    if seed is not None:
        random.seed(seed)

    if not data:
        raise ValueError("data must contain at least one city: (x, y, population)")
    if n_airports < 1:
        raise ValueError("n_airports must be at least 1")
    if n_children < 2:
        raise ValueError("n_children must be at least 2")
    if iterations < 0:
        raise ValueError("iterations must be non-negative")
    if not 0 <= mutation_rate <= 1:
        raise ValueError("mutation_rate must be in [0, 1]")
    if mutation_strength_perc < 0:
        raise ValueError("mutation_strength_perc must be non-negative")

    list_children_cost = initialize(data, n_children, n_airports, boundries)
    best_solution = find_best_parents(list_children_cost, 1)[0]
    error_cost = [best_solution[1]]

    for _ in range(iterations):
        list_children = next_gen(
            list_children_cost,
            n_children,
            mutation_rate,
            mutation_strength_perc,
            boundries,
        )
        list_children_cost = calc_cost(data, list_children)

        current_best = find_best_parents(list_children_cost, 1)[0]
        if current_best[1] < best_solution[1]:
            best_solution = current_best

        error_cost.append(best_solution[1])

    return best_solution, error_cost


def genetic_algorthm(*args, **kwargs):
    return genetic_algorithm(*args, **kwargs)
