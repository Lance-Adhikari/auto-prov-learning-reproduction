# Greedy Farthest Point Sampling

Select a diverse subset by starting with the first point, then repeatedly choosing the candidate whose nearest selected point has the greatest cosine distance.

The minimum distance matters: a candidate may be far from one selected point but almost identical to another. Taking the minimum avoids favoring that redundant candidate. Ties follow dictionary insertion order.

## Example

The script uses five synthetic vectors: A = [1, 0], B = [0.9, 0.1], C = [0, 1], D = [-1, 0], and E = [0.1, 0.9]. With k = 3:

1. A is selected first.
2. D is opposite A, so its cosine distance of 2 is the largest.
3. C has distance 1 from both A and D. B is close to A, while E has a slightly smaller minimum distance than C.

The result is `['A', 'D', 'C']`.

## Scope

This implements sampling with small example vectors, not RoBERTa log embeddings. Sampling selects examples; it does not assign log types or create clusters. Streaming log clustering is the next planned stage.
