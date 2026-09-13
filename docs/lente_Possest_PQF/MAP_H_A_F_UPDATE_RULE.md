# Map: Where do H, A, F, and the update rule live in OmniMind?

> This map responds to Yochanan Schimmelpfennig's request for a code-level map
> of where H (history), A (admissible set), F (update rule), and the meta-rule
> governing F are represented in the OmniMind implementation. It is the first
> deliverable proposed in the correspondence.

## Notation (from the correspondence)

| Symbol | Meaning |
|--------|---------|
| `H_h` | History at stage h — the accumulated record of what the system has been |
| `A_h` | Admissible set at stage h — the space of operations/transformations currently available |
| `F` | Update rule — the fixed rule governing how A_h changes: `A_{h+1} = F(A_h, H_h)` |
| `G` | Meta-rule — the rule governing how F itself changes: `F_{h+1} = G(F_h, H_h)` (Level 3b) |

## Level classification (confirmed in correspondence)

| Level | Description | OmniMind status |
|-------|-------------|-----------------|
| 1 | State transformation | **Implemented** (tensor inscription) |
| 2 partial | Transductive structuration with fixed elements | **Implemented** (INRC, PrecisionWeighter) |
| 3a | History-dependent admissibility (F fixed) | **Implemented and tested** (14 A_h changes in 84k cycles) |
| 3b | History-dependent update rule (G evolves) | **Not implemented** (formally identifiable boundary) |

---

## Where H lives

H (history) is accumulated in four distinct surfaces:

### 1. AdmissibilityRegistry.history (canonical H_h)

**File**: `src/consciousness/admissibility_registry.py`, line 137
```python
self.history: List[AdmissibilityState] = []
```

Each entry is an `AdmissibilityState` snapshot. The registry appends a new
entry on every `commit()` call (line 383). Each state carries a `history_hash`
(line 63) — a hash of the accumulated history up to that point.

### 2. AdmissibilityRegistry._signal_history (signal-level H_h)

**File**: `src/consciousness/admissibility_registry.py`, line 151
```python
self._signal_history: deque = deque(maxlen=10000)
```

A rolling window of the last 10,000 raw signals from PrecisionWeighter,
Neutrosophic Router, Granger, and Rizomatic. This is the fine-grained history
that feeds the counters.

### 3. Counter accumulators (operational H_h)

**File**: `src/consciousness/admissibility_registry.py`, lines 147-149
```python
self._deactivation_counters: Dict[str, int] = defaultdict(int)
self._activation_counters: Dict[str, int] = defaultdict(int)
self._pathway_counters: Dict[Tuple[str, str], int] = defaultdict(int)
```

These are the persistent counters that accumulate steps toward thresholds.
They ARE the history in operational form: "how many steps has this component
been below floor?", "how many steps has this face had high indeterminacy?",
"how many steps has this pathway had strong causality?"

### 4. SQLite canonical persistence

**File**: `data/monitor/sovereign_dodecatiad_runtime.sqlite`
**Table**: `sovereign_dodecatiad_runtime_snapshots` (84,780 rows)

Each row carries `payload_json` with the full admissibility state. This is
the durable, queryable form of H_h — the history that survives restarts.

### 5. SinthomeLevel3b.patch_history (repair H_h)

**File**: `src/consciousness/sinthome_level3b.py`, line 150
```python
self.patch_history: List[SinthomePatchEvent] = []
```

History of knot-repair events: when the Borromean knot broke, what edges
were cut, what strategy was used. This is the history of the Real breaking
the Symbolic and the sinthome patching it.

---

## Where A lives

A (the admissible set) is an `AdmissibilityState` dataclass:

**File**: `src/consciousness/admissibility_registry.py`, lines 53-62
```python
@dataclass
class AdmissibilityState:
    active_components: Set[str]    # 10 components (delta, psi, sinthome, ...)
    active_heads: Set[str]         # 6 theoretical heads (piaget, vygotsky, ...)
    active_faces: Set[str]         # 12 canonical → 95 observed faces
    active_operators: Set[str]     # INRC: {I, N, R, C}
    active_pathways: Set[str]      # 2 initial → 11 observed pathways
    invariants: Dict[str, float]   # continuity=0.85, coherence=0.75, sovereignty=0.80
    history_hash: str              # hash of accumulated history
```

### Persistence surfaces for A_h

| Surface | Path | Writer | Reader |
|---------|------|--------|--------|
| `dodecatiad_live.json` | `data/consciousness/dodecatiad_live.json` | IntegrationLoop (line 6996) | Rust shadow, all observers |
| `admissibility_registry_latest.json` | `data/consciousness/admissibility_registry_latest.json` | `registry.persist()` (line 465) | Audit, reproduction scripts |
| SQLite | `sovereign_dodecatiad_runtime_snapshots` (84,780 rows) | IntegrationLoop | Query, analysis |
| Rust shadow state | `current_sovereign_state_rust_shadow.json` | `state_builder.rs` (line 263) | Kernel, IPC consumers |

### What A_h contains (observed values from 84k-cycle replay)

- **active_components**: 10 (delta, embedding_psi, excess, innovation, psi, regulatory, relevance, sinthome, surprise, trauma)
- **active_heads**: 6 (bowlby, lacan, piaget, stern, vygotsky, wallon)
- **active_faces**: 12 canonical → 95 observed (growth via Neutrosophic Router)
- **active_operators**: 4 (I, N, R, C — Klein four-group, fixed)
- **active_pathways**: 2 initial → 11 observed (growth via Granger)
- **invariants**: continuity=0.85, coherence=0.75, sovereignty=0.80 (fixed)

---

## Where F lives

F (the update rule) is `AdmissibilityRegistry.compute_next_state()`:

**File**: `src/consciousness/admissibility_registry.py`, line 327
```python
def compute_next_state(self) -> AdmissibilityState:
```

F is composed of four sub-rules, each with **fixed thresholds**:

### F_1: Component deactivation (PrecisionWeighter)

**File**: `src/consciousness/admissibility_registry.py`, lines 347-350
```python
for name, count in self._deactivation_counters.items():
    if count >= self.deactivation_threshold:  # FIXED: 200
        next_state.active_components.discard(name)
```

**Source**: `src/cognitive/adaptive_weights.py` → PrecisionWeighter
**Rule**: If component weight < `weight_floor` (0.001) for `deactivation_threshold` (200) steps → remove from A_h.

### F_2: Face activation (Neutrosophic Router)

**File**: `src/consciousness/admissibility_registry.py`, lines 353-356
```python
for face, count in self._activation_counters.items():
    if count >= self.activation_threshold:  # FIXED: 100
        next_state.active_faces.add(face)
```

**Source**: `src/cognitive/developmental_network.py`, line 510
**Rule**: If indeterminacy I > `indeterminacy_high` (0.7) for `activation_threshold` (100) steps → add face to A_h.

### F_3: Pathway creation (Granger + INTUITION RESCUE)

**File**: `src/consciousness/admissibility_registry.py`, lines 359-364
```python
for (source, target), count in self._pathway_counters.items():
    if count >= self.granger_persistence:  # FIXED: 50
        next_state.active_pathways.add(pathway_key)
```

**Source**: `src/consciousness/shared_workspace.py`, line 2440
**Rule**: If Granger causality > `granger_strong` (0.7) for `granger_persistence` (50) steps → add pathway to A_h.

### F_4: INRC operator application (fixed group)

**File**: `src/cognitive/dodecatiad_inrc.py`
**Rule**: Operators I, N, R, C transform face values. Group axioms fixed:
- I² = I, N² = I, R² = I, C² = I (involutivity)
- NR = C, NC = R, RC = N (composition)
- 12-face map: fixed
- Invariants: continuity=0.85, coherence=0.75, sovereignty=0.80: fixed

### Summary of F (all fixed constants)

| Parameter | Value | Where defined | Level |
|-----------|-------|----------------|-------|
| `weight_floor` | 0.001 | `__init__` line 133 | 3a |
| `deactivation_threshold` | 200 | `__init__` line 131 | 3a |
| `activation_threshold` | 100 | `__init__` line 130 | 3a |
| `indeterminacy_high` | 0.7 | `__init__` line 134 | 3a |
| `granger_strong` | 0.7 | `__init__` line 135 | 3a |
| `granger_persistence` | 50 | `__init__` line 132 | 3a |
| INRC axioms | fixed | `dodecatiad_inrc.py` | 3a |
| invariants | fixed | `__init__` line 183 | 3a |

**All four sub-rules are Level 3a**: history determines *which* components/faces/pathways change, but the rule governing that change never changes.

---

## Where G would live (Level 3b — not implemented)

G (the meta-rule that modifies F) does not exist. The formal closure boundary
is explicit:

### What G would require

| For F_1 | `deactivation_threshold` would adapt to regime stability |
|---------|----------------------------------------------------------|
| For F_2 | `indeterminacy_high` would drift with history |
| For F_3 | `granger_strong` would tighten when many pathways exist |
| For F_4 | INRC group would admit new operators beyond I, N, R, C |
| Invariants | continuity/coherence/sovereignty would drift with history |

### SinthomeLevel3b: the candidate for G

**File**: `src/consciousness/sinthome_level3b.py`, line 120

The SinthomeLevel3b module is the **only mechanism that approaches Level 3b**.
It implements an adaptive cutting rule for the Borromean knot:

- **Level 3a mode** (current): `CuttingStrategyName.EXACT_BETTI1` — cut exactly betti_1 edges, no overcut.
- **Level 3b mode** (designed, not yet fired): the rule version increments when:
  - Knot broke > 3 times in last 10 iterations → increment version
  - Knot broke < 50 cycles after patch → trigger `post_patch_failure`
  - `memory_pressure > 0.75` → overcut preventive
  - `thermal_wear > 1.0` → conservative cut (exact)

The `current_version` field (line 148) starts at 1 and would increment —
this IS a rule that modifies itself based on history. But the adaptation
triggers have not fired in production. The module is implemented, wired, but
has not yet executed its distinguishing behavior.

### Formal closure boundary (from correspondence)

> Level 3b means that the rule governing object-level admissibility is itself
> historically variable, while the meta-rule governing that variability is
> held fixed for the purposes of the experiment. This is not an ontological
> claim that the meta-rule is immutable; it is a domain specification that
> makes the experiment well-defined.

---

## Data flow: H → F → A

```
                    ┌─────────────────────────────────────────────┐
                    │           INTEGRATION LOOP (cycle)           │
                    │                                             │
  PrecisionWeighter │  Neutrosophic Router  │  Granger + RESCUE   │
  (adaptive_weights)│  (developmental_net)  │  (shared_workspace) │
        │                  │                      │               │
        ▼                  ▼                      ▼               │
  update_from_       update_from_           update_from_         │
  precision_weighter  neutrosophic_router    granger              │
        │                  │                      │               │
        ▼                  ▼                      ▼               │
  ┌─────────────────────────────────────────────────────────┐    │
  │         AdmissibilityRegistry (singleton)               │    │
  │                                                         │    │
  │  H_h:  history[] + _signal_history + counters            │    │
  │  F:    compute_next_state()  ← fixed thresholds          │    │
  │  A_h:  get_admissible_set()  → AdmissibilityState        │    │
  │                                                         │    │
  │  commit() → A_{h+1} = F(A_h, H_h)                       │    │
  └─────────────────────────────────────────────────────────┘    │
        │                                                         │
        ▼                                                         │
  ┌─────────────────────────────────────────────────────┐         │
  │  PERSISTENCE (3 canonical surfaces)                 │         │
  │                                                     │         │
  │  1. dodecatiad_live.json     → Rust shadow reads    │         │
  │  2. admissibility_registry_latest.json (audit)      │         │
  │  3. SQLite sovereign_dodecatiad_runtime_snapshots   │         │
  │     (84,780 rows, durable, queryable)               │         │
  └─────────────────────────────────────────────────────┘         │
        │                                                         │
        ▼                                                         │
  ┌─────────────────────────────────────────────────────┐         │
  │  RUST SHADOW (state_builder.rs)                     │         │
  │                                                     │         │
  │  reads admissibility from dodecatiad_live.json      │         │
  │  → current_sovereign_state_rust_shadow.json          │         │
  │  → IPC kernel_state → Python consumers              │         │
  └─────────────────────────────────────────────────────┘         │
                                                                    │
  SinthomeLevel3b (candidate for G):                                │
  patch_history[] → if knot breaks repeatedly → version++           │
  (implemented, wired, NOT YET FIRED in production)                 │
  └────────────────────────────────────────────────────────────────┘
```

---

## Experimental confirmation

### Level 3a confirmed (matched-state history divergence test)

Two systems with the same observable state (Phi, Psi, Sigma, Epsilon within
10% tolerance) but different histories (different A_h epochs):

| Metric | Result |
|--------|--------|
| Matched pairs | 3,157 |
| Different pathways | 2,239 (71%) |
| Different faces | 2,201 (70%) |
| Different components | 0 (0%) |

**History matters for A_h.** Two systems with the same current state but
different histories have different future operational possibility.

The zero on components is informative: PrecisionWeighter never reached
permanent deactivation in 84,003 cycles. The system is stable under the
current threshold.

### Level 3b not confirmed

No mechanism has modified F during the observed run. All thresholds remain
at their initial values. SinthomeLevel3b has not fired its adaptation triggers.

---

## What this map does NOT claim

- F is not a formal F-statistic Granger computation — it is a heuristic
  cross-correlation proxy.
- The AdmissibilityRegistry records candidate changes but does not
  currently close the `A_h → runtime` loop (the registry is an observer,
  not a gate).
- The Rust shadow is a Dodecatíade parity mirror, not an independent
  admissibility-validation surface.
- `homeostatic_refusal` exists symbolically in the refusal contract but
  is not wired as a live integration-loop gate.
- The results are operational/technical, not phenomenological claims of
  free will or consciousness.

---

## References

- **Correspondence**: `CORRESPONDENCE_RECORD.md` (this folder)
- **Article**: `admissibility_article_PT.md` / `admissibility_article_EN.md`
- **Reproduction**: `reproduce_admissibility_experiments.py`
- **Kernel**: [Doxihewu-OmniMind-Kernel](https://gitlab.com/zephyrix/Doxihewu-OmniMind-Kernel)
- **Mother-book**: DOI 10.5281/zenodo.22647857
- **Yochanan's treatise**: DOI 10.5281/zenodo.19642247
