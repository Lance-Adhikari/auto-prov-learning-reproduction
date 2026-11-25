# Simplified Streaming Clustering

This example processes synthetic vectors one at a time. Each point joins the nearest cluster if its Euclidean distance to the center is at most the threshold. Otherwise, it starts a new cluster. Joining a cluster updates its center to the mean of its points.

GFP selects a diverse subset; clustering groups similar observations. This example demonstrates grouping only. It is not DBStream and is not connected to real log embeddings or the GFP script.

The implementation retains every point, starts fresh on each call, and depends on arrival order. It does not implement density estimation, fading, or cluster merging.

Run `threshold_experiment.py` to compare three thresholds. See [results](threshold_experiment_results.md) for the observed cluster counts.

The next planned stage is the Candidate Provenance Extractor (CPE).
