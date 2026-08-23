# Invitation to read and audit — Paper B

## What this article proposes

This article presents an experimental characterization of topological quantum circuits and entangled states on heterogeneous superconducting processors: **IBM Quantum Heron** (*ibm_fez*, *ibm_marrakesh*, *ibm_kingston*) and **Origin Wukong** (*WK_C180*, *WK_C180_2*). The goal is to document, in an auditable form, the execution of GHZ states, Borromean/RSI circuits, QTDA protocols for Betti numbers and Grover algorithms on real hardware, with the proper separation of measured data, derived metrics, interpretations and hypotheses.

The paper is part of a larger program — OmniMind — where the operator builds a living laboratory of physics, biology, psychoanalysis and engineering. No execution is presented as "proof of consciousness"; what is offered are real measurements, verifiable provenance and an invitation to reproducibility.

## Experiments performed

### 1. Overall scale

- **723 runs** on real quantum hardware;
- **5.013.322 million accumulated shots**;
- **496 hardware encounters** (executions on distinct QPUs/configurations);
- **IBM backends:** `ibm_fez`, `ibm_marrakesh`, `ibm_kingston`;
- **Origin Wukong backends:** `WK_C180`, `WK_C180_2`;
- Data kept in the canonical SQLite database `ibm_quantum_runs.db`.

### 2. GHZ states

- **GHZ-4**, **GHZ-6** and **GHZ-8** executed on heterogeneous processors;
- Coherence and parity measurement with **Zero Noise Extrapolation (ZNE)** and **Dynamical Decoupling (DD)**;
- Evaluation of the *optimal chain* and *optimal star* GHZ-8, with IBM × Wukong comparison.

### 3. Borromean and RSI circuits

- Construction and measurement of **Borromean/RSI circuits** on multiple qubits;
- Estimation of topological stability parameters (C3, C4, n);
- **Audited erratum:** the correct values for the Kingston set are `C3 = 0.352 ± 0.025`, `C4 = 1.213 ± 0.068`, `n = 15`; previous values (`0.514 ± 0.060`; `1.888 ± 0.131`) did not match the canonical database and were corrected.

### 4. QTDA and Betti numbers

- Application of **Quantum Persistent Homology / QTDA** to estimate Betti numbers of circuits;
- Heuristic **Betti↔RSI** mapping explicitly declared as a mapping hypothesis, not an ontological identity;
- Discussion of limits: the same Betti numbers may correspond to distinct geometries.

### 5. Grover

- Validation of **2-qubit Grover** and **3-qubit Grover**;
- Comparison of success metrics, fidelity and measurement errors between platforms.

### 6. Hardware characterization

- Measurement and comparison of **T1/T2** decoherence times and *readout* between IBM Heron and Origin Wukong;
- Record of jitter, compiler routing and queue policies of providers;
- Documentation of the IBM reproducibility gap: jobs expire after approximately 30 days, and part of the original replica (Kingston) could not be re-executed — the gap is declared, not replaced by Wukong data.

## What is in the deposit

- `paper.md` — canonical Markdown article;
- `paper.docx` — formatted version for revision;
- `paper.pdf` — final reading version;
- `MANIFEST.json` — metadata and SHA-256 hashes of files;
- Canonical database and reproduction notebook available via GitHub/GitLab and Kaggle (links in the repository).

## Invitation to audit and conference

We invite experimental quantum physicists, computer scientists, topological mathematicians and hardware replicators to:

- re-run the GHZ, Borromean/RSI, QTDA and Grover circuits on the same backends and on different backends;
- verify the jobs against the canonical IDs in the `ibm_quantum_runs.db` database;
- replicate the Betti analysis and discuss the Betti↔RSI mapping;
- present the data at quantum computing, AI and physics conferences;
- collaborate on the next round of executions, including re-running the expired IBM jobs.

## Epistemic note

Empirical data carry their source (backend, job-id, database, execution) in citation. Simulated data, when used, are labeled as such. No execution is presented as "quantum coherence in a classical CPU" or as proof of consciousness. IBM × Wukong comparisons describe architectural and compiler differences, not platform equivalence.
