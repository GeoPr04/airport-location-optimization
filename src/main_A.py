import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# ΔΕΔΟΜΕΝΑ ΠΟΛΕΩΝ
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

# -----------------------------
# ΣΥΝΑΡΤΗΣΗ ΚΟΣΤΟΥΣ
# -----------------------------

def total_distance(point):
    x, y = point
    distances = np.sqrt((cities[:,0]-x)**2 + (cities[:,1]-y)**2)
    return np.sum(distances)

# -----------------------------
# MONTE CARLO OPTIMIZATION
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

# -----------------------------
# ΓΡΑΦΗΜΑ
# -----------------------------

plt.figure(figsize=(8,6))

plt.scatter(cities[:,0], cities[:,1], s=120, label="Πόλεις")

for x, y in cities:
    plt.text(x+3, y+3, f"({int(x)}, {int(y)})")

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

plt.title("Ερώτημα Α - Απλή χωροθέτηση ενός αεροδρομίου")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()