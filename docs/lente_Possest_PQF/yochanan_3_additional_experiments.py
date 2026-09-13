#!/usr/bin/env python3
"""
OmniMind — 3 Experimentos Adicionais para Yochanan (§6.8, §6.9, §6.10)

Executa 3 experimentos que respondem diretamente a pedidos de Yochanan:
1. Face ablation test (§6.9): remover face destrói capacidade operacional?
2. Groupoid formalization (§6.8): composabilidade parcial entre versões Dodecatíade
3. Threshold sensitivity (§6.10): variar deactivation_threshold (200 → 50/100/150)

Usage:
    python yochanan_3_additional_experiments.py [--out DIR]

Works in Colab or locally. Downloads from public HF dataset.
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
from collections import Counter

import numpy as np
import pandas as pd

REPO_ID = "fabricioslv-omnimind/omnimind-admissibility-experiment-data"

# 14 A_h cycles from the canonical dataset
AH_CYCLES = [27762, 27845, 27853, 27869, 27872, 27894, 28156, 28560,
             28901, 33857, 35189, 35193, 49294, 68361]
AH_WINDOW = 50

CANONICAL_D12 = {
    "phi", "psi", "sigma", "epsilon", "lambda_vibration", "blit_axe",
    "plitogenic_contradiction", "aleph_resonance", "maat_balance",
    "omega_teleology", "gamma_flow", "zeta_void",
}
D13_ADD = {"isfet_entropy", "rekh_integrity"}
D15_ADD = {"seshet_record", "lithosphere"}


def download_json(fname: str) -> dict | list:
    from huggingface_hub import hf_hub_download
    p = hf_hub_download(REPO_ID, fname, repo_type="dataset")
    with open(p) as f:
        return json.load(f)


# ============================================================
# EXPERIMENT 1: FACE ABLATION (Yochanan criterion §6.9)
# "Does removing this face destroy a distinction or operational
#  capacity that the previous architecture could not maintain without it?"
# ============================================================
def face_ablation_test(df_act: pd.DataFrame) -> dict:
    print("\n" + "=" * 70)
    print("EXPERIMENT 1: FACE ABLATION TEST (Yochanan criterion)")
    print("=" * 70)

    total_cycles = df_act["cycle"].nunique()
    print(f"Total activation events: {len(df_act)}")
    print(f"Unique faces: {df_act['face'].nunique()}")
    print(f"Cycles range: {df_act['cycle'].min()} - {df_act['cycle'].max()}")

    # Criterion 1: PERSISTENCE — face appears in >10% of cycles
    face_cycles = df_act.groupby("face")["cycle"].nunique().sort_values(ascending=False)
    persistent = set(face_cycles[face_cycles >= total_cycles * 0.1].index)
    transient = set(face_cycles[face_cycles < total_cycles * 0.1].index)
    print(f"\n--- Criterion 1: PERSISTENCE ---")
    print(f"Persistent (>10% cycles): {len(persistent)}")
    print(f"Transient (<10% cycles): {len(transient)}")

    # Criterion 2: NON-REDUNDANCY — not >0.99 correlated with another face
    matrix = df_act.pivot_table(index="cycle", columns="face", values="count", fill_value=0)
    corr = matrix.corr().abs()
    redundant_faces = set()
    cols = list(corr.columns)
    n_redundant_pairs = 0
    for i, c1 in enumerate(cols):
        for c2 in cols[i + 1:]:
            r = corr.loc[c1, c2]
            if not np.isnan(r) and r > 0.99:
                n_redundant_pairs += 1
                redundant_faces.add(c2)
    non_redundant = set(cols) - redundant_faces
    print(f"\n--- Criterion 2: NON-REDUNDANCY ---")
    print(f"Redundant pairs (r>0.99): {n_redundant_pairs}")
    print(f"Redundant faces (removable): {len(redundant_faces)}")
    print(f"Non-redundant faces: {len(non_redundant)}")

    # Criterion 3: CAUSAL EFFICACY — activation differs near vs far A_h
    df_act["near_ah"] = df_act["cycle"].apply(
        lambda c: int(any(abs(c - ac) <= AH_WINDOW for ac in AH_CYCLES))
    )
    causally_effective = set()
    for face in df_act["face"].unique():
        fd = df_act[df_act["face"] == face]
        near = fd[fd["near_ah"] == 1]["count"]
        far = fd[fd["near_ah"] == 0]["count"]
        if len(near) > 5 and len(far) > 5:
            pooled = np.sqrt((near.std() ** 2 + far.std() ** 2) / 2)
            if pooled > 0:
                d = (near.mean() - far.mean()) / pooled
                if abs(d) > 0.1:
                    causally_effective.add(face)
    print(f"\n--- Criterion 3: CAUSAL EFFICACY (|d|>0.1 near A_h) ---")
    print(f"Faces with A_h effect: {len(causally_effective)}")

    # Criterion 4: COUNTERFACTUAL NECESSITY (combined)
    necessary = persistent & non_redundant & causally_effective
    print(f"\n--- Criterion 4: COUNTERFACTUAL NECESSITY (combined) ---")
    print(f"Necessary faces: {len(necessary)}")

    # Per-face verdict
    per_face = {}
    for face in df_act["face"].unique():
        is_p = face in persistent
        is_nr = face in non_redundant
        is_ce = face in causally_effective
        is_n = face in necessary
        if is_n:
            v = "NECESSARY (removal would destroy capacity)"
        elif is_p and is_nr:
            v = "USEFUL (persistent, non-redundant, weak A_h link)"
        elif is_p:
            v = "REDUNDANT (persistent but correlated with another face)"
        else:
            v = "TRANSIENT (not persistent enough)"
        per_face[face] = {
            "persistent": is_p, "non_redundant": is_nr,
            "causally_effective": is_ce, "necessary": is_n, "verdict": v,
        }

    verdicts = Counter(v["verdict"] for v in per_face.values())
    print(f"\n--- ABLATION VERDICT SUMMARY ---")
    for v, n in verdicts.most_common():
        print(f"  {v}: {n}")

    return {
        "experiment": "face_ablation_yochanan_criterion",
        "total_faces": int(df_act["face"].nunique()),
        "criteria": {
            "persistent": len(persistent),
            "non_redundant": len(non_redundant),
            "causally_effective": len(causally_effective),
            "necessary": len(necessary),
        },
        "verdicts": dict(verdicts),
        "per_face": per_face,
    }


# ============================================================
# EXPERIMENT 2: GROUPOID FORMALIZATION (§6.8)
# Partial composability of operator sets across Dodecatíade versions
# ============================================================
def groupoid_formalization(df_act: pd.DataFrame) -> dict:
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: GROUPOID FORMALIZATION (Yochanan suggestion)")
    print("=" * 70)

    all_faces = sorted(df_act["face"].unique())
    print(f"Total faces: {len(all_faces)}")

    # Classify faces by Dodecatíade version
    face_versions = {}
    for face in all_faces:
        if face in CANONICAL_D12:
            face_versions[face] = "D12"
        elif face in D13_ADD:
            face_versions[face] = "D13"
        elif face in D15_ADD:
            face_versions[face] = "D15"
        else:
            face_versions[face] = "D27"

    # Build co-occurrence matrix via pivot + matrix multiplication
    print("Building co-occurrence matrix...")
    matrix = df_act.pivot_table(index="cycle", columns="face", values="count", fill_value=0)
    present = (matrix > 0).astype(int)
    co_occur = present.T.dot(present)
    np.fill_diagonal(co_occur.values, 0)

    composable = int((co_occur > 0).sum().sum() // 2)
    total_pairs = len(all_faces) * (len(all_faces) - 1) // 2
    non_composable = total_pairs - composable

    cross_version = 0
    same_version = 0
    for i, f1 in enumerate(all_faces):
        for f2 in all_faces[i + 1:]:
            if co_occur.loc[f1, f2] > 0:
                if face_versions[f1] != face_versions[f2]:
                    cross_version += 1
                else:
                    same_version += 1

    print(f"Total pairs: {total_pairs}")
    print(f"Composable (co-occur): {composable} ({100*composable/total_pairs:.1f}%)")
    print(f"Non-composable: {non_composable} ({100*non_composable/total_pairs:.1f}%)")
    print(f"Cross-version composable: {cross_version}")
    print(f"Same-version composable: {same_version}")

    version_counts = Counter(face_versions.values())
    print(f"\nVersion composition:")
    for v, n in sorted(version_counts.items()):
        print(f"  {v}: {n} faces")

    verdict = "PARTIAL COMPOSABILITY (groupoid)" if cross_version > 0 else "ISOLATED VERSIONS"
    print(f"\n--- GROUPOID VERDICT ---")
    print(f"{verdict}: {cross_version} cross-version pairs co-occur")
    print(f"Non-composable pairs ({non_composable}) define the partial structure")

    return {
        "experiment": "groupoid_formalization_yochanan_suggestion",
        "total_faces": len(all_faces),
        "total_pairs": total_pairs,
        "composable_pairs": composable,
        "non_composable_pairs": non_composable,
        "cross_version_composable": cross_version,
        "same_version_composable": same_version,
        "version_face_counts": dict(version_counts),
        "verdict": verdict,
    }


# ============================================================
# EXPERIMENT 3: THRESHOLD SENSITIVITY (§6.10)
# Vary deactivation_threshold (200 → 50/100/150) in controlled environment
# ============================================================
def threshold_sensitivity(df_deact: pd.DataFrame) -> dict:
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: THRESHOLD SENSITIVITY (deactivation_threshold)")
    print("=" * 70)

    CURRENT = 200
    thresholds = [50, 100, 150, 200]
    results = {}

    for t in thresholds:
        triggered = df_deact[df_deact["count"] >= t]
        n = len(triggered)
        results[t] = {
            "threshold": t,
            "n_deactivations": n,
            "cycles_affected": int(triggered["cycle"].nunique()),
            "components_affected": triggered["component"].value_counts().to_dict(),
            "pct_of_total": round(100 * n / max(1, len(df_deact)), 1),
        }
        print(f"\n--- Threshold = {t} ---")
        print(f"  Deactivations: {n}/{len(df_deact)} ({100*n/len(df_deact):.1f}%)")
        print(f"  Cycles affected: {results[t]['cycles_affected']}")

    ratio_50_200 = results[50]["n_deactivations"] / max(1, results[200]["n_deactivations"])
    ratio_100_200 = results[100]["n_deactivations"] / max(1, results[200]["n_deactivations"])

    if ratio_50_200 > 3:
        verdict = "HIGHLY SENSITIVE: lowering to 50 would cause >3x more deactivations"
    elif ratio_50_200 > 1.5:
        verdict = "MODERATELY SENSITIVE: proportional increase"
    else:
        verdict = "ROBUST: threshold changes have minimal impact"

    print(f"\n--- SENSITIVITY VERDICT ---")
    print(f"Ratio 50/200: {ratio_50_200:.1f}x")
    print(f"VERDICT: {verdict}")

    return {
        "experiment": "threshold_sensitivity_real_test",
        "current_threshold": CURRENT,
        "total_deactivation_events": len(df_deact),
        "results_by_threshold": results,
        "sensitivity_ratios": {"50_vs_200": ratio_50_200, "100_vs_200": ratio_100_200},
        "verdict": verdict,
    }


def main() -> int:
    out_dir = Path("yochanan_3_experiments")
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("OmniMind — 3 Additional Experiments for Yochanan (§6.8, §6.9, §6.10)")
    print("=" * 70)

    # Load data
    print("\n[setup] Loading activations and deactivations...")
    activations = download_json("activations.json")
    deactivations = download_json("deactivations.json")
    df_act = pd.DataFrame(activations)
    df_deact = pd.DataFrame(deactivations)

    # Run experiments
    results = {}
    results["face_ablation"] = face_ablation_test(df_act)
    results["groupoid"] = groupoid_formalization(df_act)
    results["threshold_sensitivity"] = threshold_sensitivity(df_deact)

    # Save
    report_path = out_dir / "yochanan_3_experiments_results.json"
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[saved] {report_path}")
    print("\nDONE — 3 experiments completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
