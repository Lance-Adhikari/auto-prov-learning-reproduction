# Auto-Prov Learning and Reproduction

A staged exploration of Auto-Prov, a framework for turning system logs into provenance graphs and interpreting suspicious activity. This project contains architecture notes, vector experiments, and examples of provenance extraction and reusable regex rules. It is not a full reproduction of the research system.

## Contents

- [Architecture notes](stage_01_auto_prov_architecture/notes.md): How log discovery, extraction rules, graph enrichment, and threat interpretation fit together.
- [Cosine similarity example](stage_02_log_clustering/embeddings_cosine_similarity.py): Compares small vectors using dot products and vector lengths.
- [Vector comparison notes](stage_02_log_clustering/notes.md): The mathematics behind similarity and distance.

- [Greedy Farthest Point sampling](stage_02_log_clustering/greedy_farthest_point.py): Selects diverse vectors using their nearest cosine distance to the selected set. See the [sampling notes](stage_02_log_clustering/notes_stage_02b.md).

- [Simplified streaming clustering](stage_02_log_clustering/streaming_clustering.py): Groups incoming vectors by distance to cluster centers. Includes a [threshold experiment](stage_02_log_clustering/threshold_experiment_results.md).

- [Candidate provenance extraction](stage_03_candidate_provenance_extractor/notes.md): Builds structured records from sample logs.
- [Reusable extraction rules](stage_04_rule_generator/notes.md): Applies regex rules to further sample logs.

The vectors are synthetic, not real log embeddings. The clustering example is not DBStream. RoBERTa encoding and threat detection are not implemented. Provenance extraction uses deterministic parsing and supplied votes; regex rules are hand-written. The next planned stage is functional node features.

## Run

Requires Python 3.9 or later. From the project folder:

```bash
python -m pip install -r requirements.txt
python stage_02_log_clustering/embeddings_cosine_similarity.py
python stage_02_log_clustering/greedy_farthest_point.py
python stage_02_log_clustering/streaming_clustering.py
python stage_02_log_clustering/threshold_experiment.py
python stage_03_candidate_provenance_extractor/cpe_pdb.py
python stage_04_rule_generator/rule_generator.py
python stage_04_rule_generator/regex_example.py
python -m unittest discover -s tests -v
```

Parallel vectors have similarity 1 and distance 0; perpendicular vectors have similarity 0 and distance 1. Small floating point differences are normal.

Based on [the Auto-Prov paper](https://arxiv.org/abs/2603.17100). See [references](references/README.md) for attribution.
