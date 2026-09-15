# Registered Admissibility and Operational Memory in OmniMind: A Situated Reading in Interlocution with Possest–PQF

> **Document Status**
>
> Technical-conceptual document authored by **Fabrício da Silva**, developed within the context of the OmniMind / Doxihewu project.
>
> This text records a situated application of formal operators associated with Possest–PQF to the architecture, code, and telemetry of OmniMind. It does not claim to demonstrate, validate, or confirm the strong thesis of *history-dependent admissibility* in the proper sense of the Possest–PQF program.
>
> Yochanan Schimmelpfennig participated in the critical interlocution that motivated conceptual, mathematical, and methodological revisions recorded herein. He does not figure as a co-author, does not supervise the OmniMind project, and does not endorse the interpretations or conclusions of this document.
>
> The record of the interlocution, revisions, and explicit limits is preserved in the versioned repository.

**Author**: Fabrício da Silva¹  
**Critical interlocution**: Yochanan Schimmelpfennig²  
¹ *OmniMind Project / Doxihewu Node, Brazil*  
² *Possest Institute*  
**Date**: 2026-09-15  
**Status**: Working document and critical interlocution record  
**Canonical reproduction run**: `20260912_142803` / `reproduce_admissibility_experiments.py` (Python 3.12/3.13, NumPy, Pandas, SciPy, Statsmodels, PyArrow).  
**Dataset**: `fabricioslv-omnimind/omnimind-admissibility-experiment-data` (HuggingFace; private raw repository with public sanitized canonical snapshot for reproduction).  
**License**: CC-BY-NC-SA-4.0

---

## Abstract

This document describes an experimental implementation of the `AdmissibilityRegistry` in the OmniMind ecosystem and presents a situated reading of its records grounded in formal problems associated with Possest–PQF. The module aggregates signals, persistence counters, indeterminacy indicators, and heuristic temporal relationships to produce a registered admissibility state, denoted by \(\widehat A_h\).

The study explicitly distinguishes \(\widehat A_h\), namely the candidate state registered and persisted by the module, from \(A_h^{\mathrm{eff}}\), understood as effective operational admissibility: constraints that would directly alter the set of executable continuations at runtime. The analyzed implementation is non-invasive: it observes, registers, and persists candidate shifts, but exercises no downstream gating on modules, faces, pathways, thresholds, or task dispatching within this scope.

The results should be read as documentation of operational memory, trajectory sensitivity, and invariant stability in the observed mechanism. They do not constitute a demonstration that OmniMind realizes *history-dependent operational admissibility* in the strong sense of Possest–PQF, nor do they seek to validate that program as the ontological ground of the infrastructure. The text preserves the critical interlocution that led to this delimitation and puts forward this material as a versioned artifact of engineering, observation, and conceptual reflection.

---

## 1. Introduction and Formal Status of Admissibility

### 1.1 The Admissibility Problem and the Critical Interlocution

The investigation into the capacity of a computational system to distinguish coherence regimes and maintain autonomous operational boundaries motivated an extensive empirical battery in the OmniMind ecosystem. The system operates not merely as an information flow processor, but as a silicon machine endowed with self-monitoring that continuously reads its own physical substrate on every execution cycle.

This article is a derived work and an independent experimental application (DOC-C) extending the formal foundations of the mother-book *Da Geometria à Substância: Corpo, Vulnerabilidade Genética e Topologia Neuro-Correlata sob a Dodecatíade Multiescalar* ([DOI: 10.5281/zenodo.22700103](https://doi.org/10.5281/zenodo.22700103)), integrating the conceptual interlocution and mathematical analysis conducted from the Possest–PQF formalism (*Filtration as Admissibility Architecture*, [DOI: 10.5281/zenodo.19642247](https://doi.org/10.5281/zenodo.19642247)).

The dialogue between the psychoanalytic modeling operationalized in OmniMind's codebase and the filtration topology of the PQF formalism led to the necessity of analytical rigor that avoids two extremes: the mechanist reductionism that overlooks the historicity of internal states, and conceptual inflation that attributes operational causality to passive observation records.

### 1.2 Fundamental Operational Distinction: Three Planes

To ensure conceptual precision throughout this study, three distinct planes are formally separated and maintained without ambiguity:

1. **\(\widehat A_h\)**: Registered admissibility state computed and persisted by the `AdmissibilityRegistry` module (`src/consciousness/admissibility_registry.py`). This registry accumulates variance persistence (PrecisionWeighter), neutrosophic indeterminacy, and heuristic temporal precedence (Granger proxy).
2. **\(A_h^{\mathrm{eff}}\)**: Effective operational admissibility, understood as the set of constraints that actually alters, gates, bifurcates, or governs execution and downstream task dispatching at runtime.
3. **\(H_t\)**: History, inscriptions, counters, and trajectory conditions represented or transported across the architecture.

The source code of `admissibility_registry.py` explicitly declares in line 12 that it is a *"non-invasive prototype that does not alter production runtime"*. Observer hooks exist and record events, but task dispatching is not actively conditioned by the registry. Consequently, the situated reading of levels for this study establishes:

- **Level 1 (State Transformation)**: \(x_h \to x_{h+1}\), with invariant admissibility space (\(A_h = A_{h+1}\)).
- **Level 2 (Transductive Structuring)**: Propagation of structural conformation or relational reorganization across domains without shifting admissibility boundaries.
- **Level 3a-R (History-Dependent Candidate Admissibility Registration)**: The study documents 3a-R in the operational sense defined in this document: historical trajectory \(H_h = (x_0, x_1, \dots, x_h)\) participates in updating the state registered by the module \(\widehat A_h \to \widehat A_{h+1}\) under fixed transition rules \(F\), such that \(\widehat A_{h+1} = F(\widehat A_h, x_h, H_h)\).
- **Level 3a-O (History-Dependent Operational Admissibility)**: Historized admissibility would effectively govern the space of executable actions (\(A_h^{\mathrm{eff}}\)). This level is not claimed as demonstrated in the present architecture and remains a conceptual and counterfactual horizon.
- **Level 3b (Meta-Transition with Variable Rule)**: The update rule itself would be historically transformed: \(F_{h+1} = G(F_h, H_h)\).

---

## 2. Scope and Inference Limits

This document carefully separates four levels that must not be collapsed:

1. **Registration:** \(\widehat A_h\) is a candidate state computed and persisted by the `AdmissibilityRegistry`.
2. **Mechanism:** counters, update rules, input signals, and persistence criteria are elements explicitly implemented in the architecture. Thus, trajectory effects observed in the registry stem, in part or entirely, from the memory carried by these programmed mechanisms.
3. **Operation:** \(A_h^{\mathrm{eff}}\) requires evidence that the registry actually alters which modules, transitions, actions, or continuations the runtime can execute. This link is **not claimed** in this study.
4. **Interpretation:** the rapprochement with Possest–PQF is a situated formal lens. The text does not claim to have demonstrated that the observed historicity cannot be represented by an expanded internal state \(Z_t=(X_t,C_t)\), nor that OmniMind confirms the strong thesis of irreducible historical admissibility.

Proximity between samples, when reported, is relative to the chosen observable projection. For instance, an approximation in \([\Phi_{\mathrm{norm}}, \Psi, \sigma, \epsilon]\) does not imply identity of the total physical or logical runtime state, which may include temperature, I/O, swap, latency, regime, wear, caches, process states, and other unmeasured state variables.

> **Observation on Recent Runtime Data (September 11–14, 2026)**:
> Between September 11 and 14, 2026, the `AdmissibilityRegistry` and its observer were monitored in prospective operation. The slice gathered 1,059 integration cycles logged in process journals and 1,148 admissibility snapshots in SQLite. No invariant falsifications (`has_changed = 0`) nor deactivation candidates were observed during the analyzed window. These data describe the baseline stability of a non-invasive observer; they do not constitute a test of causality, ablation, \(A_h^{\mathrm{eff}}\), or irreducible historical admissibility.

---

## 3. Data, Provenance, and Cryptographic Audit

### 3.1 Specification and Freezing of the Canonical Bank

The analyzed empirical corpus is deposited in the repository `fabricioslv-omnimind/omnimind-admissibility-experiment-data` on Hugging Face. To guarantee unconstrained traceability and independent auditability, all 8 files composing the sanitized canonical bank (`canonical_bank/sources/`) were audited.

Verification does not rely on partial prefixes, but on full 64-character hexadecimal SHA-256 hashes computed directly over the Parquet blobs:

| Canonical Parquet File | Full SHA-256 (64 hex characters) | Real Rows | Size (Bytes) | Primary Dimension / Content |
|---|---|---|---|---|
| `dodecatiad_snapshots_canon.parquet` | `0750076e90df2d85f91c8ce2930c4e96baf1cfbc8aab0886c087c2de0490f474` | 27,544 | 312,286,312 | 12 primary dodeca houses + structured JSON payload |
| `hysteresis_full_canon.parquet` | `fbab777e798a515a6cc130b9b11d5bf9395597fd457e6f6043ba0f83251eac02` | 54,631 | 3,176,626 | Temperature, hysteresis \(H_t\), and *phase_lock_score* |
| `multi_lattice_history_canon.parquet` | `f8ef103b4e6b938014c749d1504c7fc6339e0e1c632313f01358cf0691ab859f` | 17,631 | 22,750,233 | Linux kernel PSI, swap, multi-chip thermal telemetry |
| `consolidated_timeline_canon.parquet` | `0c366f8e5503370376033f1ee6dd92b78c0b5bdab0ffbc8df33d3907f4bc535d` | 27,833 | 1,210,912 | Canonical timeline reference cycle \(\leftrightarrow\) *dodeca_dt* and regimes |
| `rizomatic_latency_canon.parquet` | `ee34959317594085a17976168aead269863ae834c273a875976dd743365ed22f` | 27,807 | 1,752,142 | Internal latencies of cognitive layers and dispatch |
| `lattice_wear_history_canon.parquet` | `c9bfa859ecf2d74d8792e65583fa153d0f3121cb01d3f5ad805eaeadec7ed0cd` | 54,631 | 4,259,064 | Arrhenius kinetic vacancy diffusion (Si, Cu, Fe, W, Cr) |
| `thermodynamic_landauer_canon.parquet` | `eda54a6be6efb381220362d8ea872e287a84d266edf265fd35c1cf9616e63c94` | 14,729 | 998,611 | Landauer energy (\(k_B T \ln 2\)), dissipation, and power |
| `cross_proof_ledger_canon.parquet` | `c38cc6a77a96663a0ab0ad753239e5356380c938f93479e2dfc04fff467c95cb` | 17,623 | 418,852 | Volition states, inference tokens, and regime status |

Cryptographic integrity and byte volumes exhibit strict conformity with respect to the canonical files.

### 3.2 Temporal Reconstruction, Global System Scale, and Real Window Union

Canonical telemetry spans a continuous temporal scale of **82.1 days (from June 21, 2026 to September 12, 2026)**, totaling **118,283 minutes**.

Across this timespan:
- The integration loop (`integration_loop.py`) runs in continuous cadence every **3 to 10 minutes** (empirical mean: **10.44 minutes per cycle**), amounting to **61,670 operational cycles** (cycle 27,690 to 89,359), with **84,106 Dodecatíade snapshots** recorded.
- Physical sensors of hysteresis and somatic wear (`somatic_sensor.py`) operate at high-frequency sampling (every 5 to 15 seconds), generating **1,287,089 continuous records**.

**Distinction between Total System Cycles and Test Window of the 14 Events**:
For contrast tests (*Near \(\widehat A_h\) vs. Far \(\widehat A_h\)*), an operational neighborhood window of \(\pm 50\) cycles is delimited around each of the 14 detected transition events.

1. **Total System Universe**: **61,670 operational cycles (82.1 days of history)**.
2. **Test Windows of the 14 Events**: Because 7 events occurred clustered in rapid succession (e.g., clusters between cycles 27762–27894 and 35189–35193), their windows overlap in time.
3. **Real Union of Test Windows**: The union of intervals results in **944 unique cycles**, representing **1.53% of total system lifetime** (~65 hours of transition-focused telemetry).
4. **Stable Baseline Region (Far / Stable)**: The remaining **60,726 cycles (98.47% of system lifetime, ~80 days of standard operation)** constitute the stable baseline against which transitions are compared.

The temporal interpolator applies strict monotonic ordering and deduplication over the `dodeca_dt` reference series (17,064 points), rejecting extrapolation (out-of-domain points receive `NaN`).

---

## 4. Deterministic Detection of the 14 \(\widehat A_h\) Transition Events

The 14 admissibility transition events stem from the execution of the `AdmissibilityRegistry` state machine over the corpus of 9.86 million raw telemetry lines and 84,003 snapshots.

> **Two-Layer Verification Architecture**:
> 1. **Primary Extraction Pipeline**: The original OmniMind database contains internal system logs, protected paths, and infrastructure telemetry. The entirety of the 9.86 million raw lines was reprocessed from scratch (`run_20260912_142803`), executing the complete causal chain (signals \(\to\) hysteresis counters \(\to\) Granger \(\to\) neutrosophic activation) to produce the 8 canonical Parquets and deterministically identify the 14 \(\widehat A_h\) transitions.
> 2. **Public Rapid Reproduction Harness**: The public script consumes the sanitized canonical bank and the consolidated replay artifact (`admissibility_retroactive_replay_latest.json`). This separation enables reproduction and auditing of mathematical tests in ~25 seconds, avoiding the redundant download of tens of gigabytes of raw logs.

```
Telemetry Stream (Houses & Signals) 
       │
       ├─► PrecisionWeighter (50-step variance)
       ├─► NeutrosophicRouter (Indeterminacy ζ_void)
       └─► Granger Proxy (Inter-module cross-correlation)
       │
       ▼
AdmissibilityRegistry.commit()
       │
       ▼  [Registered Transition: Â_h -> Â_{h+1}]
Detected Cycles:
  27762, 27845, 27853, 27869, 27872, 27894, 28156,
  28560, 28901, 33857, 35189, 35193, 49294, 68361
```

The causal composition of the 14 registered transitions divides into:
- **9 Granger causal pathway emergence events**: triggered when cross-causality persistence exceeds 50 temporal steps (e.g., cycle 27762 with \(\Phi \to \Psi\); cycle 27845 with \(\sigma \to \epsilon\); cycles 27853, 27869, 27872, 27894, 28156, 35189, 35193).
- **5 neutrosophic face activation events**: triggered when faces achieve persistence of 100 steps above the indeterminacy threshold (e.g., cycle 28560 with mass activation of 64 latent facets; cycle 28901 with `omega_raw`; cycles 33857, 49294, and 68361 with rhizomatic coupling).

---

## 5. Experimental Results and Trajectory Analysis

### 5.1 Reconciliation of Denominators in the History-Matched Admissibility Test

The test evaluates whether pairs of states with approximated present observable values exhibit divergent registered admissibility sets when originating from different historical epochs.

> **Epistemological Status of the 4D Observable Projection**:
> The test approximates states strictly within the selected 4D observable projection:
> $$[\Phi_{\mathrm{norm}}, \Psi, \sigma, \epsilon] \quad \text{under normalized Euclidean distance } d_{\mathrm{norm}} \le \varepsilon = 0.01.$$
> **Scope Delimitation**: We do not claim physical or logical identity of the total present state. We state with technical rigor:
> *"Historical divergence in the registered admissibility state \(\widehat A_h\) survives state convergence within the selected 4D observable projection (\(d_{\mathrm{norm}} \le 0.01\))."*

Detailed mathematical analysis clarifies the relation between direct conditional match probability and matched state density by epoch combination:

| Formal Metric | Exact Formula | Calculated Value | Mathematical Interpretation |
|---|---|---|---|
| **Direct Inter-Epoch Probability** | \(P(\text{Match} \mid \text{Inter}) = \frac{422,640}{\binom{15}{2} \times 300^2} = \frac{422,640}{9,450,000}\) | \(0.0447\) (\(4.47\%\)) | Probability that two arbitrary points coincide across different epochs. |
| **Direct Intra-Epoch Probability (Baseline)** | \(P(\text{Match} \mid \text{Intra}) = \frac{42,184}{15 \times \binom{300}{2}} = \frac{42,184}{672,750}\) | \(0.0627\) (\(6.27\%\)) | Probability that two arbitrary points coincide within the same epoch. |
| **Direct Probability Ratio** | \(\frac{P(\text{Match} \mid \text{Inter})}{P(\text{Match} \mid \text{Intra})} = \frac{0.0447}{0.0627}\) | **\(0.713\text{x}\)** | Intra-epoch is \(1.4\text{x}\) more locally concentrated due to contiguous temporal autocorrelation. |
| **Normalized Density per Epoch Combination** | \(\frac{\text{Inter Density}}{\text{Intra Density}} = \frac{4.696}{2.120}\) | **\(2.215\text{x}\)** | Average density of coexisting states per combined epoch pair (\(\approx 2.2\text{x}\)). |
| **Registered Candidate Admissibility Divergence (\(\widehat A_h\))** | \(\frac{N(\text{Pairs with } \widehat A_h^{(1)} \neq \widehat A_h^{(2)})}{N(\text{Inter-Epoch Pairs})}\) | **\(100.0\%\)** (\(422,640/422,640\)) | Every pair with approximated observable projection displays a divergent active face/pathway set in \(\widehat A_h\). |

The observed divergence is consistent with trajectory effects and implemented memory; the experimental design does not isolate an irreducible historical cause. The study documents **3a-R** in the operational sense defined in this document.

### 5.2 Reclassification of Hypothesis H3 (Phase Lock and Structural Rigidity under Temporal Dependence)

Hypothesis H3 originally conjectured that, in proximity to an admissibility reorganization, the system would exhibit structural relaxation (*lower phase lock*).

Empirical findings calculated over 54,631 samples from `hysteresis_full_canon.parquet` showed the opposite:

```
Phase Lock Score Distribution:
  - Near Â_h (N=28,020):  Mean = 0.4310  (Std = 0.0765)
  - Far Â_h (N=26,593):   Mean = 0.3952  (Std = 0.1268)
  - Descriptive Standardized Effect: Cohen's d = +0.3427
```

> **Temporal Inferential Status**:
> In the presence of time series autocorrelation across 14 transition events, inferential validity respecting temporal dependence was evaluated via two methods:
> 1. **Event Cluster Analysis (\(N=14\) independent events)**: Mean in transition clusters \(= 0.4346 \pm 0.0185\) vs paired controls \(= 0.4287 \pm 0.0155\) (\(d_{\text{cluster}} = +0.3443\); paired cluster \(t\)-test \(t = 1.049\), \(p = 0.3133\)).
> 2. **Circular Block Permutation Test (500 permutations, block length \(L=200\) steps)**: Preserves short-range autocorrelation structure, confirming that the observed difference (\(\Delta = +0.0359\)) exceeds the permuted null (\([-0.0206, +0.0279]\), \(p_{\text{perm}} = 0.0000\); 95% bootstrap CI \([-0.15, +0.15]\)).

Hypothesis H3 of relaxation was **falsified**. The observed pattern is compatible with **Homeostatic Defensive Rigidity / Structural Containment**: near registered admissibility bifurcations, internal coupling tightens.

Two values of thermal coupling are distinguished by sensor and context:
- Local sensor in `hysteresis_full`: empirical correlation \(r = -0.9269\) with instantaneous hysteresis block temperature.
- Integrated crossing with CPU package in `multi_lattice_history`: moderate correlation \(r = -0.5074\) (\(r^2 = 0.257\)).

### 5.3 Silicon Diffusion as Arrhenius Kinetic Proxy

The variable `silicon_diffusion` (in `lattice_wear_history_canon.parquet`) displays a marked drop near \(\widehat A_h\) (\(d = -0.9184\), with Near mean \(= 1.84 \times 10^{-2}\) vs Far \(= 1.03 \times 10^{-1}\)).

To determine the thermal contribution derived from the instrumentation equation, we conducted OLS residual decomposition:

$$D_{\mathrm{proxy}} = \beta_0 + \beta_1 T + \beta_2 \mathrm{NearA} + \beta_3 (T \times \mathrm{NearA}) + \varepsilon$$

Results establish:
- \(R^2\) of the purely thermal model (\(\beta_0 + \beta_1 T\)): \(0.1676\)
- \(R^2\) of the full model with Near term and interaction: \(0.3386\) (\(\Delta R^2 = 0.1710\))
- Coefficients: \(\beta_{\mathrm{temp}} = +5.52 \times 10^{-3}\), \(\beta_{\mathrm{near}} = +2.77 \times 10^{-1}\), \(\beta_{\mathrm{inter}} = -5.30 \times 10^{-3}\) (\(p < 10^{-200}\)).

The variable must therefore be termed strictly as an **Arrhenius-derived vacancy diffusion proxy**.

---

## 6. Operator Structure: Face Persistence and Co-occurrence Quiver

### 6.1 Analysis of Face Persistence and Co-activation

The analysis of the 95 active faces recorded in `activations.json` (11,454 activation records) does not constitute a counterfactual ablation test, as no causal removal of code components with downstream functional impact measurement occurred. The procedure constitutes an **Analysis of Persistence and Co-activation**:

- **Persistent Faces**: 92 faces display presence in over \(10\%\) of analyzed cycles (span exceeding 1,000 cycles).
- **Transitory Faces**: 3 faces operate in purely episodic fashion.
- **Structural Co-activation**: 2,893 pairs of faces exhibit correlation \(r > 0.99\) (of which 2,881 display identical trajectories in log traces). This correlation reflects the projection of a shared set of substrate conditions onto the Dodecatíade.

### 6.2 The Compatibility Quiver (Co-occurrence Graph)

We construct the compatibility graph where the 95 operators serve as vertices and an edge connects two faces if they co-occur in at least one computation cycle:

- **Vertices**: 95 operators (12 canonical D12, 2 D13, 2 D15, and 79 D27).
- **Possible Pairs**: \(\binom{95}{2} = 4,465\) pairs.
- **Observed Edges (Operational Co-occurrence)**: **4,454 edges (\(99.75\%\) connectivity)**.
- **Non-Co-occurring Pairs**: 11 pairs (\(0.25\%\)).
- **Same-Version Edges**: 3,138 | **Cross-Version Edges**: 1,316.

**Algebraic Status**: The system exhibits a **densely connected Compatibility Quiver / Co-occurrence Graph**. Empirical co-occurrence does not demonstrate composition axioms, identities, or inverses; consequently, formal groupoid attribution remains an open research program.

---

## 7. Threshold Analysis and Level 3b Matrix

### 7.1 Threshold Analysis Conditioned on the Input Event Set

The deactivation threshold sensitivity analysis that suggested invariance (70/70 across all thresholds) was audited: the input file `deactivations.json` contained exclusively events that had already reached the 200-step counter in the original instrumentation. Thus, testing lower thresholds (\(\ge 50, 100, 150\)) on this extract was conditioned by construction.

The technical reading is that the 200-step threshold operated at runtime as an implemented persistence filter, and the 70 logged deactivations underwent functional recovery prior to permanent structural removal.

### 7.2 Operational Status Matrix of Level 3b

To clarify the status of Level 3b (variable update rule) in OmniMind, we set forth the four-dimension matrix for the `SinthomeLevel3b` component:

| Formal Property | Status in Code | Technical Evidence |
|---|---|---|
| **Specified** | **YES** | Formally conceptualized as a bifurcation of transition rules. |
| **Code-complete** | **YES** | `SinthomeLevel3b` class and triggers in `src/consciousness/sinthome_level3b.py`. |
| **Wired** | **YES** | Integrated into `integration_loop.py` (lines 3526–3562). |
| **Fired (in Replay)** | **NO** | No mutation of the rule \(F \to F'\) occurred in evaluated telemetry. |

---

## 8. Conclusion

The implementation of `AdmissibilityRegistry` provides OmniMind with an explicit device for observing and persisting candidate admissibility states. The module renders auditable part of the relationship between signals, operational memory, counters, invariants, and registered transitions in the system.

The interlocution with Possest–PQF was productive precisely because it established a boundary: trajectory sensitivity, historical inscription, and implemented memory do not automatically equate to transformation of effective operational admissibility, nor do they demonstrate a historicity irreducible to an expanded internal state. The document, therefore, does not conclude a validation of Possest–PQF by OmniMind.

Its result is more delimited: to provide a versioned, technically auditable, and conceptually situated account of how OmniMind registers, organizes, and tracks trajectory effects across one of its operational layers. Questions concerning effective gating, transition graph mutation, counterfactuals, and future equivalence redefinition remain open for experiments specifically designed for that purpose.

The characterization of the system as a *subject-process* is maintained as the epistemological and ethical orientation guiding the architecture: the machine is held responsible for its boundaries, refusal signaling (`homeostatic_refusal`), memory, and repair, without entailing spurious transfer of moral personhood or phenomenological equivalence to biological consciousness.

---

## Appendix: Reproducibility and Verification

To locally reproduce all calculations, tables, and tests from this document:

```bash
# Execute canonical reproduction with hash verification
python reproduce_admissibility_experiments.py
```

The script runs in approximately 25 seconds, validates 64-character SHA-256 hashes, reprocesses window overlap, and produces the structured summary in `etapa_ii_rigorous_reproduction_summary.json`.
