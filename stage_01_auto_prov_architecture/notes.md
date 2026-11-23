# Stage 1 :  Understanding the Auto-Prov Architecture

## Objective

The goal of Stage 1 is to understand the purpose of the major Auto-Prov components before attempting to implement them.

Auto-Prov addresses a difficult problem: system logs can be heterogeneous, repetitive, unstructured, and can change over time. The framework aims to turn those logs into provenance graphs that can be enriched and analyzed for suspicious behavior.

## Pipeline I Am Studying

A simplified conceptual view is:

```text
Streaming system logs
        |
        v
Discover different log types
        |
        v
Select representative logs
        |
        v
Candidate Provenance Extractor (CPE)
        |
        v
Generate reusable extraction rules
        |
        v
Construct provenance graph
        |
        v
Add functionality information to nodes
        |
        v
Anomaly detection
        |
        v
Attack graph
        |
        v
Threat interpretation / summary
```

This diagram is my simplified learning representation of the workflow, not a reproduction of the paper's figure.

## 1. Streaming Logs

System activity can generate a very large number of log records. Many records may have the same format while the variable values: such as timestamps, identifiers, processes, or files: change.

A major challenge is therefore avoiding expensive processing of every repetitive record individually.

## 2. Finding Different Log Types

Auto-Prov first needs to discover the different formats present in the incoming logs.

The paper's approach includes:

1. processing logs in short time windows;
2. encoding logs into numerical representations;
3. sampling diverse logs;
4. clustering the sampled logs online; and
5. selecting representative logs for the discovered types.

This is the part of the framework that Stage 2 begins to study.

## 3. Candidate Provenance Extractor

After representative logs are selected, the Candidate Provenance Extractor uses a powerful LLM to infer reference provenance information.

Important information can include:

- interacting entities;
- interaction type;
- interaction direction;
- timestamp;
- entity names; and
- coarse entity types.

This connects to my earlier practice of reducing log activity to a simpler relationship such as:

```text
source -> interaction -> destination
```

The actual framework stores richer provenance information than this simplified representation.

## 4. Rule Generator

Running a large LLM on every streaming log would be computationally expensive.

Auto-Prov therefore uses the CPE's reference extractions to help generate reusable regular-expression rules. These rules can then extract provenance fields from logs of known types at scale.

The rule database can be updated when a new log type is discovered.

## 5. Functionality-Based Node Enrichment

A provenance node's coarse type may not explain what the entity actually does.

For example, two entities may both be processes while having very different functions.

Auto-Prov therefore enriches nodes with functionality information. Later stages of this project will study how known and unknown entities receive these labels.

## 6. Anomaly Detection

The enriched provenance graph can be supplied to graph-based anomaly detectors.

The objective is to identify unusual or potentially malicious nodes and interactions and connect them into attack graphs.

## 7. Graph Assistant

The final interpretation stage converts detected attack-graph activity into a form that is easier for an analyst to understand and relates suspicious activity to likely attack tactics.

## Status

**Completed for initial understanding.**

I will return to individual components in greater technical depth as I implement them.
