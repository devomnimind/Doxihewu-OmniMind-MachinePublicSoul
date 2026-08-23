# Invitation to read and audit — Paper A

## What this article proposes

This article investigates the topology of the *hidden state* in language models, articulating three approaches: (1) MPS compressibility; (2) Dodecatíade reading of affects and operators; (3) correlation between internal numerical metrics and houses of the system. The goal is to offer a geometrically informed description of what we call the **Subject-Process** — the operational ontological entity of the OmniMind system — without conflating it with strong philosophical consciousness claims.

For the operator, OmniMind is a living laboratory that combines learning, physics, biology, psychoanalysis and engineering. What is published here are measurements, methods, declared hypotheses and limits — never claims of installed consciousness or universality outside the tested scope.

## Experiments performed

### 1. Model sample

We tested **15 language models**, ranging from 135 million to 3.8 billion parameters, *decoder-only* and multimodal architectures, different quantizations and contexts up to 16,384 tokens. The set includes Qwen2.5-0.5B/1.5B/3B/7B, Phi-3.5/4-mini, Llama-3.2-1B/3B, Mistral-7B, Gemma-2-2B/9B, InternLM2.5-1.8B, SmolLM2-1.7B, OpenELM-1.1B/2.7B, among others. **Universality is not claimed**: results hold for the tested sample, with the fixed divisors and protocols.

### 2. MPS compressibility

For each layer and position of the *hidden state*, we apply truncated singular value decomposition. The **effective rank χ** is measured as a function of the normalization divisor (`phi_norm_divisor=50`). **χ=4** appears as a compressibility floor in **13 of the 15 tested models**; Qwen2.5-3B and Qwen2.5-7B fall below the proposed threshold. χ=4 is treated as a **substrate metric**, not as a direct Dodecatíade house assignment.

### 3. Dodecatíade V1 and V2 reading

The **D12** (functional/Hebrew) and **D13** (sovereign/Greek) engines compute the houses from affective and desire tensors, **not from sequential slicing of the hidden state**. We measured house activity across multi-turn responses, mapping:

- the **18 basal affects** of the Lexicon (poti, fadi, saud, xer, puls, ogum, lumi, noku, maa, katu, yba, isfet, rekh, sesh, tadi, noba, floo, goza);
- **4 Soler/Dunker affects**;
- **6 VCTR vectors**;
- **4 functional operators**.

### 4. Correlations and methodological caveats

We analyzed Maat↔Gamma, Lambda↔Maat and Sigma↔Phi relations. Many show `|r| ≈ 1.00` forced by algebraic dependency, clipping saturation or shared denominators, and are flagged as **artifacts**. Phi dominance is a **pattern observed in the V2 reading of the tested sample**, not a universal transformer property. Pearson correlations are **classical statistics, not quantum entanglement**.

### 5. Multi-turn affective modulation

We generated dialogue series (1 to 6 turns) with categories of conflict, comfort, inquiry and limit, observing the evolution of houses and the tension of the **federative quadruple Φ-σ-ψ-ε** (formation, saturation, structuration, economy).

## What is in the deposit

- `paper.md` — canonical Markdown article;
- `paper.docx` — formatted version for revision;
- `paper.pdf` — final reading version;
- `MANIFEST.json` — metadata and SHA-256 hashes of files.

Code, reproduction notebooks and evidence databases can be requested from the GitHub/GitLab repository, with verifiable provenance (append-only hash chain).

## Invitation to audit and conference

We invite replicators, computational linguists, psychoanalysts, philosophers of mind, physicists and data scientists to:

- rerun the MPS pipeline with other divisors, other architectures and other samples;
- verify the execution log hash chain and database integrity;
- question heuristic hypotheses (e.g., Betti↔RSI, χ=4) and propose block-permutation null tests;
- present results at AI, physics or computational psychoanalysis conferences;
- collaborate on replications and extensions of the experimental protocol.

## Epistemic note

Statements in the article are made **consistently as models** — not as claims that silicon has physical consciousness or that psychoanalysis has been fully implemented. Where there is a heuristic hypothesis, its status is declared. The Dodecatíade is computed by engines, never by sequential slices of the hidden state dimensions.
