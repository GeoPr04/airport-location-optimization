import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text


def plot_airport_system(cities, airports, title="Airport Location Optimization"):
    """
    Σχεδιάζει έναν δισδιάστατο χάρτη με πόλεις, αεροδρόμια και τις γραμμές σύνδεσης.

    cities: Λίστα από tuples/lists [(x, y, population), ...] ή numpy array αντίστοιχης μορφής
    airports: Numpy array ή λίστα με τις βέλτιστες θέσεις των αεροδρομίων [[X1, Y1], [X2, Y2], ...]
    title: Ο τίτλος του γραφήματος
    """
    # Μετατροπή σε numpy arrays για ευκολία στους υπολογισμούς
    cities_np = np.array(cities, dtype=float)
    airports_np = np.array(airports, dtype=float)

    city_positions = cities_np[:, :2]
    # Αν δεν υπάρχει στήλη πληθυσμού (π.χ. Στάδιο Α), βάζουμε σταθερό πληθυσμό 1
    populations = cities_np[:, 2] if cities_np.shape[1] > 2 else np.ones(len(cities_np))

    # 1. Υπολογισμός αναθέσεων: Βρίσκουμε το κοντινότερο αεροδρόμιο για κάθε πόλη
    # Υπολογίζει την απόσταση κάθε πόλης (rows) από κάθε αεροδρόμιο (columns)
    distances = np.linalg.norm(
        city_positions[:, None, :] - airports_np[None, :, :], axis=2
    )
    assignments = np.argmin(distances, axis=1)
    min_distances = np.min(distances, axis=1)

    # Υπολογισμός τελικού κόστους για τον τίτλο
    total_cost = np.sum(populations * min_distances)

    # Αρχικοποίηση γραφήματος
    plt.figure(figsize=(10, 8))

    # Δημιουργία χρωματικής παλέτας ανάλογα με τον αριθμό των αεροδρομίων
    cmap = plt.colormaps["tab10"].resampled(len(airports_np))
    colors = cmap(assignments)

    # 2. Σχεδίαση Γραμμών Σύνδεσης (Πόλη -> Αεροδρόμιο)
    for i in range(len(cities_np)):
        air_id = assignments[i]
        plt.plot(
            [city_positions[i, 0], airports_np[air_id, 0]],
            [city_positions[i, 1], airports_np[air_id, 1]],
            linestyle="--",
            color=cmap(air_id),
            linewidth=1.2,
            alpha=0.4,
        )

    # 3. Σχεδίαση Πόλεων (Κύκλοι ανάλογοι του πληθυσμού)
    # Αν οι πληθυσμοί είναι μεγάλοι (π.χ. 40.000), τους κανονικοποιούμε για το γράφημα
    if cities_np.shape[1] > 2:
        scale_factor = (
            populations / 300
        )  # Ρύθμισε το 300 ανάλογα με το πόσο μεγάλους θες τους κύκλους
    else:
        scale_factor = 100  # Σταθερό μέγεθος για το Στάδιο Α

    plt.scatter(
        city_positions[:, 0],
        city_positions[:, 1],
        s=scale_factor,
        c=colors,
        alpha=0.75,
        edgecolors="black",
        linewidths=0.5,
        label="Cities",
    )

    # 4. Σχεδίαση Αεροδρομίων (Διακριτά κόκκινα "Χ")
    plt.scatter(
        airports_np[:, 0],
        airports_np[:, 1],
        marker="X",
        s=300,
        color="red",
        edgecolors="black",
        linewidths=1,
        label="Airports",
    )

    # 5. Προσθήκη Labels με αυτόματη απώθηση (adjustText)
    texts = []

    for i in range(len(cities_np)):
        t = plt.text(city_positions[i, 0], city_positions[i, 1], f"C{i}", fontsize=9)
        texts.append(t)

    for i in range(len(airports_np)):
        t = plt.text(
            airports_np[i, 0],
            airports_np[i, 1],
            f"A{i}",
            fontsize=11,
            fontweight="bold",
            color="black",
            bbox=dict(
                boxstyle="round,pad=0.15", fc="white", ec="gray", lw=0.5, alpha=0.7
            ),
        )
        texts.append(t)

    # Αυτό το μαγικό line διορθώνει τα πάντα αυτόματα στην οθόνη!
    adjust_text(texts, arrowprops=dict(arrowstyle="->", color="gray", lw=0.5))

    # Μορφοποίηση Χάρτη
    plt.title(
        f"{title}\nTotal Cost (C) = {total_cost:,.2f}", fontsize=14, fontweight="bold"
    )
    plt.xlabel("X Coordinate", fontsize=11)
    plt.ylabel("Y Coordinate", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.xlim(-20, 520)
    plt.ylim(-20, 520)

    # Διαχείριση Legend (ώστε να μην εμφανίζεται 100 φορές)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc="upper right")

    plt.show()
