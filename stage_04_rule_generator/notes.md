# Reusable Extraction Rules

`rule_generator.py` applies hand-written regex rules to controlled file-access logs. The rule database (RDB) extracts IDs, names, interaction labels, and timestamps. Entity types are fixed to process and file, and access labels become `READ` or `WRITE`.

The PDB stores extracted records; the RDB stores rules for extracting fields from further logs in the same format. These scripts are independent examples: rules are not generated automatically from the PDB.

The example always uses process-to-file direction, including reads. It does not infer information-flow direction. Missing fields and unsupported access types return `None`.

`regex_example.py` shows the raw capture groups before normalization. No model-based rule induction or provenance graph construction is implemented.
