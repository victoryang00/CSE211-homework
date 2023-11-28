import matplotlib.pyplot as plt


def plot_ind():
    # with chain length = 64, each point is
    # (unroll, sequential speedup, interleaved speedup)
    ind_data = [
        (1, 0.983681, 1.01779),
        (2, 1.03406, 1.50855),
        (4, 1.11598, 3.16128),
        (8, 1.03202, 3.17733),
        (16, 1.02269, 4.26913),
        (32, 0.87053, 4.22056),
        (64, 0.80699, 3.40006),
    ]

    plt.clf()

    for i, label, color in zip(
        [1, 2], ["sequential", "interleaved"], ["tab:blue", "tab:orange", "tab:green"]
    ):
        plt.plot(
            list(point[0] for point in ind_data),
            list(point[i] for point in ind_data),
            label=label,
            color=color,
            marker=".",
        )

    plt.title(
        f"Speedup of Unrolled Loops with Independent Iterations as Unroll Factor Increases",
        fontsize=10
    )
    plt.xlabel("Unroll Factor")
    plt.ylabel("Speedup")
    plt.xscale('log', base=2)
    plt.legend()

    plt.tight_layout()
    plt.savefig("ind.png")


def plot_red():
    # each point is
    # (partitions, speedup)
    red_data = [
        (1, 1.1504),
        (2, 1.93572),
        (4, 2.77385),
        (8, 2.18767),
        (16, 2.05182),
    ]

    plt.clf()

    plt.plot(
        list(point[0] for point in red_data),
        list(point[1] for point in red_data),
        marker=".",
    )

    plt.title(
        f"Speedup of Unrolled Reduction Loops as Partition Count Increases",
        fontsize=10
    )
    plt.xlabel("Partition Count / Unroll Factor")
    plt.ylabel("Speedup")
    plt.xscale('log', base=2)

    plt.tight_layout()
    plt.savefig("red.png")

plot_ind()
plot_red()
