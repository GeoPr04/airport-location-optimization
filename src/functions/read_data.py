

def read_data(stage): # example: stage = "A"
    directory = "data/coordinates_" + stage + ".txt"
    data = []
    with open(directory, "r") as file:
        for line in file:
            inside = line[line.find("(")+1 : line.find(")")]
            data.append(tuple(map(int, inside.split(","))))

    return data # list(x, y, population)