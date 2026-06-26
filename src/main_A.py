import matplotlib.pyplot as plt
import numpy as np

from functions.visualization import plot_airport_system

# -----------------------------
# ΔΕΔΟΜΕΝΑ ΠΟΛΕΩΝ
# -----------------------------

cities = np.array(
    [[80, 140], [110, 200], [190, 150], [250, 200], [240, 90], [200, 60], [100, 70]],
    dtype=float,
)

# -----------------------------
# ΣΥΝΑΡΤΗΣΗ ΚΟΣΤΟΥΣ (Α)
# -----------------------------


def total_distance(point):
    x, y = point
    distances = np.sqrt((cities[:, 0] - x) ** 2 + (cities[:, 1] - y) ** 2)
    return np.sum(distances)


# -----------------------------
# ΒΕΛΤΙΣΤΟΠΟΙΗΣΗ
# -----------------------------

best_cost = float("inf")
best_point = None

for _ in range(20000):
    x = np.random.uniform(50, 300)
    y = np.random.uniform(50, 250)

    cost = total_distance([x, y])

    if cost < best_cost:
        best_cost = cost
        best_point = [x, y]

airport = np.array(best_point)
cost = best_cost

print("ΕΡΩΤΗΜΑ Α - Απλή χωροθέτηση ενός αεροδρομίου")
print(f"Βέλτιστη θέση αεροδρομίου: x = {airport[0]:.2f}, y = {airport[1]:.2f}")
print(f"Συνολικό άθροισμα αποστάσεων: {cost:.2f}")

plot_airport_system(
    cities, [airport], title="Ερώτημα Α - Απλή χωροθέτηση ενός αεροδρομίου"
)
