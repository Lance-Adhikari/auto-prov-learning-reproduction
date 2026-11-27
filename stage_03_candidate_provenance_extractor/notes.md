# Candidate Provenance Extraction

`cpe_pdb.py` parses controlled Windows-style file-access logs into eight-field provenance records. It recognizes `ReadData` and `WriteData`, uses supplied direction votes, and stores the example record in an in-memory candidate provenance database (PDB).

- `V_l`: entity ID to type.
- `N_l`: entity ID to name or path.
- `E_l`: source, destination, interaction, and time.
- `PDB`: log ID to its provenance records.

The most frequent supplied direction wins; ties use the first direction encountered. Missing fields and unsupported access types return `None`.

This is deterministic parsing with example votes, not LLM reasoning. The example expects distinct process and object IDs.
