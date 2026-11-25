"""Simplified streaming clustering with synthetic vectors, not DBStream."""

import numpy as np
# Support direct execution and imports from the project root.
if __package__:
    from .streaming_clustering import streaming_cluster
else:
    from streaming_clustering import streaming_cluster


def main():
    points = [
        np.array([1.0, 1.0]),
        np.array([1.1, 1.1]),
        np.array([0.9, 1.0]),
        np.array([5.0, 5.0]),
        np.array([5.1, 5.0]),
        np.array([9.0, 1.0]),
        np.array([9.1, 1.1])
    ]

    thresholds = [0.1, 0.5, 10.0]

    for threshold in thresholds:
        clusters = streaming_cluster(points, threshold)

        print(
            "Threshold:",
            threshold,
            "| Number of clusters:",
            len(clusters)
        )


if __name__ == "__main__":
    main()
