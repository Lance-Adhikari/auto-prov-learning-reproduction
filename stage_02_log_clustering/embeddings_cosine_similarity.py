"""Stage 2A: Embeddings and Cosine Similarity

A small educational implementation of cosine similarity and cosine
distance. The vectors below are simple examples for learning the
mathematics; they are not real RoBERTa log embeddings.
"""

import numpy as np


def cosine_similarity(vector_a, vector_b):
    """Compare finite, nonzero, one-dimensional vectors of equal length."""
    vector_a = np.asarray(vector_a, dtype=float)
    vector_b = np.asarray(vector_b, dtype=float)
    if vector_a.ndim != 1 or vector_b.ndim != 1:
        raise ValueError("Inputs must be one-dimensional vectors.")
    if vector_a.size == 0 or vector_a.shape != vector_b.shape:
        raise ValueError("Vectors must be nonempty and have equal lengths.")
    if not np.all(np.isfinite(vector_a)) or not np.all(np.isfinite(vector_b)):
        raise ValueError("Vectors must contain only finite numbers.")

    scale_a = np.max(np.abs(vector_a))
    scale_b = np.max(np.abs(vector_b))
    if scale_a == 0 or scale_b == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector.")

    # Scaling preserves direction and avoids overflow for large coordinates.
    vector_a = vector_a / scale_a
    vector_b = vector_b / scale_b
    unit_a = vector_a / np.linalg.norm(vector_a)
    unit_b = vector_b / np.linalg.norm(vector_b)

    # Keep rounding error from producing values outside [-1, 1].
    return float(np.clip(np.dot(unit_a, unit_b), -1.0, 1.0))


def cosine_distance(vector_a, vector_b):
    """Return cosine distance as 1 - cosine similarity."""
    return 1 - cosine_similarity(vector_a, vector_b)


def main():
    # Small vectors are used so the results can also be checked by hand.
    vector_a = np.array([2.0, 3.0])
    vector_b = np.array([4.0, 6.0])
    vector_c = np.array([-3.0, 2.0])

    print("Vector A:", vector_a)
    print("Vector B:", vector_b)
    print("Vector C:", vector_c)
    print()

    print("A vs B cosine similarity:", cosine_similarity(vector_a, vector_b))
    print("A vs B cosine distance:", cosine_distance(vector_a, vector_b))
    print()

    print("A vs C cosine similarity:", cosine_similarity(vector_a, vector_c))
    print("A vs C cosine distance:", cosine_distance(vector_a, vector_c))


if __name__ == "__main__":
    main()
