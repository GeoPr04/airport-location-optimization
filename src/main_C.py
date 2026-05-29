from functions.read_data import read_data
from optimizers.genetic import genetic_algorthm

data = read_data("C")

genetic_algorthm(data)