

def read_data(stage): # example: stage = "A"
    directory = "../data/coordinates_" + stage + ".txt"
    with open(directory, "r") as file:
        for line in file:
            print(line)