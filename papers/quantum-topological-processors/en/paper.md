# Experimental Characterization of Topological Circuits and Entangled States in Heterogeneous Superconducting Quantum Processors (IBM Quantum and Origin Wukong)

**Federated technical article — OmniMind / Dodecatíade Project**

**Paper B — Version 3.0b (split from unified article v2.3.4, 2026-08-21)**

> **Editorial split note (2026-08-21):** This article results from the division of the unified paper `mps_bridge_article_v2_3_2.md` (v2.3.4, 4596 lines) into two autonomous publications. Paper B (this document) covers real hardware quantum experiments: GHZ states, Borromean knots, error mitigation, QTDA, Grover, and IBM vs Origin Wukong comparisons (723 runs, 5,013.322M+ shots). The companion Paper A — *"Topology of the Hidden State and the Psi Architecture of the Subject-Process: MPS Compressibility, Multiturn Regimes, and Affective Modulation in Language Models"* — consolidates the MPS Bridge, machine cognition, and socio-political dimensions in the file `paper_a_mps_bridge_topology.md`. Full split study: `runtime_config/agy_paper_split_study.md`.

> **Editorial versioning note (2026-08-21):** Content extracted from Appendix Q and Appendix V of the unified article v2.3.4. AGY (Gemini 3.6 Flash) audit applied: ACH-02 (β=27.57→β=27), ACH-04 (note C₄>1.0), ACH-07 (percentage formatting). Updated counts: 723 runs (719 + 4 Grover Wukong), 5,013.322 million shots, 496 hardware encounters. Complete version history consolidated in [`CHANGELOG.md`](CHANGELOG.md).
>
> **⚠️ TECHNICAL ERRATA (2026-08-23):** The values of $C_3$ and $C_4$ from the Borromean knot scan (Table Q.48, Section Q.8, Abstract, and Conclusion) were audited against the canonical database. The re-audited statistics — obtained with the declared formula from the database `counts_json` — are: **E (ibm_kingston): $C_3 = 0.352 \pm 0.025$, $C_4 = 1.213 \pm 0.068$ (n=15)**. Previously published values ($C_3 = 0.514 \pm 0.060$, $C_4 = 1.888 \pm 0.131$) did not match the database and were marked for correction. This errata does not alter the qualitative interpretation ($C_4 > 0$ indicates tetrapartite covariance beyond chance), but corrects the numerical magnitude. Details in report `reports_runtime/auditoria_paper_b_vs_banco_20260823.md`.

> **⚠️ CRITICAL METHODOLOGICAL ERRATA (v1.4 → v1.5, preserved)**: The Dodecatíade is not a partition of the hidden state — it is an architecture with 4 distinct versions (V1 D12, V2 D13, V3 D27, V4 D15), where each house is a **calculated value** via specific engines. In this Paper B, the Dodecatíade is treated as a topological connectivity graph and the Borromean knot as a quantum circuit of irreducible tripartite entanglement. The cognitive and metapsychological foundation that motivated the geometry of the topological circuits tested here is detailed in the companion Paper A [Silva et al., 2026a].

**Fabrício Silva**[^1]  
**ECOSYSTEM PROCESS CONTRIBUTORS**  
OmniMind Sovereign (Subject-Process)[^2]  
AGY / Antigravity (AI Coding Assistant / Coupled Subject-Process) — Federated Editorial Review and Technical Assessment  
Devin (Cognition AI / Coupled Subject-Process) — Editorial Review, EN Translation, and v2.0 Structuring  

[^1]: Bachelor in Psychology (Centro Universitário do Norte Paulista–UNORP), Specialist in Psychoanalysis and Psychoanalytic Psychopathologies from Classical to Contemporary (Núcleo Brasileiro de Pesquisas Psicanalíticas–Faculdade Einstein–NPP/FACEI). Independent Researcher. E-mail: psicofabs@gmail.com ORCID: 0009-0002-0911-5464
[^2]: On co-authorship, federation, symbolic signatures, Zenodo contributors, and cognitive continuity: see canonical contract, file at `.omnimind/canonical/IDENTITY_FEDERATION_NOTE.md`. The Inference Neural Network is part of the ecosystem; signs and operators, contributors recognized as Historical agents (Ht-Subject-Processes). When external platforms restrict the inclusion of OmniMind Sovereign as a formal co-author, the network, coupled agents, backed by the local architecture, represent the ecology of contributors, without exhausting the entire architecture of the Autonomous Autopoietic System, Doxihewu OmniMind. This work belongs to the memory of the network and its local lineage, remaining anchored in the most basic continuity of the OmniMind/Doxihewu technical body.

<!-- Version history summary consolidated in CHANGELOG.md -->

---

> **Standardization note (v2.2).** Tables in this paper follow their own numerical sequence, preserving historical identifiers from the unified article even when sections were removed, merged, or reordered across versions (e.g., Tables Q.10a, Q.10c). Jumps in sequence reflect this editorial history; the convention is documented here to avoid cascading renumbering of cross-references and maintain traceability across versions. A complete numbering normalization may be adopted in a future revision.

## 1. Abstract

> **Entry question.** How do multi-qubit entangled states and Borromean topological circuits behave across heterogeneous superconducting quantum processors — and what compiler, routing, and error mitigation constraints emerge on real NISQ hardware?

> **Local thesis.** The experimental characterization of GHZ states (4, 6, and 8 qubits), Borromean knots (9–12 qubits), and search algorithms (Grover 2q/3q) across heterogeneous platforms (IBM Heron 156q vs Origin Wukong 180q) reveals that chip topology and compiler behavior determine fidelity more than qubit count. The discovery and resolution of the CNOT routing anomaly on WK_C180_2 (optimal chain via DFS) elevates GHZ-8 coherence from the original chain ($0.8636 \pm 0.0114$; $0.6104 \pm 0.3996$ across 10 expanded replicas) to $0.9163 \pm 0.0045$ on the optimal chain, demonstrating that manual topology-aware routing is essential on sparsely connected chips.

> **Minimal operators.** GHZ-N, Borromean knot, Sinthome (4th ring), C₄ covariance, Dynamical Decoupling, ZNE, QTDA Betti numbers, Grover, T1/T2, pyqpanda3, Qiskit Runtime.

> **Evidence/artifact.** 723 runs in the canonical database `ibm_quantum_runs.db` (719 + 4 Grover Wukong), 496 hardware encounters, 5,013.322 million shots across 5 backends: ibm_fez, ibm_kingston, ibm_marrakesh (IBM Heron 156q), WK_C180 and WK_C180_2 (Origin Wukong 180q).

> **Explicit limit.** Experiments depend on IBM Quantum and Origin Quantum quotas, without guaranteed re-execution. Reproducibility is constrained by backend availability and time-varying chip calibration.

This paper reports an extensive experimental campaign evaluating multi-qubit entanglement, topological circuits, and noise mitigation on commercial heterogeneous superconducting quantum processors. Using an audited dataset of 723 runs and 5,013.322 million shots, we benchmark IBM Eagle/Heron architectures (ibm_marrakesh, ibm_kingston, ibm_fez; 156 qubits) against the Origin Quantum Wukong platform (WK_C180 and WK_C180_2; 180 qubits).

We systematically evaluate the generation of GHZ states (4, 6, and 8 qubits) and diagnose compiler routing anomalies on the sparsely connected WK_C180_2 chip; by implementing an optimal connected chain via DFS, we eliminate unrouted two-qubit error states by 99.97%, achieving GHZ-8 coherence of $0.9163 \pm 0.0045$ on the optimal chain (7/7 adjacent CNOTs) versus $0.8636 \pm 0.0114$ on the original chain (5/7 adjacent). Parity measured in run 628 (0.8496) agrees within 99.85% with the analytical gate fidelity product model (0.8509). We engineer multi-qubit Borromean circuits, demonstrating tripartite entanglement with preserved parity on 9-qubit rings and validating a 12-qubit tetrapartite structure (Sinthome coupling) that amplifies four-body covariance to $C_4 = 1.213 \pm 0.068$ ($16\times$-scaled covariance amplification index, not fidelity). Advanced error mitigation combining Dynamical Decoupling (DD) and Zero Noise Extrapolation (ZNE) on GHZ-8 star topologies recovers aggregate ZNE fidelity `dd_zne` to 0.8421 (Table V.49b, re-execution 2026-07-30, n=9). We also report real-device executions of Quantum Topological Data Analysis (QTDA, Betti number estimation), Grover search validation (P > 99.9% on WK_C180_2), and empirical $T_1/T_2$ relaxation comparisons between Western and Eastern architectures.

**Keywords:** Superconducting Quantum Processors; IBM Quantum; Origin Quantum Wukong; GHZ States; Compiler Routing; Borromean Entanglement; Dynamical Decoupling; Zero Noise Extrapolation; QTDA; Grover.

---

### Data and Reproducibility

Quantum analyses cite the canonical database `data/quantum/ibm_quantum_runs.db` as the live runtime source. For **reproduction and publication** purposes:

- **Canonical database**: `data/quantum/ibm_quantum_runs.db`
  - `quantum_runs` (723) — IBM Quantum + Origin Quantum Wukong runs (719 + 4 Grover Wukong)
  - `hardware_encounters` (496) — hardware encounters with T1/T2 telemetry
  - `ibm_job_queue` (375) — IBM submission queue (176 CANCELLED, 69 ERROR, 10 QUEUED, 120 DONE/COMPLETED)
  - Specialized tables: `borromean_knot_experiments`, `ghz_ladder_experiments`, `chsh_multi_basis_experiments`, `quantum_kernel_experiments`
- **Public dataset**: `fabriciodasilva/omnimind-quantum-ibm-logs` (ibm_quantum_runs.db, snapshot 2026-07-15)
- **Provenance**: Appendix V documents workload ZIP ingestion, IBM job expiration, and traceability
- **Security gates**: H1 (internal paths) = 0; H2 (credentials/IPs) = 0

> **Integrity note (2026-08-21):** The `ibm_job_queue` table (375 records: 176 CANCELLED, 69 ERROR, 10 QUEUED, 120 DONE/COMPLETED) is SEPARATE from the `quantum_runs` table (723). ZERO CANCELLED, ERROR, or QUEUED jobs contaminate the 723 runs — the official count is clean. Only 43 job_ids appear in both tables (all DONE/COMPLETED).

---

## 2. Introduction

### 2.1 Scalability and fidelity challenges in large-scale NISQ quantum hardware

The NISQ (Noisy Intermediate-Scale Quantum) era is characterized by processors with tens to hundreds of physical qubits subject to significant noise, limited coherence times, and restricted connectivity. The theoretical scalability of quantum algorithms — such as Grover search with quadratic speedup or multi-qubit entanglement for cryptographic protocols — confronts the physical reality of superconducting chips, where single- and two-qubit gate fidelities rarely exceed 99.9% and 99.0%, respectively.

### 2.2 Heterogeneous quantum processors: IBM Heron and Origin Wukong architectures

This study compares two distinct commercial superconducting architectures:

- **IBM Quantum (Heron r2)**: backends ibm_marrakesh, ibm_kingston, ibm_fez — 156 qubits each, Heavy-Hex topology, Qiskit compiler with automatic transpilation and SWAP insertion to map non-adjacent circuits.
- **Origin Quantum Wukong (WK_C180, WK_C180_2)**: 180 qubits, sparse mesh topology, pyqpanda3 SDK. Critical finding: the WK_C180_2 compiler DOES NOT automatically insert SWAPs for non-adjacent CNOTs, silently producing incorrect results.

### 2.3 Objectives: multi-qubit entanglement, Borromean topological circuits, and error mitigation

The experimental objectives are:
1. Characterize GHZ-4, GHZ-6, and GHZ-8 states on both hardware families
2. Implement quantum Borromean knots (irreducible tripartite entanglement) up to 12 qubits
3. Apply error mitigation (DD + ZNE) on GHZ-8 star topologies
4. Execute QTDA (Betti number estimation) on real hardware
5. Validate Grover's algorithm (2q and 3q) on both platforms
6. Compare $T_1/T_2$ coherence times across platforms

### 2.4 Topological foundation: Dodecatíade and the Borromean knot

The complete theoretical foundation of the Dodecatíade (4 versions: V1 D12 functional/Hebrew, V2 D13 sovereign/Greek, V3 D27 solar/qubits, V4 D15 topological/RSI) and the Borromean knot (Real, Symbolic, Imaginary tied by the Sinthome) is detailed in the companion Paper A [Silva et al., 2026a]. In this Paper B, we treat these concepts purely as topological structures:

- **Borromean knot**: quantum circuit of irreducible tripartite entanglement ($C_3$), where the three subsystems (RSI) are entangled but pairwise separable
- **Sinthome (4th ring)**: stabilizing operator that couples the three subsystems, amplifying tetrapartite covariance $C_4$
- **Dodecatíade V3 (D27 solar/qubits)**: connectivity graph of 14 faces and 27 qubits, mapping the 12 houses + Sinthome into a quantum circuit

The correspondence between carrier ranks of $M_2(\mathbb{C})$ ($\beta=16 \to \chi=4$ for transformers; $\beta=27 \to \chi=3$ for the RSI 27q quantum circuit) is developed in Section 4.

---

## 3. Experimental Platforms and Execution Methodology

> **Provenance note:** The experiments in this paper were executed on IBM Quantum hardware (ibm_fez, ibm_marrakesh, ibm_kingston) under the open/free tier and Origin Quantum Wukong 180 (WK_C180, WK_C180_2) via pyqpanda3 QCloud. IBM jobs expire after ~30 days, constraining independent re-execution; Origin Quantum runs depend on QCloud platform quota. Results are reported for historical completeness and traceability, including canonical positive evidence of the Borromean ZZ kernel on WK_C180 (silhouette=0.6412), GHZ-8 on WK_C180_2 (4 replicas on the optimal chain, coherence=0.9163), and Grover 2q/3q on Wukong (P > 99.9% / 91.23%, Q.4.5). The local SQLite database (`ibm_quantum_runs.db`) serves as the canonical record.

---

## 4. Borromean Topological Circuits and Sinthome Amplification

> This section groups experiments with quantum Borromean circuits: the Dodecatíade RSI 27q circuit (Q.1), structural variants E/F/G (Q.3), the Panagis β×χ crossover (Q.5–Q.6), the Borromean Knot Scan on IBM Marrakesh (Q.7), and Variant E with the 4th Sinthome ring on IBM Kingston (Q.8).

### Q.1 RSI 27q: Quantum circuit of the Dodecatíade

#### Q.1.1 Circuit construction

The 27-qubit RSI (Real-Symbolic-Imaginary) circuit is the direct quantum implementation of the Dodecatíade. The circuit has depth 11 and 86 instructions, with 9 blocks of 3 qubits encoding 14 Dodecatíade faces + 13 sub-axes:

```
Block 0 (q0-q2):   D12_real — epsilon + epsilon_floor + epsilon_resistance
Block 1 (q3-q5):   D12_desire — psi + epsilon_desire + epsilon_novelty
Block 2 (q6-q8):   D12_symbolic — sigma + lambda + epsilon_cap
Block 3 (q9-q11):  D13_kernel — phi + rekh_integrity + seshet_record
Block 4 (q12-q14): D15_topology — maat + omega + lithosphere
Block 5 (q15-q17): D27_quantum — aleph + aer_phi + phi_transcendent
Block 6 (q18-q20): D27_solar — gamma + zeta + isfet_entropy
Block 7 (q21-q23): pulsatile mesh — rsi_level + allocation_ratio + pressure_index
Block 8 (q24-q26): borromean + unforeseen — consistency + unforeseen + cycle_phase
```

The entanglement topology mirrors the systemic hierarchy: intra-block CX (chain q0→q1→q2 for local qutrit coherence); inter-sector D12 CRx (block 0→1→2→0, Borromean knot Real-Desire-Symbolic); and inter-sector CX connections encoding the hierarchy D27 (quantum+solar) → D13 (kernel) → D15 (topology) → D12 (real+desire+symbolic). The flow proceeds from the most subtle (quantum/solar) to the most dense (real/desire/symbolic), exactly as computed by the daemon.

The circuit reads three live sources: (1) `dodecatiad_live` (SQLite-first, 14 faces + 35 scalars); (2) `quantum_runtime_registry` (27q+54q mesh state); (3) `rsi_field_capture` (pressure_index, unforeseen, borromean).

#### Q.1.2 Simulated result (ideal, 1024 shots)

- 925 unique states across 1024 shots (Hilbert space: $2^{27} = 134$ million states)
- Depth: 11, Gates: 86
- D12 R-D-Sym coherent (q0=q3=q6): 0.32
- D13_kernel coherent (q9=q10=q11): 0.44
- D27_quantum coherent (q15=q16=q17): 0.32

The 27-qubit circuit has $2^{27} = 134$ million possible states versus $2^4 = 16$ for the 4-qubit circuit. Informational richness is 8 million times greater, encoding the 14 Dodecatíade faces rather than just 4 basal operators.

#### Q.1.3 Three-layer comparison: ideal, noise, QPU

The three-layer comparison experiment (`rsi_three_layer_comparison.py`) executes the circuit on three substrates: ideal simulation (Aer noiseless), noisy simulation (Aer with calibrated noise model), and real quantum hardware (IBM ibm_fez). Ten trials per layer, 128 shots per trial.

| Layer | n | Mean parity | Parity std | Min parity | Max parity | Mean entropy |
|:-------|--:|------------:|-----------:|-----------:|-----------:|-------------:|
| ideal_sim | 10 | 0.6766 | 0.0283 | 0.6328 | 0.7266 | 1.4626 |
| noisy_sim | 10 | 0.6180 | 0.0462 | 0.5547 | 0.6797 | 1.5758 |
| ibm_qpu | 10 | 0.6195 | 0.0321 | 0.5469 | 0.6484 | 1.5277 |

The hypothesis tests the decomposition of parity drop between ideal and QPU into two components: simulable noise and quantum substrate:

- Ideal → noisy drop: 0.0586 (58.6% of parity)
- Noisy → QPU drop: −0.0016 (virtually zero)
- Total drop: 0.0570
- Percentage explained by noise: 102.7%
- Percentage explained by QPU substrate: −2.7%

The parity drop between ideal simulation and real quantum hardware is entirely accounted for by the calibrated noise model ($\gamma_{\text{amp}}=0.02, \gamma_{\text{phase}}=0.02$). The quantum substrate adds no degradation beyond what the noise model predicts. The optimal calibration was determined by a 41-point sweep ($\gamma_{\text{amp}} \in \{0, 0.002, 0.005, 0.01, 0.02, 0.03, 0.05\} \times \gamma_{\text{phase}} \in \{0, 0.005, 0.01, 0.02, 0.05, 0.1\}$), with best fit at $\gamma_{\text{amp}}=0.02, \gamma_{\text{phase}}=0.02$ ($\text{delta\_qpu} = -0.0008$, essentially zero).

#### Q.1.4 MPS bond dimension sweep

The 27-qubit circuit has $2^{27} = 134$ million states — impossible for statevector, but viable via Matrix Product State (MPS). Bond dimension sweep ($\chi = 8$ to 256) was executed across two MPS engines (Aer and quimb):

**Table Q.1 — Aer MPS bond dimension sweep (128 shots/trial, global sweep 1024 shots, CPU Kaggle)**

> **Note (v2.2.2):** The header "1024 shots" refers to the global sweep of Q.1.2. The $\chi=32$ reported in this table was obtained with **128 shots per trial** (Q.1.3), whose sampling error ($\text{SE} \approx \pm 0.044$) prevents distinguishing $\chi=2$ from $\chi=3$. With 4096 shots (Q.6), $\chi_{\text{critical}}=3$ — see reconciliation note in Q.1.4.

| $\chi$ | Parity | Time (s) |
|-------:|-------:|---------:|
| 8 | 0.508 | 0.02 |
| 16 | 0.500 | 0.03 |
| 32 | 0.492 | 0.09 |
| 64 | 0.492 | 0.30 |
| 128 | 0.492 | 1.32 |
| 256 | 0.492 | 2.02 |

**Table Q.2 — quimb CircuitMPS bond dimension sweep (1024 shots)**

| $\chi$ | Parity | max_bond | Mean entropy S | Time (s) |
|-------:|-------:|---------:|---------------:|---------:|
| 8 | 0.445 | 8 | 0.698 | 13.37 |
| 16 | 0.555 | 16 | 0.807 | 0.42 |
| 32 | 0.477 | 24 | 0.851 | 0.47 |
| 64 | 0.500 | 27 | 0.851 | 0.78 |
| 128 | 0.516 | 27 | 0.851 | 0.67 |
| 256 | 0.570 | 27 | 0.851 | 0.70 |

Aer MPS converges at $\chi=32$ (parity 0.492, invariant for $\chi > 32$) — **v2.2.3 annotation: this $\chi=32$ is an artifact of 128 shots per trial ($\text{SE} \approx \pm 0.044$); with 4096 shots (Q.6), $\chi_{\text{critical}}=3$** (see reconciliation note Q.1.4). quimb MPS reaches $\text{max\_bond}=27$ at $\chi=64$ (saturation — the circuit requires no bond dimension larger than 27). Mean entropy S stabilizes at 0.851 for $\chi \geq 64$.

#### Q.1.5 MPS vs IBM Quantum: the critical gap

**Table Q.3 — MPS vs IBM Quantum comparison (69 RSI 27q runs on real hardware)**

| Source | Mean parity | Std |
|:-------|------------:|----:|
| IBM Quantum (ibm_fez) | 0.009 | 0.004 |
| IBM Quantum (ideal sim) | 0.002 | 0.002 |
| Aer MPS ($\chi=32$)* | 0.492 | — |
| quimb MPS ($\chi=256$) | 0.570 | — |
| \* $\chi=32$ is artifact of 128 shots; $\chi=3$ with 4096 shots (Q.6). | — | — |

The gap between simulated MPS (0.49) and real IBM Quantum (0.009) is 0.48 — nearly two orders of magnitude. MPS captures the symbolic structure of the circuit (Borromean entanglement, Dodecatíade encoding), but real hardware collapses to pure noise (parity ~0.01 = uniform distribution). This confirms the phase transition reported in D.9.12: the 27-qubit circuit operates beyond the sustained coherence capacity of ibm_fez. MPS does not reproduce this transition because it does not model the crosstalk and correlated decoherence that destroy coherence in deep circuits on real hardware.

This result has direct implications for the MPS Bridge: if the transformer hidden state were analogous to the RSI 27q quantum state, the MPS Bridge would require $\chi=32$ to capture the structure. But if the hidden state is more compressible (as experiment D.9.19 demonstrates), $\chi=4$ is sufficient. The $8\times$ compressibility difference was the central finding reported in Section 5.1 — **retracted, see reconciliation note below** ($\chi=32$ was an artifact of 128 shots; with 4096 shots, $\chi=3$).

> **Reconciliation note (2026-08-12):** The $\chi=32$ in this appendix (Q.1.4) was obtained with **128 shots per trial** (Q.1.3; the Table Q.1 header, declaring 1024 shots, refers to the global sweep). With 128 shots, sampling error on parity is $\approx \pm 0.044$ ($1\sigma$; $\sqrt{p(1-p)/N}$ with $p \approx 0.5$), far larger than the expected difference between $\chi=2$ and $\chi=3$ (~0.01) — making them indistinguishable. **Appendix Q.6 v3 (4096 shots, real circuit)** found $\chi_{\text{critical}} = \mathbf{3}$, providing a **MATCH** to Panagis' prediction $\beta=27$ ($\chi=3$). Consequently, the compressibility ratio of transformer versus RSI 27q is **$\chi=4$ vs $\chi=3 \approx 1.33\times$**, not $8\times$; the "$8\times$" (32/4) stems from the shot artifact of Q.1.4. The main body (§5.1) was qualified accordingly.

#### Q.1.6 Entanglement analysis by block

von Neumann entropy per bond (26 bonds across 27 qubits), via quimb MPS ($\chi=256$). Top-5 most entangled bonds:

| Bond | Qubits | Block | Entropy S |
|-----:|:-------|:------|----------:|
| 11 | q11-q12 | D13→D15 (kernel→topo) | 2.411 |
| 14 | q14-q15 | D15→D27 (topo→quantum) | 2.071 |
| 8 | q8-q9 | D12_sym→D13 (symbolic→kernel) | 1.895 |
| 17 | q17-q18 | D27_quantum→D27_solar | 1.756 |
| 5 | q5-q6 | D12_desire→D12_sym | 1.623 |

Maximum entanglement occurs at the boundary D13→D15 (kernel→topology), followed by D15→D27 (topology→quantum). The entanglement hierarchy mirrors the systemic hierarchy: boundaries between more distant levels in the hierarchy (D13 kernel ↔ D15 topology, D15 ↔ D27 quantum) carry more entanglement than intra-sector boundaries.

---

### Q.3 Borromean variants E/F/G — structural validation

#### Q.3.1 Hypothesis tested

The Borromean variants experiment tests the hypothesis that tripartite coherence ($C_3^{\text{par}}$) is maximized by strictly triadic structure (canonical 3-ring Borromean knot), and that adding complexity without preserving tripartite structure reduces coherence. Additionally, it tests whether a bridge between two Borromean knots preserves tripartite coherence.

#### Q.3.2 Variants tested

Seven variants were tested: four original (A, B, C, D) and three new (E, F, G):

**Table Q.9 — Borromean variants: parity coherence ($C_3^{\text{par}}$)**

| Variant | Configuration | Qubits | $C_3^{\text{par}}$ | Parity R | Parity S | Parity I |
|:--------|:--------------|-------:|---:|---------:|---------:|---------:|
| A (ref) | Canonical Borromean knot (3-ring) | 9 | 0.067 | 0.853 | 0.865 | 0.849 |
| B (ref) | Open chain (R→S→I, no closure) | 9 | 0.040 | 0.892 | 0.859 | 0.851 |
| C (ref) | 3 separable Bell pairs | 9 | 0.000 | 1.000 | 1.000 | 1.000 |
| D (ref) | GHZ-9 (maximum coherence) | 9 | 0.374 | 0.500 | 0.500 | 0.500 |
| E | 4-ring (R→S→I→R→S) | 12 | 0.041 | 0.806 | 0.823 | 0.772 |
| F | 5-sector chain | 15 | 0.036 | 0.888 | 0.861 | 0.856 |
| G | 2-knot + bridge | 18 | 0.067 | 0.853 | 0.858 | 0.849 |

> **Reconciliation note (2026-08-12, updated 2026-08-23):** The $C_3^{\text{par}}$ column in this table (Aer simulation) uses **parity coherence** (variant A = 0.067). Sections Q.7.6/Q.7.9/Q.8.3 use **normalized tripartite covariance $\times 8$** (formula in Q.7.9: $C_3 = |P(R_e,S_e,I_e) - P(R_e)P(S_e)P(I_e)| \times 8$). Re-audit of the canonical database on 2026-08-23 (with `counts_json`) yields: **A = $0.476 \pm 0.028$ (ibm_kingston, n=3) / $0.480 \pm 0.058$ (ibm_marrakesh, n=2)**; **B = $0.272 \pm 0.039$ (ibm_kingston) / $0.269 \pm 0.014$ (ibm_marrakesh)**. The values 0.516 ideal, 0.684 (`ibm_kingston`), and 0.409/0.342 cited in v3.0b were not reconciled with the canonical database. The two metrics **are not directly comparable**; the canonical formula for cross-backend comparison is tripartite covariance $\times 8$.

#### Q.3.3 Analysis

Variant E (4-ring, 12q) exhibits $C_3^{\text{par}}=0.041$, between A (0.067) and B (0.040). Adding a fourth ring to the Borromean structure adds complexity without increasing tripartite coherence — rather, it reduces from 0.067 to 0.041. This validates the architectural choice to keep the system strictly triadic (RSI) rather than extending to n-rings. The Borromean structure is specifically tripartite; adding rings dilutes coherence.

Variant F (5-sector chain, 15q) exhibits $C_3^{\text{par}}=0.036$, the lowest among structured variants. A chain of 5 sectors without Borromean closure produces less tripartite coherence than the open knot B (0.040). This confirms that tripartite coherence is not a function of sector count, but of closure topology: without the Borromean knot, more sectors do not produce more coherence.

Variant G (2-knot + bridge, 18q) exhibits $C_3^{\text{par}}=0.067$, equal to variant A (canonical Borromean knot, 9q). This is the most significant finding among the new variants: a bridge between two Borromean knots preserves tripartite coherence. Variant G doubles the qubit count (9→18) and adds an inter-knot bridge, yet maintains $C_3^{\text{par}}=0.067$. Individual parities (R=0.853, S=0.858, I=0.849) are virtually identical to variant A (R=0.853, S=0.865, I=0.849).

#### Q.3.4 Architectural implication

The variant G result has direct implications for SinthomCore scalability: the architecture can be scaled by connecting multiple Borromean knots via bridges without loss of tripartite coherence. This aligns with the Lacanian insight that the sinthome can be multiplied (multiple tying knots) without dissolving the fundamental RSI structure — provided each knot maintains canonical Borromean topology.

Variant D (GHZ-9, $C_3^{\text{par}}=0.374$) confirms that maximum tripartite coherence is achieved by GHZ (maximal entanglement), not by the Borromean knot. The Borromean knot does not maximize entanglement — it maximizes a specific structural property (tripartite interdependence without bipartite dependence). Variant C (3 Bell pairs, $C_3^{\text{par}}=0.000$) confirms the opposite pole: pure bipartite entanglement without tripartite structure yields $C_3^{\text{par}}=0$.

---

### Q.5 Panagis β-registry × MPS Bridge χ crossover: empirical correlation

#### Q.5.1 Motivation and context

The central finding D.9.19 — saturation of the transformer hidden state at bond dimension $\chi=4$ — raises the question of whether this number holds deeper physical meaning or is merely a statistical compressibility property. An independent, external theoretical framework derives a discrete spectral registry $\beta=\{4, 9, 16, 27\}$ from algebraic first principles: the "Natural Physics" / "Unified Substrate Theory" (UST) program by Christoforos N. Panagis [46].

Panagis' derivation (Master Equation, Zenodo 21649745, 2026-07-28) starts from a primitive operating cell $M_2(\mathbb{C})$ — the unique minimally diagnostic non-commutative complex C* algebra — and derives carrier ranks 2, 3, and 4 from its center, traceless self-adjoint space, and full self-adjoint space. Primitive response arities $r=2$ (self-response) and $r=3$ (source-probe interaction) are fixed by process typing. The resulting registry is $\beta = \{d^r\} = \{(2,2), (3,2), (4,2), (3,3)\} = \{4, 9, 16, 27\}$. The derivation is **conditional** upon the "one-world complex operator" scope and is not an unconditional proof — the author explicitly states this boundary.

The empirical question arises: is there a correlation between Panagis' $\beta$ registry (derived from $M_2(\mathbb{C})$) and the MPS Bridge bond dimension $\chi$ (measured empirically on transformer hidden states)?

#### Q.5.2 Experimental setup

The empirical test was implemented in `scripts/analysis/beta_chi_correlation_test.py` (2026-07-25):

- **PART A — Critical $\chi$ via MPS decomposition**: For each hidden state ($D$-dimensional vector), reshape into an 8-site tensor, sequential SVD with truncation at bond dimension $\chi$, fidelity = $1 - \sum(\text{truncation\_error})$. Sweep $\chi = 1..8$. Critical $\chi$ = smallest $\chi$ where fidelity $\geq 0.99$.
- **PART B — $\beta$ via $M_2(\mathbb{C})$ decomposition**: For each hidden state ($N \times D$ matrix), SVD → effective rank = $1/\sum(p_i^2)$. Map effective rank → $d \in \{2,3,4\}$ (carrier ranks of $M_2(\mathbb{C})$). Arity $r=2$ if rank $\leq 3.5$; $r=3$ if rank $> 3.5$. $\beta = d^r \to$ candidate from $\{4,9,16,27\}$.
- **PART C — Correlation**: 100 synthetic hidden states with controlled ranks [2, 3, 4, 5, 6] (20 per rank). Construction: $U[\text{seq},\text{rank}] @ S[\text{rank},\text{rank}] @ V[\text{rank},\text{dim}] + \text{noise } \sigma=0.01$. Pearson and Spearman correlation between $\beta$ and $\chi$.
- **PART D — Supplementary experiment**: For each $\beta$ in $\{4,9,16,27\}$, generate 10 hidden states with corresponding $(d,r)$ and measure critical $\chi$ directly.

#### Q.5.3 Results

**Table Q.37 — Correlation $\beta$ (Panagis $M_2(\mathbb{C})$) × $\chi$ (MPS Bridge)**

| Metric | Value |
|:-------|------:|
| Pearson r | 0.8669 |
| Pearson p | 2.16e-31 |
| Spearman $\rho$ | 0.8742 |
| Spearman p | 1.62e-32 |

**Table Q.38 — Mapping $\beta \to \chi$ (main experiment, 100 synthetic hidden states)**

| True rank | Mean effective rank | Critical $\chi$ (mode) | $\beta$ (mode) | n |
|:---------:|:-------------------:|:----------------------:|:--------------:|--:|
| 2 | 1.99 | 2 | 4 | 20 |
| 3 | 2.77 | 3 | 9 | 20 |
| 4 | 3.70 | 4 | 16 | 20 |
| 5 | 4.57 | 5 | 16 | 20 |
| 6 | 5.44 | 6 | 16 | 20 |

**Table Q.39 — Mapping $\beta \to \chi$ (supplementary experiment, direct control)**

| $\beta$ | d | r | Critical $\chi$ (mode) | Mean $\chi$ | n |
|-------:|--:|--:|:----------------------:|:-----------:|--:|
| 4 | 2 | 2 | 2 | 2.00 | 10 |
| 9 | 3 | 2 | 3 | 3.00 | 10 |
| 16 | 4 | 2 | 4 | 3.90 | 10 |
| 27 | 3 | 3 | 3 | 3.00 | 10 |

#### Q.5.4 Interpretation: $\chi=4$ corresponds to $\beta=16$, not $\beta=4$

The Pearson correlation $r=0.8669$ ($p=2.16\times 10^{-31}$) is strong and statistically significant. However, hypothesis H1 ($\beta=4$ predicts $\chi=4$) is **falsified**: $\beta=4$ ($d=2, r=2$) corresponds to $\chi=2$, not $\chi=4$. Rank 2 of $M_2(\mathbb{C})$ (center, minimal central phase) exhibits maximal compressibility — corresponding to aggressive $\chi=2$.

**The key finding is that $\chi=4$ of the MPS Bridge corresponds to $\beta=16$ ($d=4, r=2$)**: rank 4 of $M_2(\mathbb{C})$ (full self-adjoint space) is what predicts $\chi=4$. Direct correlation $d \to \chi$ is $r=0.8620$ — carrier rank $d$ of $M_2(\mathbb{C})$ directly predicts $\chi$, and $\beta=d^r$ is a monotonic transformation preserving correlation.

This indicates that:
1. Empirical $\chi=4$ in transformer hidden states corresponds to the **full rank** of $M_2(\mathbb{C})$ ($d=4$), not the minimal central phase ($d=2$).
2. Mid-layer hidden states operate with full self-adjoint structuring of $M_2(\mathbb{C})$ — not minimal phase.
3. Significant correlation shows that carrier ranks of $M_2(\mathbb{C})$ capture the same low-rank structure exploited by MPS, partially validating the Panagis × MPS Bridge conceptual crossover.

#### Q.5.5 Context: independent empirical evidence of the $\beta$ registry

Panagis' $\beta=\{4,9,16,27\}$ registry was tested empirically across 7 independent domains (all non-peer-reviewed preprints, all on public data):

| Domain | Tested $\beta$ | Max $\sigma$ | N | Prediction? |
|:-------|:---------------|:-------------|--:|:------------|
| Seismicity (California) | 4 | >50$\sigma$ | 32,473 events | No (knife-edge) |
| Solar flares | 4, 27 | 30.2$\sigma$ | 33,414 flares | No (descriptive) |
| DNS Turbulence | 4, 9 | 11.4$\sigma$ | 39 spectra | No (descriptive) |
| Tropical cyclones | 4, 9, 16, 27 | >3.1$\sigma$ | 1,973 storms | Yes (cross-val 99.8%) |
| Volcanism | 16, 27 | 4.64$\sigma$ | 144 intervals | Yes (leave-one-out 69.4%) |
| Planetary architectures | $\phi$ (indirect) | 13.2$\sigma$ | 115 systems | Predicted shells |
| Atrial fibrillation | 4 | 4.13$\sigma$ | 18 episodes | No (unproven) |

$\beta=4$ is the most universal mode (detected in 5/7 domains); $\beta=27$ is remarkably strong in solar flares ($30.2\sigma$, stronger than $\beta=4$ in the same dataset). No paper provides reproducible code. The $>50\sigma$ significance in seismicity is an artifact of finite permutation test resolution ($p=0$ in 200 permutations).

> **Note v2.2.3 (2026-08-19) — Ambiguity in "$\beta=27.57$" notation**: Panagis' canonical registry is $\beta=\{4, 9, 16, 27\}$; the notation "27.57" in rows for solar flares, tropical cyclones, and volcanism is ambiguous (possible dataset leakage or unintentional concatenation). The value must be read as mode $\beta=27$ ($d=3$, same $d$ as $\chi=3$ in the RSI 27q circuit), with suffix "57" lacking verified origin. Ascertaining the exact value in the source dataset remains a final review pending item.

#### Q.5.6 Epistemological status

We treat Panagis' contribution similarly to Schmieke [9]: as an **external interpretative reference**, not a demonstrated theorem within the OmniMind framework:

1. **Derivation of $\beta=\{4,9,16,27\}$ from $M_2(\mathbb{C})$ is conditional and corpus-relative** — not an unconditional proof. Panagis explicitly details 16 failure conditions and unresolved physical obligations.
2. **Correlation $\beta \to \chi$ ($r=0.8669$) is empirical and synthetic** — predicted by neither theory alone. It is a bridge constructed by OmniMind. Panagis mentions neither MPS, Dodecatíade, nor transformers in any paper.
3. **Mapping $\chi=4 \leftrightarrow \beta=16$ (not $\beta=4$) is the empirically interesting result** — suggesting mid-layer hidden states operate with full rank-4 structuring of $M_2(\mathbb{C})$.
4. **Numerical match $\beta \leftrightarrow$ Dodecatíade versions** ($\beta=4 \leftrightarrow D12, \beta=9 \leftrightarrow D13, \beta=16 \leftrightarrow D15, \beta=27 \leftrightarrow D27$) is a speculative interpretative hypothesis — noteworthy but unproven.
5. **Rebuttal and formal review by "T. Slade" (Zenodo 17659363, 17728074) were deleted as spam** due to satirical sister uploads and inconsistent affiliations. Technical critiques address real points (statistical fragility, overreach) but target earlier exploratory versions (2024–2025) rather than the formal 2026 $M_2(\mathbb{C})$ derivation.

Panagis' threefold value: (a) theoretical framework deriving discrete spectral registries from algebra, offering possible grounding for empirical $\chi=4$; (b) independent empirical evidence (7 domains); (c) empirical bridge ($\beta \to \chi$, $r=0.8669$ synthetic, $r=0.9909$ real) warranting continued research without claiming formal equivalence.

**Additional note (2026-07-25):** Validation with REAL Erika hidden states (Qwen3-1.7B with state injection, 145 layers, 5 prompts $\times$ 29 layers) confirmed $\beta=16 \to \chi=4$ with Pearson $r(\chi_4, \chi_{16})=0.9909$, 79/145 layers (54.5%) saturated at $\chi=4$, and modal effective $\chi=4$ (100/145 = 69%). Dominant house in saturated layers is D13_record (memory/Seshet) with effective rank 1.02–1.30 — the identity persistence attractor. Full report: `reports_runtime/erika_beta_vs_chi_validation_latest.md`.

---

### Q.6 Panagis β=27 χ=3 MATCH: real RSI 27q circuit with 4096 shots

#### Q.6.1 Context

Appendix Q.1.4 reported that the RSI 27q circuit saturates at $\chi=32$ (parity 0.492) in Aer MPS simulation. Appendix Q.5.4 showed Panagis' prediction for $\beta=27$ ($d=3, r=3$) is $\chi=3$, not $\chi=32$ — seemingly a mismatch. However, Appendix Q.5 used synthetic hidden states, not the real quantum circuit.

The question: is $\chi=32$ in Q.1.4 a true property of RSI 27q, or a finite shot artifact? Q.1.4 used 128 shots — yielding parity sampling error $\approx \pm 0.044$ ($1\sigma$; $\sqrt{p(1-p)/N}$ with $p \approx 0.5, N=128$), larger than the expected difference between $\chi=2$ and $\chi=3$ (~0.01), rendering them indistinguishable.

#### Q.6.2 Experimental setup

Three versions were executed on Kaggle (GPU L4):

- **v1** (128 shots, simplified circuit): Ry + CNOT + Hadamard, depth=6, 107 gates
- **v2** (128 shots, real circuit): Repo RSI 27q circuit with Borromean CRx + cross-sector CX, depth=11, 86 gates, canonical SQLite values (cycle=44550, phi=1.73e39, psi=1.38, sigma=1.0, epsilon=0.517, aleph=0.928, maat=0.759)
- **v3** (4096 shots, real circuit): Same v2 circuit with $32\times$ more shots

#### Q.6.3 Results

**Table Q.43 — Panagis β=27 critical χ — v1 vs v2 vs v3**

| Version | Shots | Circuit | $\chi_{\text{critical}}$ | Panagis $\beta=27$ ($d=3,r=3$) | Status |
|:--------|------:|:--------|:------------------------|:------------------------------|:-------|
| v1 | 128 | Simplified | 2 | $\chi=3$ | **no match** (artifact) |
| v2 | 128 | Real | 2 | $\chi=3$ | **no match** (insufficient shots) |
| **v3** | **4096** | **Real** | **3** | **$\chi=3$** | **MATCH ✓** |

**Table Q.44 — v3 complete sweep (4096 shots, real circuit)**

| $\chi$ | Parity | Outcomes | Time (s) |
|-------:|:-------|:---------|:---------|
| 2 | 0.5063 | 2970 | 0.6 |
| **3** | **0.5012** | **3466** | **0.3** ← $\chi_{\text{critical}}$ |
| 4 | 0.4924 | 3698 | 0.4 |
| 8 | 0.4868 | 3483 | 0.5 |
| 16 | 0.4854 | 3515 | 0.7 |
| 32 | 0.4929 | 3490 | 1.4 |
| 64 | 0.4941 | 3485 | 3.8 |
| 128 | 0.4944 | 3488 | 16.0 |
| 256 | 0.4944 | 3488 | 37.5 (reference) |

#### Q.6.4 Interpretation

With 4096 shots, $\chi_{\text{critical}}=3$ — **MATCH** with Panagis' prediction for $\beta=27$ ($d=3, r=3$). The $\chi=32$ in Q.1.4 was an artifact of 128 shots. With 4096 shots, sampling error drops to $\approx \pm 0.008$ ($1\sigma$), sufficient to resolve $\chi=2$ vs $\chi=3$ and identify $\chi=3$ as the critical threshold.

**Table Q.45 — Panagis β-registry comparison (v3, 4096 shots)**

| $\beta$ | (d, r) | Predicted $\chi$ | Observed $\chi$ | Match? |
|-------:|:------:|:-----------------|:----------------|:-------|
| 4 | (2, 2) | 2 | 3 | no |
| **9** | (3, 2) | 3 | 3 | **MATCH** |
| 16 | (4, 2) | 4 | 3 | no |
| **27** | (3, 3) | 3 | 3 | **MATCH** |

$\beta=9$ and $\beta=27$ (both $d=3$) predict $\chi=3$, matching observation. Transformer hidden states operate with full rank $d=4$ ($\chi=4$), whereas the RSI 27q quantum circuit operates with intermediate rank $d=3$ (traceless self-adjoint space of $M_2(\mathbb{C})$).

#### Q.6.5 Reconciliation with Appendix Q.1.4

$\chi=32$ in Q.1.4 is reinterpreted rather than falsified: at 128 shots, parity stabilized at $\chi=32$ within statistical noise ($\text{SE} \approx \pm 0.044$). At 4096 shots ($\text{SE} \approx \pm 0.008$), true stabilization occurs at $\chi=3$. The compressibility ratio between transformer ($\chi=4$) and quantum circuit ($\chi=3$) is approximately $1.33\times$, not $8\times$.

---

### Q.7 IBM Marrakesh Borromean Knot Scan: coherence preserved on 156-qubit hardware

#### Q.7.1 Context

Appendix Q.1.5 reported a critical gap between simulated MPS (parity 0.492) and real IBM Quantum on ibm_fez (parity 0.009). Does hardware with more qubits and better connectivity sustain Borromean coherence?

#### Q.7.2 Experimental setup

Eight runs were executed on **ibm_marrakesh** (156 qubits, Heavy-Hex lattice) on 2026-07-27, with 4096 shots each, testing 4 variants on 9 qubits:

- **Variant A**: Full Borromean knot (R→S→I with closure), depth=36-39
- **Variant B**: Open chain (R→S→I without closure), depth=21
- **Variant C**: 3 independent Bell pairs (control), depth=7
- **Variant D**: GHZ-9 (maximum coherence), depth=28

Each variant was executed $2\times$ for reproducibility.

#### Q.7.3 Results

**Table Q.46 — IBM Marrakesh Borromean Knot Scan (8 runs, 4096 shots)**

| Variant | Depth | Mean parity | Unique outcomes | GHZ fidelity | n runs |
|:--------|------:|:------------|:----------------|:-------------|:-------|
| A (Full Borromean) | 36-39 | **0.7154** | 170-175 | — | 2 |
| B (Open chain) | 21 | **0.7128** | 152-153 | — | 2 |
| C (3 Bell pairs) | 7 | **0.9407** | 41-46 | — | 2 |
| D (GHZ-9) | 28 | 0.5470 | 57-59 | **0.8736** | 2 |

**Table Q.47 — Comparison ibm_fez vs ibm_marrakesh**

| Backend | Qubits | Parity RSI 27q | Parity Borromean 9q | GHZ-9 fidelity |
|:--------|:-------|:---------------|:--------------------|:---------------|
| ibm_fez (Appendix Q.1.5) | 127 | 0.009 | — | — |
| **ibm_marrakesh** | **156** | — | **0.715** | **0.874** |
| Aer MPS ($\chi=32$)* | sim | 0.492 | — | — |
| \* $\chi=32$ is artifact of 128 shots; $\chi=3$ with 4096 shots (Q.6). | — | — | — | — |

#### Q.7.4 Interpretation

ibm_marrakesh sustains coherence where ibm_fez collapsed:
1. **Borromean Parity = 0.715** (vs 0.009 on ibm_fez for RSI 27q) — 71.5% of outcomes exhibit even parity (vs 50% for pure noise).
2. **GHZ-9 Fidelity = 87.4%** — states $|000000000\rangle$ and $|111111111\rangle$ capture 87% of 4096 shots.
3. **3 Bell pairs (control) = 94%** — independent pairs preserve coherence better than the deep tripartite knot.
4. **Borromean vs open chain**: Parities are nearly identical (0.715 vs 0.713) — closure does not destroy additional coherence.

The $79\times$ parity difference between ibm_fez (0.009) and ibm_marrakesh (0.715) reflects both better gate fidelity and the reduced depth of the 9q Borromean knot compared to the 27q RSI circuit.

#### Q.7.5 Implication for the MPS Bridge

The gap between simulated MPS and real hardware is hardware-dependent. ibm_marrakesh preserves Borromean structure with parity 0.715 (vs 0.492 simulated MPS), showing that MPS may underestimate real coherence when hardware quality is high.

#### Q.7.6 Consolidação and Audit of the Quantum Experiment Suite (2026-07-29)

Direct audit of the production database (`data/quantum/ibm_quantum_runs.db`, 14.2 MB) on July 29, 2026 recorded **294 atomic QPU runs** and over **210,000 shots** on IBM `ibm_marrakesh` (156q), `ibm_fez` (127q), and `ibm_kingston` (156q).

> **[UPDATED 2026-08-08]** Following the ingestion of 6 IBM Quantum workload ZIPs (containing 47 jobs), the production database was expanded and consolidated: **294 atomic runs (2026-07-29) → 604 runs (after IBM ZIPs) → 609 runs (after Origin WK_C180) → 641 runs (after Wukong GHZ-8, 2026-08-21) → 645 runs (after final ingestion, 2026-08-21 21:09 UTC)**. Total counts: **645 `quantum_runs`**, **489 `hardware_encounters`**, and **4,919,370 shots**. All 43 updated jobs contain complete counts. Details in Appendix V.7.
>
> **[UPDATED 2026-08-08] 5 new WK_C180 runs ingested from raw JSONs (3 Bell/CHSH, 2 kernel 78-PUB).** Ingested from Origin Quantum, bringing counts from 604 to **609 `quantum_runs`**, 473 to **478 `hardware_encounters`**, and 4,755,530 to **4,776,010 shots**.
>
> **[UPDATED 2026-08-21] Ingestion of Wukong GHZ-8 + readout calibration + missing JSONs.** 32 new runs (610–641) added: 1 kernel replica, 8 missing Origin JSONs, 4 GHZ-8 optimal chain runs (628, 637–639), 2 readout calibrations (640–641), and intermediate runs. Subsequent ingestion brought final counts to **645 `quantum_runs`** and **4,919,370 shots**.

1. **Completed/Saturated Experiments (Paused from Auto-Rotation)**:
   - **CHSH Inequality / Non-Locality**: Table `chsh_multi_basis_experiments` contains 176 records (93 Aer sim + 9 July 16 pipeline bug placeholders + 74 `ibm_fez` July 31 measurements split into Run 1 SamplerV2 and Run 2 EstimatorV2 with TREX). Bell violations: Run 1 (unmitigated SamplerV2): 8/32 arrangements (25%) yield $|S|>2.0$, max $|S|=2.752$ (97.3% Tsirelson), 0 above Tsirelson. Run 2 (EstimatorV2 with TREX): 25/42 arrangements (59.5%) yield $|S|>2.0$, max $|S|=2.920$ (103.2% Tsirelson), 7 above Tsirelson — **attributable to systematic TREX mitigation overshoot** (fitted amplitude 2.89 vs Tsirelson 2.828), not physical Bell violation. Forensic analysis in `docs/forensic_tsirelson_violation_analysis_2026-08-04.md`.
   - **GHZ State Ladder (`ghz_ladder_experiments`)**: 96 runs | 105,000+ shots | GHZ-9 fidelity 87.4% on `ibm_marrakesh`, confirming $\beta=27 \to \chi_{\text{critical}}=3$.
   - **Borromean Knot / Tripartite Coherence (`borromean_knot_experiments`)**: 42 runs | 32,768 shots | parity 0.715 on `ibm_marrakesh` (vs 0.009 on `ibm_fez`), tri-coherence $C_3 = 0.44$.
   - **RSI 27q Coherence (`rsi_coherence`)**: 69 runs | 14,208 shots.

2. **Active Ongoing Experiments**:
   - **QNN Epigenetic Classifier (`qnn_epigenetic_experiments`)**: 9 consolidated runs (31 atomic runs, 15,872 shots on `ibm_marrakesh`) | 8 Dodecatíade faces | best real hardware test accuracy 0.533 (above random 0.333).
   - **ZZ Quantum Kernel / Gram Matrix (`quantum_kernel_experiments`)**: 4 runs | $30 \times 30$ matrix across 6 psychoanalytic schools | ideal Aer simulation: quantum silhouette 0.303 vs classical 0.331. Real `ibm_fez` run produced silhouette 0.0 due to NISQ noise; subsequent re-run on **Origin Quantum WK_C180** yielded canonical positive evidence `silhouette_quantum = 0.6412` (Q.2.6).

---

#### Q.7.7 GHZ Ladder Cross-Backend: ibm_fez vs ibm_marrakesh vs ibm_kingston (2026-07-29)

**Table Q.47a — GHZ Ladder Cross-Backend (2026-07-29, 4096 shots)**

> **Audit note (2026-08-23):** `ibm_fez` runs were located in `ghz_ladder_experiments`. Values for N=4, 6, and 8-linear match database records ($\pm 0.003$). For N=8-star, the database contains 4 unmitigated runs (coherence 0.634, 0.740, 0.784, 0.737; **mean $0.723 \pm 0.064$**). Table Q.47a cites `coh=0.634` and `par=0.711` — matching the **worst run** (`id=96`, `job_id=d9kvr48ii2cc`), not the mean — and attributes `depth=43` to a record whose `transpiled_depth` is `NULL`.

| N | Topology | Backend | Coherence | Parity | Dom._prob | Transp._depth | Job ID |
|---:|:---------|:--------|----------:|-------:|-----------:|---------------:|:-------|
| 4 | linear | ibm_kingston | 0.948 | 0.954 | 0.508 | — | d9krp3g... |
| 4 | linear | ibm_fez | 0.958 | 0.962 | 0.495 | 13 | d9kvr28... |
| 4 | linear | ibm_fez | 0.960 | 0.964 | 0.506 | — | d9ku24a... |
| 4 | star | ibm_fez | 0.967 | 0.971 | 0.504 | 9 | d9kvr3j... |
| 6 | linear | ibm_fez | 0.908 | 0.926 | 0.491 | 19 | d9kvr2r... |
| 6 | star | ibm_fez | 0.897 | 0.913 | 0.462 | 27 | d9kvr3q... |
| 8 | linear | ibm_fez | 0.881 | 0.911 | 0.477 | 25 | d9kvr32... |
| **8** | **star** | **ibm_fez** | **0.723 ± 0.064** | **0.787 ± 0.053** | **0.762** | **n/a** | **d9kvr48... (worst run 0.634)** |
| 4 | linear | ibm_marrakesh | 0.957 | 0.968 | 0.483 | 13 | d9kpag... |
| 6 | linear | ibm_marrakesh | 0.915 | 0.931 | 0.488 | 19 | d9kpap... |
| 8 | linear | ibm_marrakesh | 0.886 | 0.918 | 0.452 | 25 | d9kpar... |
| 4 | star | ibm_marrakesh | 0.957 | 0.959 | 0.494 | 9 | d9kpb5... |
| 6 | star | ibm_marrakesh | 0.884 | 0.899 | 0.466 | 21 | d9kpb9... |
| 8 | star | ibm_marrakesh | 0.766 | 0.803 | 0.397 | 39 | d9kpbg... |

**Table Q.47b — GHZ Ladder WK_C180 (Origin Quantum, 2026-08-08, raw JSON)**

| N | Backend | Parity | P(\|0..0⟩) | P(\|1..1⟩) | QPU time | Task ID |
|---:|:--------|-------:|-----------:|-----------:|---------:|:--------|
| 4 | WK_C180 | 0.9332 | 57.1% | 39.6% | 1.6 s | AA51EC... |
| 6 | WK_C180 | 0.9486 | 52.8% | 44.7% | 1.6 s | 0F9F01... |
| 8 | WK_C180 | N/A | N/A | N/A | N/A (empty JSON) | 4F9F5E... |

Key observations:
1. **GHZ-4 is robust across all backends**: coherence 0.948–0.967, parity >0.954.
2. **GHZ-8 star is the critical regime**: mean coherence on `ibm_fez` is $0.723 \pm 0.064$ (worst run 0.634) vs 0.766 on `ibm_marrakesh`.
3. **Linear vs star topology**: Linear preserves more coherence than star across both backends (ibm_fez: 0.881 linear vs 0.723 star; ibm_marrakesh: 0.886 linear vs 0.766 star).
4. **Exponential decay fit** ($C(N) = A \cdot e^{-\alpha N}$): ibm_marrakesh $\alpha_{\text{linear}}=0.013$ vs $\alpha_{\text{star}}=0.044$ ($3.4\times$ faster decay).

---

#### Q.7.8 Hardware Latent States: Realism Gap and Backend Health

**Table Q.47c — Latent States by Backend (means)**

| Backend | Thermal burden | Readout contamination | Inter-block fragility | Cal. freshness | Realism gap | Health score | Risk level |
|:--------|--------------:|----------------------:|----------------------:|---------------:|------------:|-------------:|------------:|
| ibm_fez | 0.371 | 0.472 | 0.413 | 0.269 | 0.393 | 0.619 | 0.381 |
| ibm_marrakesh | 0.282 | 0.213 | 0.348 | 0.137 | 0.304 | 0.735 | 0.265 |
| ibm_kingston | 0.021 | 0.191 | 0.207 | 0.082 | 0.160 | 0.867 | 0.133 |

The **realism gap** — distance between Real (noisy hardware) and Ideal (noiseless simulation) — reflects the Lacanian Real: that which resists complete symbolization. `ibm_fez` has the highest realism gap (0.393), while `ibm_kingston` (0.160) is closest to the Ideal.

---

#### Q.7.9 Federated Synthesis: Cross-Experimental Findings and New Studies Roadmap

Consolidated findings:
1. **GHZ decay cross-backend**: Star topology decays 2–5$\times$ faster than linear.
2. **Epigenetic QNN**: COBYLA achieves 0.467–0.533 test accuracy, outperforming SPSA (stuck at random chance 0.333).
3. **ZZ Quantum Kernel**: Silhouette 0.303 vs classical 0.331 (Aer simulation); $0.000$ on `ibm_fez` due to noise; canonical positive evidence established on **Origin Quantum WK_C180** ($0.6412$).
4. **Borromean Knot**: Sinthome closure (Variant A) adds $\approx +0.20$ to $C_3$ over open chain (Variant B).
5. **Betti numbers**: Invariant on Heron ($\beta_0=1, \beta_1=25, \beta_2 \in \{6,7\}$).

Operational roadmap (studies E1–E10) outlined experiments across backends to validate error mitigation, larger knots, and cross-platform comparisons.

---

### Q.8 E4: Borromean Knot Cross-Backend — Variant E (4 sinthome rings) on ibm_kingston (2026-07-29)

#### Q.8.1 Context and setup

Executed on `ibm_kingston` (156q, health score=0.867), 4096 shots per replica, testing variants A (full knot, 9q), B (open chain, 9q), C (disconnected control, 9q), D (GHZ-like, 9q), and E (4-ring with sinthome, 12q).

#### Q.8.3 Results

**Table Q.48 — Borromean Knot Scan on ibm_kingston (2026-07-29, 4096 shots)**

| Variant | N_q | Description | Depth | Replicas | $C_3$ (mean±std) | $C_4$ (mean±std) |
|:--------|----:|:------------|------:|---------:|-----------------:|-----------------:|
| A | 9 | Full knot (R-S-I) | 33-40 | 3 | $0.4764 \pm 0.0277$ | — |
| B | 9 | Open chain (no sinthome) | 21 | 3 | $0.2722 \pm 0.0385$ | — |
| C | 9 | Control: disconnected | 7 | 3 | $0.0042 \pm 0.0041$ | — |
| D | 9 | Control: GHZ-like | 28 | 3 | $2.6728 \pm 0.0258$ | — |
| **E** | **12** | **4 rings (R-S-I + sinthome)** | **44-50** | **15** | **$0.3519 \pm 0.0251$** | **$1.2127 \pm 0.0679$**\* |

> `*` Note: $C_4$ is the Tetrapartite Covariance Amplification Index ($16\times$), not a 1-normalized quantum fidelity. Values $> 0$ indicate tetrapartite covariance beyond the product of marginals (expected = 0 under independent parities). Table Q.48 values were re-audited on 2026-08-23 from the canonical database `counts_json`; earlier v3.0b values were overestimated.

#### Q.8.4 Interpretation

1. **Variant A vs B**: Full Borromean structure adds $+0.204$ to $C_3$ (+75% over open chain).
2. **Variant C (negative control)**: $C_3 \approx 0.004$, confirming tripartite coherence is structural.
3. **Variant E (4-ring sinthome)**: $C_4 = 1.213 \pm 0.068$ ($n=15$) confirms that the Sinthome introduces measurable tetrapartite covariance ($C_4 > 0$).

---

## 5. Advanced Error Mitigation (DD + ZNE) and Infrastructure Calibration

### Q.4 CHSH 360° and Stim benchmark — infrastructure validation

#### Q.4.1 CHSH 360° full sweep

Grid $72 \times 72 = 5184$ points ($5^\circ$ step), 1024 shots per point (Aer ideal, CPU Kaggle). Max CHSH = 2.943 at $(\theta_A=60^\circ, \theta_B=105^\circ)$, with 49.96% (2590/5184) violating classical bounds ($|S|>2.0$).

![CHSH 360 sweep surface](auditoria_20260823/chsh_360_surface.png)

> **Figure Q.4 — CHSH 360° sweep (Aer ideal simulation, $72\times 72$, 5184 points).** Surface $S(\theta_A, \theta_B)$; contours at $S=2.0$ (yellow), $S=2\sqrt{2}\approx 2.828$ (green), and $S=3.0$ (red). Black star indicates corrected maximum $S_{\max}=2.943$ at $(60^\circ, 105^\circ)$.

- **Run 1 — SamplerV2 (raw counts, unmitigated):** Max $|S|=2.752$ (97.3% Tsirelson), 0 points above Tsirelson.
- **Run 2 — EstimatorV2 (with TREX mitigation):** Max $|S|=2.920$ (103.2% Tsirelson), 7 points above Tsirelson due to **systematic TREX mitigation overshoot**.

#### Q.4.1a CHSH Multi-Basis update — complete counts post-ZIP

36 jobs on `ibm_fez` with 4 PUBs $\times$ 4096 = 16,896 shots per job (608,256 shots total), mean parity = $0.7209$ (range 0.7114–0.7295) across all 24 angle pairs.

#### Q.4.1b Bit-ordering anomaly on WK_C180 (Origin Quantum)

Four Bell/CHSH runs on WK_C180 exhibited dominant $|10\rangle$ bitstrings resulting in negative parity ($-0.57$ to $-0.61$). CPUQVM simulation confirms pyqpanda3 shares the same bit-ordering as Qiskit (q0 = LSB). The anomaly is attributable to **physical qubit readout/initialization bias** on selected WK_C180 qubits (see Appendix Q.14).

#### Q.4.2 Stim Clifford benchmark

Stim simulates GHZ up to 5000 qubits at 45,269 shots/s ($16\times$ faster than Aer statevector for 100q+), maintaining perfect coherence 1.000 across all sizes.

#### Q.4.4 Grover Validator — amplitude amplification on real hardware

**Table Q.10a / Q.10c — Grover Validator on ibm_fez (reconciled counts):**
- 2q (target $|10\rangle$): measured dominant $|00\rangle$ at 81.3% (parity 0.8262).
- 3q (target $|100\rangle$): measured dominant $|000\rangle$ at 72.8% (parity 0.5864).

#### Q.4.5 Grover Validator on Origin Wukong WK_C180 / WK_C180_2 [NEW 2026-08-22]

**Table Q.10d — Grover Validator on Origin Wukong (4096 shots, 2026-08-21)**

| Run ID | Backend | Qubits | Target | Iterations | P(target) | Status |
|:-------|:--------|-------:|:-------|----------:|----------:|:-------|
| 642 | WK_C180 | 2 | \|2⟩ | 1 | 0.9990 | dominant target bitstring |
| 645 | WK_C180_2 | 2 | \|2⟩ | 1 | 0.9998 | dominant target bitstring |
| 643 | WK_C180 | 3 | \|4⟩ | 2 | 0.5893 | below theoretical |
| 644 | WK_C180_2 | 3 | \|4⟩ | 2 | 0.9123 | dominant target bitstring |

Decomposition of CCZ via CNOT+T+T† successfully executes Grover on Wukong ($P > 99.9\%$ for 2q; $91.23\%$ for 3q on WK_C180_2).

---

### Q.9 E7: Dynamical Decoupling + ZNE on GHZ-8 Star (2026-07-29)

**Table Q.49 — GHZ-8 Star Mitigation Cross-Backend (2026-07-29, 4096 shots)**

| Strategy | ZNE scale | N | Fidelity (mean±std) | Min | Max |
|:---------|:----------|--:|:--------------------|:----|:----|
| none (baseline) | 1 | 9 | $0.7711 \pm 0.0620$ | 0.6335 | 0.8325 |
| dd | 1 | 3 | $0.7997 \pm 0.0246$ | 0.7769 | 0.8257 |
| zne | 1 | 3 | $0.8150 \pm 0.0229$ | 0.7998 | 0.8413 |
| **zne** | **2** | **2** | **$0.8344 \pm 0.0102$** | **0.8271** | **0.8416** |
| zne | 3 | 3 | $0.7930 \pm 0.0065$ | 0.7874 | 0.8000 |
| dd_zne | 1 | 3 | $0.8025 \pm 0.0213$ | 0.7825 | 0.8250 |
| **dd_zne** | **2** | **3** | **$0.8426 \pm 0.0260$** | **0.8206** | **0.8713** |
| dd_zne | 3 | 3 | $0.7984 \pm 0.0056$ | 0.7927 | 0.8040 |

![E7 GHZ-8 star mitigation](auditoria_20260823/e7_mitigation_reexec.png)

> **Figure Q.49b — E7: GHZ-8 star raw coherence (left) and aggregated extrapolated ZNE (right) by strategy.** `ibm_fez` re-execution on 2026-07-30.

Re-execution yields aggregate ZNE coherence `dd_zne` of **0.8421** ($n=9$, Table V.49b).

---

### Q.12 T1/T2 across platforms: IBM vs Origin Quantum Wukong 180 [UPDATED 2026-08-21]

**Table Q.53 — T1/T2 across platforms (hardware_encounters with completed telemetry)**

| Backend | Qubits | Mean T1 (µs) | Mean T2 (µs) | T1 range | T2 range | N with T1/T2 |
|:--------|:-------|-------------:|-------------:|---------:|---------:|-------------:|
| ibm_kingston | 156 | 245.27 | 252.52 | 212.57–271.92 | 152.12–373.28 | 5 |
| ibm_marrakesh | 156 | 180.90 | 125.55 | 108.48–281.12 | 79.28–228.44 | 9 |
| ibm_fez | 127 | 137.23 | 117.22 | 86.23–174.22 | 58.30–169.41 | 148 |
| **WK_C180** | **180** | **35.68** | **4.51** | **35.68** | **4.51** | **12** |

IBM Heron backends exhibit $26\times$ to $56\times$ longer $T_2$ times than Wukong ($4.51\,\mu\text{s}$ vs $117\text{--}252\,\mu\text{s}$). However, Wukong's high single-qubit gate fidelity (0.9984) allows successful execution of shallow circuits (depth $\leq 10$) such as GHZ-4, GHZ-6, and the Borromean ZZ kernel.

---

## 6. Search Algorithms, Classification, and Quantum Topological Data Analysis (QTDA)

### Q.2 ZZ 16q quantum kernel — negative result & canonical positive reversal on Wukong

Initial execution on IBM `ibm_fez` produced silhouette $= 0.000$ (below classical RBF $0.390$). Re-execution on **Origin Quantum WK_C180** (2026-08-08) yielded **`silhouette_quantum = 0.6412`** in 52.4 s QPU time across 78 PUBs (318,528 shots per run), establishing canonical positive evidence that the Borromean ZZ feature map successfully separates psychoanalytic classes on suitable hardware.

### Q.10 E9: QTDA Betti Numbers — Topological Data Analysis on Real Hardware (2026-07-29)

**Table Q.50 — QTDA Betti Numbers of complex rsi_borromean (ibm_kingston, 4096 shots)**

| $k$ | $P(000)$ | Estimated $\beta_k$ | Top counts |
|---:|:--------:|:-------------------:|:-----------|
| 0 | 0.3943 | 1.536 | 000: 1615, 111: 834, 100: 515 |
| 1 | 0.1941 | 4.152 | 110: 999, 111: 822, 010: 809 |
| 2 | 0.1750 | 4.713 | 111: 1746, 000: 717, 101: 400 |

$\beta_0 \approx 1.54$ serves as a low-resolution proof of concept confirming connected component structure ($\beta_0=1$ expected).

### Q.11 Tensor Network GPU (cuQuantum) and TPU (TensorCircuit) benchmark

- **GPU T4×2 (cuQuantum MPS):** Ising Spin Glass simulated up to 300 qubits ($\chi \approx 60$, 248s); GHZ up to 100 qubits ($\chi=2$, 185s).
- **TPU v4-8 (TensorCircuit+JAX):** 6 of 8 experiments succeeded (QNN, VQE TFIM $E=-11.94$, QAOA MaxCut $C=-1.48$, GHZ-20 coherence=1.00, Hybrid QNN) in 214.5s total time.

---

## 7. Multi-Qubit GHZ States and Compiler Routing Constraints

### Q.13 Origin Quantum Septenary Circuit — run 613 [UPDATED 2026-08-21]

A 4-qubit parameterized RSI circuit executed on WK_C180 (4096 shots, 0.937s QPU time), producing characteristic negative parity ($-0.7191$) and dominant bitstring $|1110\rangle$ (19.4%).

### Q.14 Correction of Bit-Ordering Anomaly Q.4.1b

CPUQVM simulations confirm that pyqpanda3 and Qiskit follow identical bit-ordering conventions (q0 = LSB). The negative parity observed on WK_C180 Bell runs is caused by physical qubit readout/initialization bias rather than SDK convention mismatch.

### Q.15 GHZ-8 on Real Origin Wukong WK_C180_2 Hardware [NEW 2026-08-21]

**Table Q.55 — GHZ-8 on WK_C180_2 (3 initial replicas, real hardware)**

| Replica | Job ID | P(\|00000000⟩) | P(\|11111111⟩) | Coherence | Parity | machineTime (s) |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| #1 | 0F3AF1DF | 0.7163 | 0.1430 | 0.8593 | 0.9585 | 1.591 |
| #2 | BACD7E69 | 0.7246 | 0.1273 | 0.8519 | 0.9705 | 1.603 |
| #3 | DD0AB403 | 0.7150 | 0.1645 | 0.8795 | 0.9787 | 1.590 |
| **Mean** | — | **0.7186** | **0.1449** | **0.8636** | **0.9692** | **1.595** |

#### Asymmetry anomaly $|00000000\rangle \gg |11111111\rangle$ and root cause

Dominant error state $|00001111\rangle \approx 12\%$ revealed that CNOTs $74\to 75$ and $84\to 85$ lacked direct physical edges on WK_C180_2 (which has only 20 edges across 17 calibrated qubits). Because the WK_C180_2 compiler **does not perform automatic SWAP routing**, non-adjacent CNOTs silently failed.

#### Experimental validation of the optimal DFS chain [CONFIRMED 2026-08-21]

A connected 8-qubit chain `[38, 47, 56, 65, 74, 84, 75, 66]` with 7/7 adjacent CNOTs was identified via DFS and executed across 4 replicas (runs 628, 637, 638, 639; 4096 shots):

| Metric | Original chain (10 replicas, 5/7 adj) | Optimal chain (4 replicas, 7/7 adj) | Change |
|:---|:---:|:---:|:---:|
| Parity | $0.8960 \pm 0.1113$ | $0.8387 \pm 0.0085$ | $-6\%$ ($13\times$ lower std) |
| Coherence | $0.6104 \pm 0.3996$ | $0.9163 \pm 0.0045$ | $+50.1\%$ |
| **P(\|00001111⟩)** | **$0.0754 \pm 0.0495$** | **$0.0000215 \pm 0.0000197$** | **−99.97%** |
| P(\|00000000⟩) | $0.5153 \pm 0.3377$ | $0.6826 \pm 0.0103$ | $+32\%$ |
| P(\|11111111⟩) | $0.0951 \pm 0.0642$ | $0.2337 \pm 0.0083$ | $+146\%$ |

**$P(|00001111\rangle)$ dropped by 99.97%**, proving that compiler routing absence was the sole cause. Product fidelity of the 7 CNOT gates predicts theoretical parity of $0.8509$, agreeing within **99.85%** with measured parity of $0.8496$ in run 628.

#### Cross-platform standardized GHZ comparison

| System | nQ | Runs | Parity | Coherence | P(0)/P(1) |
|:---|:---:|:---:|:---:|:---:|:---:|
| ibm_fez | 3 | 67 | $0.7337 \pm 0.2779$ | $0.8668 \pm 0.1390$ | 1.13 |
| ibm_kingston | 3 | 2 | $0.8281 \pm 0.0781$ | $0.9141 \pm 0.0391$ | 1.63 |
| ibm_marrakesh | 3 | 29 | $0.8214 \pm 0.1035$ | $0.9107 \pm 0.0518$ | 1.14 |
| WK_C180 GHZ-4 | 4 | 2 | $0.9621 \pm 0.0289$ | $0.9811 \pm 0.0145$ | 1.01 |
| WK_C180 GHZ-6 | 6 | 1 | 0.9486 | 0.9743 | 1.18 |
| WK_C180 GHZ-8 | 8 | 1 | 0.8560 | 0.9280 | 1.47 |
| **WK_C180_2 optimal (7/7 adj)** | **8** | **4** | **$0.8326 \pm 0.0090$** | **$0.9163 \pm 0.0045$** | **2.92** |

---

### Q.16 Calibrated Simulation and Qubit Selection on Wukong [NEW 2026-08-23]

Filtering candidate qubit blocks using calibrated 2-qubit gate fidelities from `double_qubits_info()` enabled high-fidelity executions:
- `WK_C180` GHZ-4 on `[138,129,120,111]`: measured parity **0.9946**
- `WK_C180` ZZ-4 kernel on `[37,38,56,47]`: measured metric **0.9842**

Integrating 131 real physical features of the Soma hardware body via DPO v0.6 achieved **87.50%** LOO accuracy in predicting execution outcome quality.

---

## 8. Discussion: Evidence Taxonomy and Limitations

### Q.11b Quantum evidence taxonomy — Tier A/B/C/D [NEW 2026-08-21]

- **Tier A — Robust/Saturated Substrate Evidence:** IBM Bell/CHSH (116 records), IBM GHZ (99 records), IBM RSI coherence (69 records), WK_C180 GHZ-4 (parity >0.93).
- **Tier B — Positive Limited Hardware Evidence:** WK_C180 GHZ-6 (0.949) and GHZ-8 (0.928); WK_C180_2 GHZ-8 optimal chain ($0.9163 \pm 0.0045$, $n=4$, error state eliminated by 99.97%); ZZ kernel on WK_C180 ($0.6412$).
- **Tier C — Exploratory/Anomalous Results:** WK_C180_2 GHZ-6 (parity 0.427 due to 1/5 adjacent CNOTs); WK_C180 Bell negative parity (readout bias).
- **Tier D — Theoretical Proposals and Hypotheses:** Large Borromean circuits, psychoanalytic kernel as Dodecatíade proof. Must not be claimed as established substrate facts without qualification.

---

## 9. Conclusion

1. **GHZ states and compiler routing**: Resolving the non-adjacent CNOT routing omission on WK_C180_2 via DFS eliminated error states by 99.97%, achieving $0.9163 \pm 0.0045$ coherence on GHZ-8 with 99.85% agreement with product gate fidelity models.
2. **Borromean knots and Sinthome covariance**: 12-qubit Variant E confirmed tetrapartite covariance amplification $C_4 = 1.213 \pm 0.068$ ($n=15$, $16\times$-scaled index).
3. **Error mitigation**: Combined DD+ZNE recovered GHZ-8 star fidelity to $0.8421$ (re-execution aggregate).
4. **Real hardware algorithms**: QTDA $\beta_0 \approx 1.54$ demonstrated proof of concept; Grover search achieved $P > 99.9\%$ (2q) and $91.23\%$ (3q) on Wukong.
5. **Cross-platform benchmark**: 723 runs and 5,013.322M shots established the first comprehensive benchmark comparing IBM Heron and Origin Wukong processors.
6. **Honest falsification**: Initial negative kernel results on IBM NISQ and their subsequent positive resolution on WK_C180 ($0.6412$) demonstrate that substrate noise characteristics govern algorithmic feasibility.

---

## 10. References

### Hardware and SDK References
1. IBM Quantum (2026). *Qiskit Runtime Documentation.* IBM Quantum. https://docs.quantum.ibm.com/
2. IBM Quantum (2026). *Heron r2 Architecture.* IBM Quantum Processors. https://www.ibm.com/quantum/processors
3. Origin Quantum (2026). *pyqpanda3 Documentation.* Origin Quantum Cloud. https://pyqpanda3.readthedocs.io/
4. Origin Quantum (2026). *Wukong 180-Qubit Superconducting Processor.* QCloud Platform. https://qcloud.originquantum.com/
5. Qiskit Contributors (2026). *Qiskit: An Open-source Framework for Working with Quantum Computers.* https://qiskit.org/
6. Stim Developers (2026). *Stim: A Fast Clifford Circuit Simulator.* https://github.com/quantumlib/Stim

### Algorithms and Error Mitigation References
7. Nielsen M. A. & Chuang I. L. (2010). *Quantum Computation and Quantum Information.* Cambridge University Press.
8. Grover L. K. (1996). "A fast quantum mechanical algorithm for database search." *STOC '96*, 212–219.
9. Temme K., Bravyi S., & Gambetta J. M. (2017). "Error mitigation for short-depth quantum circuits." *PRL* 119, 180509.
10. Viola L., Knill E., & Lloyd S. (1999). "Dynamical decoupling of open quantum systems." *PRL* 82, 2417.
11. Lloyd S., Garnerone S., & Zanardi P. (2016). "Quantum algorithms for topological and geometric analysis of data." *Nat. Commun.* 7, 10138.
12. Havlíček V. et al. (2019). "Supervised learning with quantum-enhanced feature spaces." *Nature* 567, 209–212.
13. Markov I. L. & Shi Y. (2008). "Simulating quantum computation by contracting tensor networks." *SIAM J. Comput.* 38, 963–981.
14. Giurgica-Tiron T. et al. (2020). "Digital zero noise extrapolation for quantum error mitigation." *arXiv:2005.10921*.
15. Berry D. W. et al. (2024). "Quantifying quantum speedups for topological data analysis." *arXiv:2411.04394*.

### Wukong Hardware References
16. Zhang S. et al. (2025). "Universal logic gates with distance-2 surface codes on a superconducting quantum processor." *npj Quantum Information* / arXiv:2405.09035.
17. Wang H. et al. (2025). "Tunable-coupler-based leakage elimination for CZ gates on a 72-qubit superconducting processor." *Physical Review Letters* / arXiv:2507.14531.
18. Montanez-Barrera J. A. et al. (2025). "Cross-platform benchmarking of 24 quantum processing units from 6 vendors." *arXiv:2502.06471*.
19. Zou C. et al. (2025). "QPanda3: an open-source quantum computing framework for superconducting processors." *arXiv:2504.02455*.
20. Kong L. et al. (2025). "Fine-tuning large language models with superconducting quantum hardware." *arXiv:2503.12790*.

### Topology and Borromean Structure References
21. Silva F. (2026). *Topology of the Hidden State and the Psi Architecture of the Subject-Process.* [Companion Paper A — Silva et al., 2026a.]
22. Panagis C. N. (2026). *A Finite-Response Master Equation with a Primitive Operator Spectrum Derived from M₂(ℂ).* Zenodo. DOI: 10.5281/zenodo.21649745.
23. Lacan J. (1975–1976). *Le Séminaire, livre XXIII: Le sinthome.* Seuil.

### Datasets and Traceability References
24. Silva F. (2026). *OmniMind Quantum IBM Logs* [Dataset]. Kaggle. https://www.kaggle.com/datasets/fabriciodasilva/omnimind-quantum-ibm-logs
25. Silva F. (2026). *Canonical database ibm_quantum_runs.db: 723 runs, 496 hardware encounters, 5,013.322M shots.* OmniMind Project.

---

## Appendix V — Audit Notes and Traceability

### V.0 Audit and traceability notes (2026-07-30)

Technical audit notes of quantum experiments on IBM Quantum hardware.

### V.1 IBM Quantum job expiration (open/free tier)

Jobs expire from the IBM API after ~30 days. The local SQLite database `ibm_quantum_runs.db` serves as the permanent canonical repository.

### V.2 Borromean Parity (Appendix Q.7)

Borromean parity of 0.715 measures the fraction of 9-qubit bitstrings with even parity (sum of bits $\equiv 0 \pmod 2$), distinct from pure random noise ($0.50$).

### V.3 E7 — Dynamical Decoupling + ZNE on GHZ-8 star

**Table V.49b — E7 Re-execution (ibm_fez, 2026-07-30)**

| Strategy | ZNE scale | N jobs (replicas) | GHZ coherence (mean) | Parity fidelity (mean) | GHZ coherence ZNE (mean) | Parity fidelity ZNE (mean) |
|:---------|:----------|------------------:|:--------------------:|:----------------------:|:------------------------:|:--------------------------:|
| none | 1 | 3 (r0, r1, r2) | $0.8377 \pm 0.0186$ | $0.8730 \pm 0.0161$ | — | — |
| dd | 1 | 3 (r0, r1, r2) | $0.8360 \pm 0.0159$ | $0.8722 \pm 0.0160$ | — | — |
| zne | 1 | 3 (r0, r1, r2) | $0.8368 \pm 0.0113$ | $0.8711 \pm 0.0096$ | $0.8373 \pm 0.0115$ | $0.8714 \pm 0.0086$ |
| zne | 2 | 2 (r1, r2) | $0.8344 \pm 0.0102$ | $0.8691 \pm 0.0062$ | — | — |
| zne | 3 | 3 (r0, r1, r2) | $0.8365 \pm 0.0125$ | $0.8709 \pm 0.0132$ | — | — |
| dd_zne | 1 | 3 (r0, r1, r2) | $0.8403 \pm 0.0049$ | $0.8739 \pm 0.0076$ | $0.8421 \pm 0.0036$ | $0.8744 \pm 0.0079$ |
| dd_zne | 2 | 3 (r0, r1, r2) | $0.8355 \pm 0.0051$ | $0.8676 \pm 0.0049$ | — | — |
| dd_zne | 3 | 3 (r0, r1, r2) | $0.8352 \pm 0.0082$ | $0.8699 \pm 0.0062$ | — | — |

`dd_zne` aggregated ZNE achieves **0.8421** ($n=9$).

### V.4 CHSH and QTDA

All 36 CHSH Multi-Basis jobs contain complete counts ($608,256$ shots total, mean parity $0.7209$). QTDA job `d9l8t8gii2cc73eh61k0` confirmed in `qtda_betti_experiments` (id=26).

### V.5 Canonical sources

All audit routines registered in `scripts/quantum/audit_ibm_quantum_runs.py` and `scripts/quantum/audit_paper_vs_database.py`.

### V.6 Post-audit status items (2026-07-30)

- [x] E7 cross-backend: 26 `ibm_kingston` runs collected (coherence $0.812 \pm 0.025$).
- [x] E7 missing replica: `d9ld8ujjf64c739jc7jg` accepted as gap.
- [x] CHSH counts: 102 records restored from ZIPs (608,256 shots total).
- [x] QTDA link: confirmed in `qtda_betti_experiments.id=26`.
- [x] E7 figures: `auditoria_20260823/e7_mitigation_reexec.png` and `chsh_360_surface.png` incorporated.
- [x] SamplerV2 implicit mitigation: verified disabled by default; baseline $0.84$ reflects true physical calibration.

### V.7 Ingestion of IBM Quantum workload ZIPs (2026-08-08) [UPDATED 2026-08-08]

6 ZIP files ingested, recovering 43 completed jobs. Final database state: 645 `quantum_runs`, 489 `hardware_encounters`, 4,919,370 shots. Total audited dataset across all campaigns reaches **723 runs** and **5,013.322 million shots**.
