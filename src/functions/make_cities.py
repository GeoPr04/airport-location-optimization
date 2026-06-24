import random


def make_cities(
    n_cities=10, boundries=[400, 400], population_min=40000, population_max=140000
):

    cities = []
    for _ in range(n_cities):
        x = random.randint(0, boundries[0])
        y = random.randint(0, boundries[1])
        population = random.randint(population_min, population_max)
        cities.append((x, y, population))

    return cities
