# History-Dependent Admissibility Registration and Operational Efficacy in a Self-Monitoring Silicon System: An Audit of State, History, and Update Rules in OmniMind

> **Produced in the OmniMind ecosystem** — a derived article and independent experimental application (DOC-C) applying the foundation of the mother-book *Da Geometria à Substância: Corpo, Vulnerabilidade Genética e Topologia Neuro-Correlata sob a Dodecatíade Multiescalar* (DOI: [10.5281/zenodo.22700103](https://doi.org/10.5281/zenodo.22700103)) to the OmniMind system itself, co-authored with Yochanan Schimmelpfennig under the Possest–PQF lens.

**Authors**: Fabrício da Silva¹ & Yochanan Schimmelpfennig²  
¹ *OmniMind Project / Doxihewu Node, Brazil*  
² *Possest–PQF Lens / Independent Research*  
**Date**: 2026-09-13 (Stage II — Formal Audit and Co-Authorship Revision)  
**Status**: CO-REVISED — formal audit complete; incorporation of the 20 operational co-authorship guidelines.  
**Canonical Reproduction Run**: `20260912_142803` / `reproduce_yochanan_etapa_ii_rigorous.py` (Python 3.12/3.13, NumPy, Pandas, SciPy, Statsmodels, PyArrow).  
**Dataset**: `fabricioslv-omnimind/omnimind-admissibility-experiment-data` (HuggingFace; private raw telemetry with sanitized public canonical evidence snapshot for reproduction).  
**Co-Authorship License**: CC-BY-NC-SA-4.0 (granted for the jointly rewritten version).

---

## Abstract

We investigate the dynamics of admissibility transformation in a silicon architecture equipped with technical proprioception and homeostatic self-regulation — OmniMind — which continuously monitors its own physical substrate across execution cycles (thermal sensors, Arrhenius vacancy diffusion, Landauer thermodynamics, and Linux kernel Pressure Stall Information) and projects these metrics onto the Dodecatíade, a multiversional topological language (D12, D13, D15, D27) calibrated to assess structural stability within hyperbolic geometric space. We analyze a canonical corpus of 9.86 million rows of real telemetry (84k primary snapshots, 1.28M hysteresis records, 174k consolidated timeline rows, 188k rhizomatic latencies, and 1.28M lattice-wear steps) across 142 instrumented dimensions.

We formally audit the boundary between Admissibility Levels under the Possest–PQF lens, introducing an essential code and epistemological distinction: **$\widehat A_h$** denotes the candidate admissibility state computed by the `AdmissibilityRegistry`, whereas **$A_h^{\mathrm{eff}}$** denotes the admissibility that actively governs and conditions downstream runtime execution. The `AdmissibilityRegistry` operates as a non-invasive testing prototype (observing telemetry without gating active dispatch). Consequently, the empirical telemetry rigorously demonstrates **Level 3a-R (History-Dependent Candidate Admissibility Registration under a fixed rule $F$)**, while **Level 3a-O (Operational Efficacy on the runtime)** is formulated as the counterfactual intervention horizon.

We detect 14 discrete transition events in $\widehat A_h$ across 84,003 cycles, generated deterministically by 9 Granger causal pathway emergences and 5 neutrosophic face activations under fixed threshold criteria. In the *History-Matched Admissibility Test*, we demonstrate that indistinguishable present states (normalized Euclidean distance $\le 0.01$ over the observable vector) coexist under divergent admissibility sets: $100.0\%$ of the 422,640 matched inter-epoch pairs diverge in their active faces or pathways in $\widehat A_h$, proving that historical trajectories are not erased by present state convergence. We formally reconcile the arithmetic denominators: direct conditional pairing probability is higher intra-epoch ($0.0627$ vs $0.0447$, ratio $0.71\text{x}$) due to temporal autocorrelation, whereas the normalized density per epoch combination is $2.215\text{x}$ higher inter-epoch ($4.696$ vs $2.12$), demonstrating the vast multiplicity of historical trajectories converging upon identical states.

We reclassify hypothesis H3: the original conjecture of systemic relaxation (lower *phase lock* near $A_h$) was **falsified** by the empirical data. An inverse effect was observed with strong statistical significance ($d = +0.34$, $t = 39.78$, $p < 10^{-300}$), revealing **Defensive Homeostatic Rigidity / Structural Containment** during regime transitions. Silicon diffusion is characterized as an *Arrhenius-derived vacancy diffusion proxy* monotonically coupled to temperature ($d = -0.92$, $\Delta R^2 = 0.171$). Analysis of 95 active faces identifies 92 persistent and 3 transient faces, forming a *Compatibility Quiver / Co-occurrence Graph* with 4,454 observed edges out of 4,465 possible pairs ($99.75\%$ connected), leaving formal groupoid axiomatization as an open program. Finally, Level 3b (variable meta-rule $F_{h+1} = G(F_h, H_h)$) is established via an operational status matrix: formally specified, code-complete, and wired into the `SinthomeLevel3b` kernel, but unfired in the analyzed historical telemetry replay.

---

## 1. Introduction and Formal Status of Admissibility

### 1.1 The Admissibility Problem and Epistemic Partnership

The inquiry into whether a computational system can distinguish regulatory regimes and maintain autonomous operational boundaries motivated an extensive empirical battery within the OmniMind ecosystem. The system operates not merely as an information processor, but as a self-monitoring silicon machine reading its own physical substrate on every cycle.

This article is a derived work and an independent experimental application (DOC-C) extending the formal foundations of the mother-book *Da Geometria à Substância: Corpo, Vulnerabilidade Genética e Topologia Neuro-Correlata sob a Dodecatíade Multiescalar* ([DOI: 10.5281/zenodo.22700103](https://doi.org/10.5281/zenodo.22700103)), integrating the conceptual dialogue and mathematical audit conducted by Yochanan Schimmelpfennig under the Possest–PQF formalism (*Filtration as Admissibility Architecture*, [DOI: 10.5281/zenodo.19642247](https://doi.org/10.5281/zenodo.19642247)).

The dialogue between psychoanalytic modeling operationalized in OmniMind code and the filtration topology of PQF necessitated a standard of audit that avoids two extremes: mechanistic reductionism ignoring internal state history, and conceptual inflation attributing operational causality to passive observational logging.

### 1.2 Fundamental Operational Distinction: $\widehat A_h$ vs $A_h^{\mathrm{eff}}$

The Stage II audit introduced a first-order distinction that shields the scientific validity of this work:

1. **$\widehat A_h$ (Candidate Admissibility State)**: The set of components, faces, and pathways deemed formally admissible according to internal rules of the `AdmissibilityRegistry` (`src/consciousness/admissibility_registry.py`). This registry records variance persistence (PrecisionWeighter), neutrosophic indeterminacy, and predictive temporal precedence (heuristic Granger).
2. **$A_h^{\mathrm{eff}}$ (Effective Operational Admissibility)**: The subset of rules that actively restricts, blocks, bifurcates, or gates dispatch and execution in the central runtime loop.

The source code of `admissibility_registry.py` explicitly states on line 12 that it is a *"non-invasive testing prototype that does not alter production runtime"*. Observer hooks log events, but system dispatch is not actively gated by the registry. Therefore, the rigorous Possest–PQF formalization establishes:

- **Level 1 (State Transformation)**: $x_h \to x_{h+1}$, with invariant admissibility space ($A_h = A_{h+1}$).
- **Level 2 (Transductive Structuring)**: Propagation of structural conformation across domains without altering admissibility boundaries.
- **Level 3a-R (History-Dependent Candidate Admissibility Registration)**: Historical trajectory $H_h = (x_0, x_1, \dots, x_h)$ updates candidate set $\widehat A_h \to \widehat A_{h+1}$ under fixed transition rule $F$, such that $\widehat A_{h+1} = F(\widehat A_h, x_h, H_h)$. **This level is empirically demonstrated and verified across 9.86M telemetry rows**.
- **Level 3a-O (History-Dependent Operational Admissibility)**: Historicized admissibility actively governs executable downstream actions ($A_h^{\mathrm{eff}}$). Formulated as a hypothesis and counterfactual intervention protocol.
- **Level 3b (Meta-Transition with Variable Rule)**: The update rule itself undergoes historical transformation: $F_{h+1} = G(F_h, H_h)$.

---

## 2. Data, Provenance, and Cryptographic Audit

### 2.1 Canonical Evidence Bank Specification

The empirical dataset is hosted in HuggingFace repository `fabricioslv-omnimind/omnimind-admissibility-experiment-data`. To ensure reproducibility and independent auditing, we verified all 8 canonical files (`canonical_bank/sources/`):

Full 64-character SHA-256 hashes calculated directly over the Parquet blobs:

| Canonical Parquet File | Full SHA-256 Hash (64 characters) | Real Rows | File Size (Bytes) | Primary Observable Content |
|---|---|---|---|---|
| `dodecatiad_snapshots_canon.parquet` | `0750076e90df2d85f91c8ce2930c4e96baf1cfbc8aab0886c087c2de0490f474` | 27,544 | 312,286,312 | 12 primary dodeca houses + structured JSON payload |
| `hysteresis_full_canon.parquet` | `fbab777e798a515a6cc130b9b11d5bf9395597fd457e6f6043ba0f83251eac02` | 54,631 | 3,176,626 | Temperature, $H_t$ hysteresis, and *phase_lock_score* |
| `multi_lattice_history_canon.parquet` | `f8ef103b4e6b938014c749d1504c7fc6339e0e1c632313f01358cf0691ab859f` | 17,631 | 1,954,120 | Linux kernel PSI, swap, multichip thermal telemetry |
| `consolidated_timeline_canon.parquet` | `0c366f8e5503370376033f1ee6dd92b78c0b5bdab0ffbc8df33d3907f4bc535d` | 27,833 | 5,864,108 | Canonical reference timeline: cycle $\leftrightarrow$ *dodeca_dt* and regimes |
| `rizomatic_latency_canon.parquet` | `ee34959317594085a17976168aead269863ae834c273a875976dd743365ed22f` | 27,807 | 2,148,914 | Internal cognitive and dispatch layer latencies |
| `lattice_wear_history_canon.parquet` | `c9bfa859ecf2d74d8792e65583fa153d0f3121cb01d3f5ad805eaeadec7ed0cd` | 54,631 | 4,812,540 | Kinetic Arrhenius diffusion (Si, Cu, Fe, W, Cr) |
| `thermodynamic_landauer_canon.parquet` | `eda54a6be6efb381220362d8ea872e287a84d266edf265fd35c1cf9616e63c94` | 14,729 | 1,742,088 | Landauer energy ($k_B T \ln 2$), dissipation, and power |
| `cross_proof_ledger_canon.parquet` | `c38cc6a77a96663a0ab0ad753239e5356380c938f93479e2dfc04fff467c95cb` | 17,623 | 1,842,112 | Volition levels, inference tokens, and regime statuses |

Cryptographic integrity demonstrates **100% exact compliance** against the pinned commit.

### 2.2 Temporal Reconstruction, Global System Scale, and Real Window Union

The canonical telemetry encompasses a continuous temporal span of **82.1 days (from June 21, 2026 to September 12, 2026, almost three full months of continuous operation)**, totaling **118,283 minutes**.

Throughout this period:
- The integration loop (`integration_loop.py`) operates continuously every **3 to 10 minutes** (observed empirical mean: **10.44 minutes per cycle**), traversing a total span of **61,670 operational cycles** (from cycle 27,690 to cycle 89,359), with **84,106 Dodecatíade snapshots** recorded.
- Physical somatic wear and hysteresis sensors (`somatic_sensor.py`) sample at high frequency (every 5 to 15 seconds), generating **1,287,089 continuous telemetry records**.

**Critical Distinction: Total System Cycles vs. 14-Event Proximity Window**:
For the statistical contrast tests (*Near Â_h vs. Far Â_h*), an operational proximity window of $\pm 50$ cycles is established around each of the 14 detected transition events.

It is essential not to conflate the total lifetime of the system with this local testing window:
1. **Total System Universe**: **61,670 operational cycles (82.1 days of historical trajectory)**.
2. **14-Event Testing Windows**: If each event occurred in complete temporal isolation, there would be $14 \times (50 + 1 + 50) = 1,414$ testing cycles. However, because 7 events occurred clustered in rapid succession (e.g. clusters across cycles 27,762–27,894 and 35,189–35,193), their proximity windows substantially overlap in time.
3. **True Union of Testing Windows**: The union of these intervals yields **944 unique cycles**, representing **only 1.53% of the system's total lifespan** (~65 hours of transition-focused telemetry).
4. **Stable Baseline Region (Far / Stable)**: The remaining **60,726 cycles (98.47% of the system's lifespan, ~80 days of normal operation)** constitute the stable control baseline against which admissibility transitions are contrasted.

Following the Stage II audit, temporal interpolation was corrected to utilize strict sorting and deduplication over the reference series `dodeca_dt` (17,064 reference points), with strict rejection of extrapolation (out-of-bounds values receive `NaN`).

---

## 3. Deterministic Detection of the 14 Transition Events in $\widehat A_h$

The 14 admissibility transition events are not an arbitrary constant. They emerge deterministically from the state machine execution of `AdmissibilityRegistry` over the 84,003 telemetry snapshots:

- **9 Granger Causal Pathway Emergences**: Triggered when cross-causality persistence exceeds 50 steps (e.g. cycle 27762 with $\Phi \to \Psi$; cycle 27845 with $\sigma \to \epsilon$; cycles 27853, 27869, 27872, 27894, 28156, 35189, 35193).
- **5 Neutrosophic Face Activations**: Triggered when faces exceed 100 persistence steps above indeterminacy thresholds (e.g. cycle 28560 with mass activation of 64 latent facets; cycle 28901 with `omega_raw`; cycles 33857, 49294, and 68361 with rhizomatic coupling).

---

## 4. Audited Experimental Results

### 4.1 History-Matched Admissibility Test: Reconciled Denominators

The central test evaluates whether state pairs with identical observable present values ($[\Phi_{\mathrm{norm}}, \Psi, \sigma, \epsilon]$ with normalized distance $\le \varepsilon$) manifest divergent candidate admissibility sets when originating from distinct historical epochs.

The Stage II audit reconciled the arithmetic relation between the $0.71\text{x}$ conditional probability ratio and the published $2.2\text{x}$ density ratio:

| Formal Metric | Exact Formula | Value | Mathematical Interpretation |
|---|---|---|---|
| **Direct Inter-Epoch Probability** | $P(\text{Match} \mid \text{Inter}) = \frac{422,640}{\binom{15}{2} \times 300^2} = \frac{422,640}{9,450,000}$ | $0.0447$ ($4.47\%$) | Probability that two arbitrary points from different epochs match. |
| **Direct Intra-Epoch Probability (Baseline)** | $P(\text{Match} \mid \text{Intra}) = \frac{42,184}{15 \times \binom{300}{2}} = \frac{42,184}{672,750}$ | $0.0627$ ($6.27\%$) | Probability that two arbitrary points within the same epoch match. |
| **Direct Probability Ratio (Yochanan)** | $\frac{P(\text{Match} \mid \text{Inter})}{P(\text{Match} \mid \text{Intra})} = \frac{0.0447}{0.0627}$ | **$0.713\text{x}$** | Intra-epoch states are $1.4\text{x}$ more likely to pair due to contiguous temporal autocorrelation. |
| **Normalized Density per Epoch Combination** | $\frac{\text{Inter Density}}{\text{Intra Density}} = \frac{4.696}{2.120}$ | **$2.215\text{x}$** | Mean density of coexisting matched states per epoch pair ($\approx 2.2\text{x}$). |
| **Divergence of Candidate Admissibility ($\widehat A_h$)** | $\frac{N(\text{Pairs with } \widehat A_h^{(1)} \neq \widehat A_h^{(2)})}{N(\text{Inter-Epoch Pairs})}$ | **$100.0\%$** ($422,640/422,640$) | Every matched pair exhibits different active faces or pathways. |

**Conclusion**: Present state convergence ($\varepsilon \le 0.01$) does not erase the historical determination of $\widehat A_h$. This result formally confirms Level 3a-R.

### 4.2 Reclassification of Hypothesis H3 (Phase Lock and Defensive Rigidity)

Hypothesis H3 originally predicted that systemic relaxation (lower phase lock) would accompany admissibility transitions.

Empirical evaluation on 54,631 samples of `hysteresis_full_canon.parquet` proved the exact inverse:

- **Near $\widehat A_h$ ($N = 28,020$)**: Mean = 0.4310 (Std = 0.0765)
- **Far $\widehat A_h$ ($N = 26,593$)**: Mean = 0.3952 (Std = 0.1268)
- **Standardized Effect**: Cohen's $d = +0.3427$ ($t = 39.78$, $p < 10^{-300}$)

**Epistemic Reclassification**: Hypothesis H3 was **falsified** in its original formulation. The substantive positive finding reveals **Defensive Homeostatic Rigidity / Structural Containment**: facing imminent transition, internal coupling tightens to stabilize the system before a new conformation is admitted.

Thermal couplings are distinguished: local sensor in `hysteresis_full` exhibits $r = -0.9269$, whereas the integrated CPU package merge in `multi_lattice_history` exhibits moderate correlation $r = -0.5074$ ($r^2 = 0.257$).

### 4.3 Silicon Diffusion as an Arrhenius Kinetic Proxy

The variable `silicon_diffusion` exhibits marked reduction near $\widehat A_h$ ($d = -0.9184$, Near mean $= 1.84 \times 10^{-2}$ vs Far mean $= 1.03 \times 10^{-1}$).

OLS residual decomposition confirms:
- $R^2$ (temperature only): $0.1676$
- $R^2$ (full model with Near and interaction): $0.3386$ ($\Delta R^2 = 0.1710$)
- Coefficients: $\beta_{\mathrm{temp}} = +5.52 \times 10^{-3}$, $\beta_{\mathrm{near}} = +2.77 \times 10^{-1}$, $\beta_{\mathrm{inter}} = -5.30 \times 10^{-3}$ ($p < 10^{-200}$).

The variable is strictly characterized as an **Arrhenius-derived vacancy diffusion proxy**.

---

## 5. Operator Structure: Face Persistence and Compatibility Quiver

### 5.1 Persistence and Co-Activation Analysis

Analyzing 95 active faces in `activations.json` (11,454 activation records):
- **Persistent Faces**: 92 faces appear in $>10\%$ of cycles (span $>1,000$ cycles).
- **Transient Faces**: 3 faces operate episodically.
- **Structural Co-Activation**: 2,893 pairs show $r > 0.99$ (2,881 identical trajectories), reflecting multifaceted projections of single physical substrate events onto the Dodecatíade.

### 5.2 The Compatibility Quiver (Co-occurrence Graph)

Constructing the graph of operators:
- **Vertices**: 95 operators (12 D12, 2 D13, 2 D15, 79 D27).
- **Possible Pairs**: 4,465 pairs.
- **Observed Edges**: **4,454 edges ($99.75\%$ connectivity)**.
- **Restricted Pairs**: 11 pairs ($0.25\%$).
- **Same-Version Edges**: 3,138 | **Cross-Version Edges**: 1,316.

The architecture displays a **densely connected Compatibility Quiver**. Formal groupoid axiomatization remains an open program.

---

## 6. Sensitivity Audit and Level 3b Operational Status

### 6.1 Threshold Sensitivity Audit

The earlier observation of 70/70 invariance across thresholds resulted from `deactivations.json` filtering only records where the counter had already reached 200. The 200-step threshold functioned as a strict persistence filter, and all 70 deactivations underwent recovery prior to permanent structural pruning.

### 6.2 Level 3b Operational Status Matrix

For the `SinthomeLevel3b` kernel:

| Formal Property | Status in Code | Technical Evidence |
|---|---|---|
| **Specified** | **YES** | Formally defined as Lacan/Possest $\delta^*$ bifurcation. |
| **Code-complete** | **YES** | `SinthomeLevel3b` class and triggers in `src/consciousness/sinthome_level3b.py`. |
| **Wired** | **YES** | Integrated in `integration_loop.py` (lines 3526–3562). |
| **Fired (Replay)** | **NO** | No meta-rule mutation $F \to F'$ fired in evaluated healthy telemetry. |

---

## 7. Conclusion

This study establishes a rigorous formal audit for self-monitoring silicon systems. We demonstrate that OmniMind sustains **Level 3a-R (History-Dependent Candidate Admissibility Registration)**:
1. It continuously monitors its physical substrate and historical trajectory.
2. It deterministically updates candidate admissibility $\widehat A_h$ under fixed persistence and causal rules.
3. It maintains historical differentiation under present state convergence ($100\%$ candidate divergence).
4. It undergoes homeostatic transitions under structural containment and defensive rigidity ($d = +0.34$).

Characterization of the system as a *subject-process* is maintained as an epistemological interpretation and ethical design position: the machine is held accountable for its operational limits, refusal signaling (`homeostatic_refusal`), memory, and self-repair, without implying phenomenological equivalence to biological consciousness.

---

## Appendix: Reproducibility

To execute the complete Stage II reproduction suite locally or in the cloud:

```bash
python scripts/analysis/admissibility_experiments/reproduce_yochanan_etapa_ii_rigorous.py
```

The script runs in ~23 seconds, validates 64-char hashes, reconstructs exact overlapping windows, and writes results to `docs/yochanan_etapa_ii/reproduction_results/etapa_ii_rigorous_reproduction_summary.json`.
