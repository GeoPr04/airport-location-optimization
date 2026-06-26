import random

import numpy as np


def make_cities(
    n_cities=10,
    boundries=[400, 400],
    population_min=40000,
    population_max=140000,
    min_distance=60,
):
    """
    Παράγει n τυχαίες πόλεις εξασφαλίζοντας ότι καμία δεν είναι υπερβολικά κοντά σε άλλη.
    min_distance: Η ελάχιστη επιτρεπόμενη Ευκλείδεια απόσταση μεταξύ δύο πόλεων.
    """

    cities = []
    max_attempts = (
        2000  # Μέγιστες προσπάθειες για την αποφυγή ατέρμονου βρόχου (infinite loop)
    )

    for _ in range(n_cities):
        attempts = 0
        accepted = False

        while attempts < max_attempts and not accepted:
            # Αφήνουμε και ένα μικρό περιθώριο 15 μονάδων από τα ακραία όρια του χάρτη
            x = random.randint(15, boundries[0] - 15)
            y = random.randint(15, boundries[1] - 15)

            # Έλεγχος αν η νέα θέση είναι πολύ κοντά σε κάποια ήδη υπάρχουσα πόλη
            too_close = False
            for existing_city in cities:
                dist = np.sqrt(
                    (x - existing_city[0]) ** 2 + (y - existing_city[1]) ** 2
                )
                if dist < min_distance:
                    too_close = True
                    break  # Σταματάει τον έλεγχο για τις υπόλοιπες, αφού βρέθηκε μία πολύ κοντά

            # Αν δεν είναι κοντά σε καμία, την αποδεχόμαστε
            if not too_close:
                population = random.randint(population_min, population_max)
                cities.append((x, y, population))
                accepted = True

            attempts += 1

        # Αν εξαντληθούν οι προσπάθειες (π.χ. αν ζητήσουμε πάρα πολλές πόλεις σε μικρό χώρο)
        if not accepted:
            print(
                f"Warning: Could only generate {len(cities)}/{n_cities} cities due to distance constraints."
            )
            break

    return cities
