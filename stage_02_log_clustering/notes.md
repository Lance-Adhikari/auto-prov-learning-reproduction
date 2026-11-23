# Stage 2A :  Embeddings and Cosine Similarity

## Objective

Before implementing the paper's log-sampling procedure, I needed to understand how numerical vectors can be compared.

This stage focuses on the mathematical foundation rather than attempting to reproduce the paper's full embedding model.

## 1. From Text to Numerical Representations

Clustering algorithms operate on numerical data.

A text log therefore needs a numerical representation before mathematical similarity or distance calculations can be applied to it.

A simplified example is:

```text
log text
   |
   v
embedding model
   |
   v
[0.12, 0.74, -0.31, ...]
```

The paper uses RoBERTa to encode log entries before its sampling procedure.

The small vectors in my Python exercise are **not RoBERTa embeddings**. They are intentionally simple examples used to understand the mathematics first.

## 2. Dot Product

For two vectors

```text
A = [a1, a2]
B = [b1, b2]
```

their dot product is:

```text
A . B = (a1 * b1) + (a2 * b2)
```

## 3. Vector Magnitude

For:

```text
A = [a1, a2]
```

the magnitude is:

```text
||A|| = sqrt(a1^2 + a2^2)
```

## 4. Cosine Similarity

Cosine similarity compares the directions of two vectors:

```text
cosine_similarity(A, B) =
    (A . B) / (||A|| * ||B||)
```

If two non-zero vectors point in the same direction, their cosine similarity is 1.

## 5. Cosine Distance

For this learning exercise:

```text
cosine_distance = 1 - cosine_similarity
```

Therefore, highly similar vectors have a small cosine distance.

## 6. Connection to Auto-Prov

This matters because Auto-Prov needs to select diverse log examples rather than repeatedly selecting logs that are nearly identical.

The paper encodes logs with RoBERTa and uses cosine distance during Greedy Farthest Point sampling.

So Stage 2A establishes the foundation for the next implementation:

```text
logs
  |
  v
embeddings
  |
  v
cosine distances
  |
  v
Greedy Farthest Point sampling
```

## Python Exercise

`embeddings_cosine_similarity.py` implements cosine similarity and cosine distance for small NumPy vectors.

The purpose is to understand the calculation clearly before applying the idea to a larger set of vectors.

## Status

**Completed.**

## Next

**Stage 2B: Greedy Farthest Point Sampling**

The next goal is to select a diverse subset of vectors by repeatedly considering their distances from already-selected points.
