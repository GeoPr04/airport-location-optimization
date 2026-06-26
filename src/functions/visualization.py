import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text
from matplotlib.widgets import Button, RadioButtons, Slider


def plot_airport_system(cities, airports, title="Airport Location Optimization"):
    """
    ΣΤΑΤΙΚΟ ΓΡΑΦΗΜΑ: Σχεδιάζει τον χάρτη για τα Στάδια Α, Β, Γ, Δ με γεωμετρικά σύνορα.
    """
    cities_np = np.array(cities, dtype=float)
    airports_np = np.array(airports, dtype=float)

    city_positions = cities_np[:, :2]
    populations = cities_np[:, 2] if cities_np.shape[1] > 2 else np.ones(len(cities_np))

    distances = np.linalg.norm(
        city_positions[:, None, :] - airports_np[None, :, :], axis=2
    )
    assignments = np.argmin(distances, axis=1)
    min_distances = np.min(distances, axis=1)
    total_cost = np.sum(populations * min_distances)

    plt.figure(figsize=(10, 8))
    cmap = plt.colormaps["tab10"].resampled(len(airports_np))
    colors = cmap(assignments)

    # --- ΠΡΟΣΘΗΚΗ: ΓΕΩΜΕΤΡΙΚΑ ΣΥΝΟΡΑ (VORONOI BACKGROUND) ---
    grid_x = np.linspace(-20, 520, 200)
    grid_y = np.linspace(-20, 520, 200)
    X, Y = np.meshgrid(grid_x, grid_y)
    grid_points = np.c_[X.ravel(), Y.ravel()]
    # Υπολογισμός κοντινότερου αεροδρομίου για κάθε σημείο του φόντου
    dist_grid = np.linalg.norm(
        grid_points[:, None, :] - airports_np[None, :, :], axis=2
    )
    Z = np.argmin(dist_grid, axis=1).reshape(X.shape)
    # Σχεδίαση έγχρωμου φόντου (zorder=0 για να είναι τέρμα πίσω)
    plt.pcolormesh(X, Y, Z, cmap=cmap, alpha=0.12, shading="auto", zorder=0)

    # 1. Γραμμές σύνδεσης
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

    if cities_np.shape[1] > 2:
        scale_factor = populations / 300
    else:
        scale_factor = 100

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

    for i in range(len(cities_np)):
        plt.annotate(
            f"C{i}",
            (city_positions[i, 0], city_positions[i, 1]),
            xytext=(6, 6),
            textcoords="offset points",
            fontsize=9,
        )
    for i in range(len(airports_np)):
        plt.annotate(
            f"A{i}",
            (airports_np[i, 0], airports_np[i, 1]),
            xytext=(-18, -18),
            textcoords="offset points",
            fontsize=11,
            fontweight="bold",
            color="black",
            bbox=dict(
                boxstyle="round,pad=0.2", fc="white", ec="gray", lw=0.5, alpha=0.85
            ),
        )

    plt.title(
        f"{title}\nTotal Cost (C) = {total_cost:,.2f}", fontsize=14, fontweight="bold"
    )
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True, linestyle=":", alpha=0.4)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.xlim(-20, 520)
    plt.ylim(-20, 520)

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc="upper right")
    plt.show()


def plot_interactive_dashboard(cities_data):
    """
    ΔΙΑΔΡΑΣΤΙΚΟ ΓΡΑΦΗΜΑ: Live dashboard με Sliders, Κουμπιά και γεωμετρικά σύνορα.
    """
    from optimizers.genetic_lab_implementation import genetic_algorithm
    from optimizers.pso import pso_airport_optimization

    cities_np = np.array(cities_data, dtype=float)
    city_positions = cities_np[:, :2]
    populations = cities_np[:, 2]

    fig, ax = plt.subplots(figsize=(11, 9))
    plt.subplots_adjust(bottom=0.28, left=0.25)

    def run_and_draw(n_airports, algorithm_name):
        ax.clear()

        if algorithm_name == "PSO":
            best_airports, best_cost, assignments, _ = pso_airport_optimization(
                cities=cities_data, n_airports=n_airports, iterations=100
            )
        else:
            best_solution, _ = genetic_algorithm(
                cities_data,
                n_airports=n_airports,
                boundries=[500, 500],
                iterations=100,
                n_children=600,
            )
            best_airports = np.array(best_solution[0])
            distances = np.linalg.norm(
                city_positions[:, None, :] - best_airports[None, :, :], axis=2
            )
            assignments = np.argmin(distances, axis=1)
            best_cost = np.sum(populations * np.min(distances, axis=1))

        cmap = plt.colormaps["tab10"].resampled(n_airports)
        colors = cmap(assignments)

        # --- ΠΡΟΣΘΗΚΗ: ΓΕΩΜΕΤΡΙΚΑ ΣΥΝΟΡΑ (VORONOI BACKGROUND LIVE) ---
        grid_x = np.linspace(-20, 520, 200)
        grid_y = np.linspace(-20, 520, 200)
        X, Y = np.meshgrid(grid_x, grid_y)
        grid_points = np.c_[X.ravel(), Y.ravel()]
        dist_grid = np.linalg.norm(
            grid_points[:, None, :] - best_airports[None, :, :], axis=2
        )
        Z = np.argmin(dist_grid, axis=1).reshape(X.shape)
        ax.pcolormesh(X, Y, Z, cmap=cmap, alpha=0.12, shading="auto", zorder=0)

        # Γραμμές σύνδεσης
        for i in range(len(cities_np)):
            air_id = assignments[i]
            ax.plot(
                [city_positions[i, 0], best_airports[air_id, 0]],
                [city_positions[i, 1], best_airports[air_id, 1]],
                linestyle="--",
                color=cmap(air_id),
                linewidth=1.2,
                alpha=0.4,
            )

        ax.scatter(
            city_positions[:, 0],
            city_positions[:, 1],
            s=populations / 300,
            c=colors,
            alpha=0.8,
            edgecolors="black",
            linewidths=0.5,
            label="Cities",
        )
        ax.scatter(
            best_airports[:, 0],
            best_airports[:, 1],
            marker="X",
            s=300,
            color="red",
            edgecolors="black",
            linewidths=1,
            label="Airports",
        )

        texts = []
        for i in range(len(cities_np)):
            t = ax.text(city_positions[i, 0], city_positions[i, 1], f"C{i}", fontsize=9)
            texts.append(t)
        for i in range(len(best_airports)):
            t = ax.text(
                best_airports[i, 0],
                best_airports[i, 1],
                f"A{i}",
                fontsize=11,
                fontweight="bold",
                bbox=dict(
                    boxstyle="round,pad=0.15", fc="white", ec="gray", lw=0.5, alpha=0.7
                ),
            )
            texts.append(t)
        adjust_text(
            texts, ax=ax, arrowprops=dict(arrowstyle="->", color="gray", lw=0.5)
        )

        ax.set_title(
            f"Interactive Optimization ({algorithm_name})\nTotal Cost (C) = {best_cost:,.2f}",
            fontsize=13,
            fontweight="bold",
        )
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(-20, 520)
        ax.set_ylim(-20, 520)
        ax.grid(True, linestyle=":", alpha=0.4)

        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), loc="upper right")
        fig.canvas.draw_idle()

    # Widgets Setup
    ax_slider = plt.axes([0.35, 0.15, 0.45, 0.03])
    slider_m = Slider(
        ax_slider, "Airports (m)", 1, 8, valinit=3, valstep=1, valfmt="%d"
    )

    ax_radio = plt.axes([0.05, 0.12, 0.15, 0.10])
    radio_algo = RadioButtons(ax_radio, ("PSO", "Genetic"))

    ax_button = plt.axes([0.48, 0.05, 0.20, 0.05])
    button_run = Button(ax_button, "Optimize!", color="lightgreen", hovercolor="green")

    def on_optimize_clicked(event):
        button_run.label.set_text("Thinking...")
        fig.canvas.draw()
        fig.canvas.flush_events()
        run_and_draw(int(slider_m.val), radio_algo.value_selected)
        button_run.label.set_text("Optimize!")
        fig.canvas.draw_idle()

    button_run.on_clicked(on_optimize_clicked)

    run_and_draw(3, "PSO")
    plt.show()
