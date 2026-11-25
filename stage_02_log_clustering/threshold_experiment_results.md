# Threshold Experiment Results

Observed output from `threshold_experiment.py` using the seven synthetic points in their listed order:

| Threshold | Number of clusters |
|---:|---:|
| 0.1 | 5 |
| 0.5 | 3 |
| 10.0 | 1 |

For this dataset, increasing the threshold lets more points join an existing cluster. At 0.5, the groups contain 3, 2, and 2 points. At 10.0, all seven points join one group.

A point farther than the threshold from every current center creates a new cluster, allowing distinct observations arriving later to form new groups. Results depend on input order and floating point comparisons near the threshold.

These results describe the simplified example, not DBStream or an Auto-Prov evaluation.
