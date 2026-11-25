"""Simplified streaming clustering with synthetic vectors, not DBStream."""

import numpy as np


def streaming_cluster(points, threshold):
    """Group equal-length finite vectors using a Euclidean distance threshold.

    Each call starts fresh. Points are processed in order and retained in memory.
    """
    if not np.isscalar(threshold) or not np.isfinite(threshold) or threshold < 0:
        raise ValueError("threshold must be a finite, nonnegative number.")
    clusters = []

    for point in points:
        point = np.array(point, dtype=float, copy=True)
        if point.ndim != 1 or point.size == 0 or not np.all(np.isfinite(point)):
            raise ValueError("Points must be finite, nonempty, one-dimensional vectors.")
        if clusters and point.shape != clusters[0]["center"].shape:
            raise ValueError("Points must have equal lengths.")
        # The first observation creates the initial cluster.
        if not clusters:
            clusters.append({
                "center": point.copy(),
                "points": [point]
            })
            continue

        distances = []

        for cluster in clusters:
            distance = np.linalg.norm(point - cluster["center"])
            distances.append(distance)

        # Compare Euclidean distances; ties choose the first cluster.
        nearest_index = np.argmin(distances)
        nearest_distance = distances[nearest_index]

        # Include points exactly on the threshold boundary.
        if nearest_distance <= threshold:
            clusters[nearest_index]["points"].append(point)

            # Recalculate the center as the mean of all assigned points.
            cluster_points = np.array(
                clusters[nearest_index]["points"]
            )

            clusters[nearest_index]["center"] = np.mean(
                cluster_points,
                axis=0
            )
        else:
            clusters.append({
                "center": point.copy(),
                "points": [point]
            })

    return clusters


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

    threshold = 0.5
    clusters = streaming_cluster(points, threshold)

    print("Threshold:", threshold)
    print("Number of clusters:", len(clusters))
    print()

    for index, cluster in enumerate(clusters):
        print("Cluster", index + 1)
        print("Center:", cluster["center"])
        print("Number of points:", len(cluster["points"]))
        print()


if __name__ == "__main__":
    main()
