import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# ΔΕΔΟΜΕΝΑ ΠΟΛΕΩΝ ΚΑΙ ΠΛΗΘΥΣΜΩΝ
# -----------------------------

cities = np.array([
    [80, 140],
    [110, 200],
    [190, 150],
    [250, 200],
    [240, 90],
    [200, 60],
    [100, 70]
], dtype=float)

populations = np.array([
    40000,
    60000,
    50000,
    90000,
    120000,
    100000,
    70000
], dtype=float)

# -----------------------------
# ΣΥΝΑΡΤΗΣΗ ΚΟΣΤΟΥΣ (Β)
# -----------------------------

def weighted_total_distance(point):
    x, y = point

    distances = np.sqrt(
        (cities[:,0] - x)**2 +
        (cities[:,1] - y)**2
    )

    return np.sum(populations * distances)

# -----------------------------
# ΒΕΛΤΙΣΤΟΠΟΙΗΣΗ
# -----------------------------

best_cost = float("inf")
best_point = None

for _ in range(30000):

    x = np.random.uniform(50, 300)
    y = np.random.uniform(50, 250)

    cost = weighted_total_distance([x, y])

    if cost < best_cost:
        best_cost = cost
        best_point = [x, y]

airport = np.array(best_point)
cost = best_cost

print("ΕΡΩΤΗΜΑ Β - Σταθμισμένη χωροθέτηση ενός αεροδρομίου")
print(f"Βέλτιστη θέση αεροδρομίου: x = {airport[0]:.2f}, y = {airport[1]:.2f}")
print(f"Σταθμισμένο συνολικό κόστος: {cost:.2f}")

# -----------------------------
# ΓΡΑΦΗΜΑ
# -----------------------------

plt.figure(figsize=(8,6))

sizes = populations / 800

plt.scatter(
    cities[:,0],
    cities[:,1],
    s=sizes,
    label="Πόλεις"
)

for i, (x, y) in enumerate(cities):
    plt.text(x+3, y+3, f"({int(x)}, {int(y)})")
    plt.text(x-15, y+14,
             f"{int(populations[i]):,}".replace(",", "."))

plt.scatter(
    airport[0],
    airport[1],
    marker="*",
    s=300,
    label=f"Αεροδρόμιο ({airport[0]:.2f}, {airport[1]:.2f})"
)

for city in cities:
    plt.plot(
        [airport[0], city[0]],
        [airport[1], city[1]],
        "--",
        alpha=0.5
    )

plt.title("Ερώτημα Β - Σταθμισμένη χωροθέτηση ενός αεροδρομίου")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()