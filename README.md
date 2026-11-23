# Auto-Prov Learning and Reproduction

A staged exploration of Auto-Prov, a framework for turning system logs into provenance graphs and interpreting suspicious activity. This project currently contains architecture notes and a NumPy experiment for comparing vectors. It is not a full reproduction of the research system.

## Contents

- [Architecture notes](stage_01_auto_prov_architecture/notes.md): How log discovery, extraction rules, graph enrichment, and threat interpretation fit together.
- [Cosine similarity example](stage_02_log_clustering/embeddings_cosine_similarity.py): Compares small vectors using dot products and vector lengths.
- [Vector comparison notes](stage_02_log_clustering/notes.md): The mathematics behind similarity and distance.

The example vectors are synthetic, not real log embeddings. RoBERTa encoding, sampling, clustering, and threat detection are not implemented yet. The next planned step is greedy farthest point sampling.

## Run

Requires Python 3.9 or later. From the project folder:

```bash
python -m pip install -r requirements.txt
python stage_02_log_clustering/embeddings_cosine_similarity.py
python -m unittest discover -s tests -v
```

Parallel vectors have similarity 1 and distance 0; perpendicular vectors have similarity 0 and distance 1. Small floating point differences are normal.

Based on [the Auto-Prov paper](https://arxiv.org/abs/2603.17100). See [references](references/README.md) for attribution.
