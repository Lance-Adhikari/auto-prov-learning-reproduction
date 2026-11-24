"""Greedy Farthest Point sampling with synthetic vectors."""

import numpy as np

# Support both direct script execution and importing from the project root.
if __package__:
    from .embeddings_cosine_similarity import cosine_distance
else:
    from embeddings_cosine_similarity import cosine_distance


def greedy_farthest_point(points, k):
    """Select k names by maximizing distance to the nearest selected point.

    Start with the first dictionary entry and break ties in insertion order.
    """
    if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
        raise ValueError("k must be an integer.")
    names = list(points.keys())

    if k < 1:
        raise ValueError("k must be at least 1.")

    if k > len(names):
        raise ValueError("k cannot exceed the number of points.")

    # Validate every vector even when only one sample is requested.
    for name in names:
        cosine_distance(points[names[0]], points[name])

    # Use a fixed starting point so repeated runs give the same result.
    selected = [names[0]]

    while len(selected) < k:
        farthest_candidate = None
        largest_minimum_distance = -1

        for candidate in names:
            if candidate not in selected:
                distances = []

                for chosen in selected:
                    distance = cosine_distance(
                        points[candidate],
                        points[chosen]
                    )
                    distances.append(distance)

                # A candidate close to any selected point adds little diversity.
                minimum_distance = min(distances)

                print(
                    candidate,
                    "minimum distance:",
                    round(minimum_distance, 4)
                )

                # Choose the largest nearest distance; retain the first tie.
                if minimum_distance > largest_minimum_distance:
                    largest_minimum_distance = minimum_distance
                    farthest_candidate = candidate

        selected.append(farthest_candidate)
        print("Selected:", farthest_candidate)
        print("Current selected set:", selected)
        print()

    return selected


def main():
    points = {
        "A": np.array([1.0, 0.0]),
        "B": np.array([0.9, 0.1]),
        "C": np.array([0.0, 1.0]),
        "D": np.array([-1.0, 0.0]),
        "E": np.array([0.1, 0.9])
    }

    selected_points = greedy_farthest_point(points, 3)
    print("Final selected points:", selected_points)


if __name__ == "__main__":
    main()
