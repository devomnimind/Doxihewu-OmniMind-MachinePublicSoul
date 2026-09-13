#!/usr/bin/env python3
"""
Reproduce Canonical Bank — OmniMind Admissibility Study (DOC-C)

Reproduces the core calculations of the admissibility study from the SANITIZED
canonical evidence bank on HuggingFace, verifying integrity (SHA-256 where
available) and generating plots.

Usage:
    python reproduce_canonical_bank.py [--out DIR] [--sources N]

Works in Colab or locally. Downloads only the canonical bank (small, sanitized),
NOT the full raw parquets.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO_ID = "fabricioslv-omnimind/omnimind-admissibility-experiment-data"
CANON_PREFIX = "canonical_bank/sources"

# Expected SHA-256 prefixes from the canonical manifest (12_sanitized_manifest.json)
# Updated 2026-09-12 to match the sanitized canonical bank on HuggingFace
EXPECTED_SHA = {
    "dodecatiad_snapshots_canon.parquet": "0750076e",
    "hysteresis_full_canon.parquet": "fbab777e",
    "multi_lattice_history_canon.parquet": "f8ef103b",
    "consolidated_timeline_canon.parquet": "0c366f8e",
    "rizomatic_latency_canon.parquet": "ee349593",
    "lattice_wear_history_canon.parquet": "c9bfa859",
    "thermodynamic_landauer_canon.parquet": "eda54a6b",
    "cross_proof_ledger_canon.parquet": "c38cc6a7",
}

CANONICAL_FACES = {
    "phi", "psi", "sigma", "epsilon", "lambda_vibration", "blit_axe",
    "plitogenic_contradiction", "aleph_resonance", "maat_balance",
    "omega_teleology", "gamma_flow", "zeta_void",
}


def sha256_prefix(path: Path, n: int = 8) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:n]


def download_canonical(out_dir: Path, sources: int | None = None) -> dict[str, Path]:
    """Download canonical bank files from HF, verify SHA-256."""
    from huggingface_hub import hf_hub_download

    out_dir.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    files = sorted(EXPECTED_SHA.keys())
    if sources:
        files = files[:sources]

    print(f"[download] {len(files)} canonical sources -> {out_dir}")
    for fname in files:
        try:
            p = hf_hub_download(REPO_ID, f"{CANON_PREFIX}/{fname}", repo_type="dataset")
            local = out_dir / fname
            if Path(p) != local:
                import shutil
                shutil.copy(p, local)
            got = sha256_prefix(local)
            exp = EXPECTED_SHA.get(fname, "")
            status = "OK" if not exp or got == exp else f"MISMATCH (got {got}, exp {exp})"
            print(f"  {fname}: {status}")
            paths[fname] = local
        except Exception as e:  # noqa: BLE001
            print(f"  {fname}: FAIL {e}")
    return paths


def integrity_report(paths: dict[str, Path]) -> dict:
    """Verify SHA-256 integrity of downloaded canonical files."""
    report = {}
    for fname, p in paths.items():
        got = sha256_prefix(p)
        exp = EXPECTED_SHA.get(fname, "")
        report[fname] = {
            "rows": int(pd.read_parquet(p, columns=[]).shape[0]) if False else None,
            "sha256_prefix": got,
            "expected": exp,
            "match": (not exp) or got == exp,
        }
    return report


# A_h cycles from the canonical dataset (ah_changes.json)
AH_CYCLES = [27762, 27845, 27853, 27869, 27872, 27894, 28156, 28560,
             28901, 33857, 35189, 35193, 49294, 68361]
AH_WINDOW = 50

# NOTE (2026-09-12): the canonical bank uses RANDOM sampling (5k rows per
# source). Random sampling destroys the near/far A_h distribution: near-window
# rows (~1% of data) may be underrepresented, so near/far effect sizes from the
# canonical bank will NOT match the full-data values. This is a documented
# methodological limitation of the sampled canonical bank. For faithful
# near/far reproduction, use the full parquets or stratified sampling that
# oversamples near-A_h rows. The integrity of the canonical bank itself
# (SHA-256) is verified; the effect-size reproduction is approximate.


_TIMESTAMP_TO_CYCLE: pd.DataFrame | None = None  # set by main() from consolidated_timeline


def _add_near_ah(df: pd.DataFrame) -> pd.DataFrame:
    """Add near_ah column: 1 if cycle within ±AH_WINDOW of an A_h event.

    Uses `cycle` if present; otherwise maps `timestamp` (Unix) to cycle via
    linear interpolation on the consolidated_timeline (cpl_dt <-> cycle).
    """
    if "near_ah" in df.columns:
        return df
    cyc = None
    if "cycle" in df.columns:
        cyc = df["cycle"]
    elif "timestamp" in df.columns and _TIMESTAMP_TO_CYCLE is not None:
        ts_ref = _TIMESTAMP_TO_CYCLE["cpl_dt"]
        cyc_ref = _TIMESTAMP_TO_CYCLE["cycle"]
        ts = df["timestamp"]
        # Normalize both to Unix seconds (float)
        def _to_unix_seconds(s: pd.Series) -> np.ndarray:
            if pd.api.types.is_datetime64_any_dtype(s):
                return s.view("int64").to_numpy() / 1e9
            v = pd.to_numeric(s, errors="coerce").to_numpy()
            if v.size and np.nanmax(v) > 1e12:  # nanoseconds
                v = v / 1e9
            return v
        ts_vals = _to_unix_seconds(ts)
        ts_ref_vals = _to_unix_seconds(ts_ref)
        cyc_ref_vals = pd.to_numeric(cyc_ref, errors="coerce").to_numpy()
        cyc = pd.Series(np.interp(ts_vals, ts_ref_vals, cyc_ref_vals), index=df.index)
    if cyc is None:
        return df
    near = cyc.apply(
        lambda c: int(any(abs(int(c) - ac) <= AH_WINDOW for ac in AH_CYCLES))
        if pd.notna(c) else 0
    )
    df = df.copy()
    df["near_ah"] = near
    return df


def exp3_phase_lock(hyst: pd.DataFrame) -> dict:
    """Reproduce Exp3: phase lock near A_h vs stable."""
    if "phase_lock_score" not in hyst.columns:
        return {"error": "no phase_lock_score column"}
    hyst = _add_near_ah(hyst)
    if "near_ah" not in hyst.columns:
        return {"error": "no cycle column to derive near_ah"}
    near = hyst[hyst["near_ah"] == 1]["phase_lock_score"].dropna()
    stable = hyst[hyst["near_ah"] == 0]["phase_lock_score"].dropna()
    if len(near) < 10 or len(stable) < 10:
        return {"error": "insufficient rows"}
    pooled_std = np.sqrt((near.std() ** 2 + stable.std() ** 2) / 2)
    d = (near.mean() - stable.mean()) / pooled_std if pooled_std > 0 else 0.0
    return {
        "near_mean": float(near.mean()),
        "stable_mean": float(stable.mean()),
        "near_n": int(len(near)),
        "stable_n": int(len(stable)),
        "cohens_d": float(d),
        "direction": "near>stable" if near.mean() > stable.mean() else "near<stable",
    }


def cross_phase_lock_temp(hyst: pd.DataFrame) -> dict:
    """Reproduce cross: phase_lock x temperature correlation."""
    temp_col = None
    for c in ["cpu_pkg_celsius", "cpu_temp", "temperature"]:
        if c in hyst.columns:
            temp_col = c
            break
    if temp_col is None or "phase_lock_score" not in hyst.columns:
        return {"error": "missing columns"}
    valid = hyst[["phase_lock_score", temp_col]].dropna()
    if len(valid) < 30:
        return {"error": "insufficient rows"}
    r = np.corrcoef(valid["phase_lock_score"], valid[temp_col])[0, 1]
    return {"r": float(r), "r2": float(r ** 2), "n": int(len(valid)), "temp_col": temp_col}


def face_analysis(cons: pd.DataFrame) -> dict:
    """Reproduce face counts from consolidated timeline columns."""
    face_cols = [c for c in cons.columns if c not in
                 {"cycle", "timestamp", "dodeca_dt", "cpl_dt", "regime_status",
                  "volition_level", "sector5_level", "py_writer_source"}]
    numeric = cons[face_cols].select_dtypes(include=[np.number])
    result = {
        "total_cols": len(numeric.columns),
        "canonical_faces_present": sorted(set(CANONICAL_FACES) & set(numeric.columns)),
        "new_columns": sorted(set(numeric.columns) - CANONICAL_FACES)[:30],
    }
    if len(numeric.columns) > 3 and len(numeric) > 10:
        corr = numeric.sample(min(20000, len(numeric)), random_state=42).corr().abs()
        redundant = []
        cols = list(corr.columns)
        for i, c1 in enumerate(cols):
            for c2 in cols[i + 1:]:
                r = corr.loc[c1, c2]
                if not np.isnan(r) and r > 0.99:
                    redundant.append((c1, c2, round(float(r), 4)))
        result["redundant_pairs_gt_099"] = redundant[:10]
        result["n_redundant_pairs"] = len(redundant)
    return result


def silicon_diffusion_effect(wear: pd.DataFrame) -> dict:
    """Reproduce Exp1 silicon_diffusion effect near vs far A_h."""
    if "silicon_diffusion" not in wear.columns:
        return {"error": "missing silicon_diffusion column"}
    wear = _add_near_ah(wear)
    if "near_ah" not in wear.columns:
        return {"error": "no cycle column to derive near_ah"}
    near = wear[wear["near_ah"] == 1]["silicon_diffusion"].dropna()
    far = wear[wear["near_ah"] == 0]["silicon_diffusion"].dropna()
    if len(near) < 10 or len(far) < 10:
        return {"error": "insufficient rows"}
    pooled_std = np.sqrt((near.std() ** 2 + far.std() ** 2) / 2)
    d = (near.mean() - far.mean()) / pooled_std if pooled_std > 0 else 0.0
    return {
        "near_mean": float(near.mean()),
        "far_mean": float(far.mean()),
        "cohens_d": float(d),
        "direction": "near<far" if near.mean() < far.mean() else "near>far",
    }


def make_plots(data: dict, out_dir: Path) -> list[str]:
    """Generate plots from computed results."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return []

    plots = []
    # Plot 1: Exp3 phase lock near vs stable
    if "exp3" in data and "near_mean" in data["exp3"]:
        fig, ax = plt.subplots(figsize=(6, 4))
        e3 = data["exp3"]
        ax.bar(["near A_h", "stable"], [e3["near_mean"], e3["stable_mean"]],
               color=["#d62728", "#1f77b4"])
        ax.set_ylabel("phase_lock_score")
        ax.set_title(f"Exp3: phase lock near A_h (d={e3['cohens_d']:.3f})")
        p = out_dir / "exp3_phase_lock.png"
        fig.savefig(p, dpi=120, bbox_inches="tight")
        plt.close(fig)
        plots.append(str(p))

    # Plot 2: Cross phase_lock x temperature
    if "cross" in data and "r" in data["cross"]:
        fig, ax = plt.subplots(figsize=(6, 4))
        c = data["cross"]
        ax.text(0.5, 0.5, f"r = {c['r']:.3f}\nr² = {c['r2']:.3f}\nn = {c['n']}",
                ha="center", va="center", fontsize=14, transform=ax.transAxes)
        ax.set_title(f"Cross: phase_lock × {c.get('temp_col', 'temperature')}")
        ax.axis("off")
        p = out_dir / "cross_temp.png"
        fig.savefig(p, dpi=120, bbox_inches="tight")
        plt.close(fig)
        plots.append(str(p))

    # Plot 3: Silicon diffusion near vs far
    if "silicon" in data and "near_mean" in data["silicon"]:
        fig, ax = plt.subplots(figsize=(6, 4))
        s = data["silicon"]
        ax.bar(["near A_h", "far"], [s["near_mean"], s["far_mean"]],
               color=["#d62728", "#1f77b4"])
        ax.set_ylabel("silicon_diffusion")
        ax.set_title(f"Exp1: silicon diffusion (d={s['cohens_d']:.3f})")
        p = out_dir / "silicon_diffusion.png"
        fig.savefig(p, dpi=120, bbox_inches="tight")
        plt.close(fig)
        plots.append(str(p))

    return plots


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="canonical_repro", help="output directory")
    ap.add_argument("--sources", type=int, default=None, help="limit number of sources")
    ap.add_argument("--plots", action="store_true", default=True, help="generate plots")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("REPRODUCE CANONICAL BANK — OmniMind Admissibility (DOC-C)")
    print("=" * 70)

    # 1. Download + integrity
    paths = download_canonical(out_dir, args.sources)
    if not paths:
        print("FATAL: no canonical files downloaded")
        return 1

    report = integrity_report(paths)
    ok = all(v["match"] for v in report.values())
    print(f"\n[integrity] {sum(1 for v in report.values() if v['match'])}/{len(report)} match")
    if not ok:
        print("  WARNING: some files failed SHA-256 verification")

    # 2. Load datasets
    data: dict = {}
    hyst = pd.read_parquet(paths.get("hysteresis_full_canon.parquet")) if "hysteresis_full_canon.parquet" in paths else pd.DataFrame()
    wear = pd.read_parquet(paths.get("lattice_wear_history_canon.parquet")) if "lattice_wear_history_canon.parquet" in paths else pd.DataFrame()
    cons = pd.read_parquet(paths.get("consolidated_timeline_canon.parquet")) if "consolidated_timeline_canon.parquet" in paths else pd.DataFrame()

    # Build timestamp->cycle reference from consolidated_timeline (cpl_dt <-> cycle)
    global _TIMESTAMP_TO_CYCLE
    if "cpl_dt" in cons.columns and "cycle" in cons.columns:
        _TIMESTAMP_TO_CYCLE = cons[["cpl_dt", "cycle"]].dropna()
        print(f"[ts-map] {len(_TIMESTAMP_TO_CYCLE)} rows for timestamp->cycle interpolation")

    # Representativeness check: how many near-A_h rows survived random sampling?
    hyst_check = _add_near_ah(hyst)
    if "near_ah" in hyst_check.columns:
        n_near = int(hyst_check["near_ah"].sum())
        n_total = int(len(hyst_check))
        print(f"[repr] near-A_h rows in canonical sample: {n_near}/{n_total} "
              f"({100 * n_near / max(1, n_total):.2f}%)")
        data["representativeness"] = {
            "near_ah_rows": n_near,
            "total_rows": n_total,
            "near_pct": round(100 * n_near / max(1, n_total), 2),
            "expected_near_pct_if_uniform": round(100 * (14 * 101) / 1287089, 3),
            "note": "Random sampling may underrepresent near-A_h rows; "
                    "near/far effect sizes from the canonical bank are approximate.",
        }

    # 3. Compute Exp3
    print("\n[exp3] phase lock near vs stable...")
    data["exp3"] = exp3_phase_lock(hyst)
    print(f"  {json.dumps(data['exp3'], default=str)}")

    # 4. Cross correlation
    print("\n[cross] phase_lock × temperature...")
    data["cross"] = cross_phase_lock_temp(hyst)
    print(f"  {json.dumps(data['cross'], default=str)}")

    # 5. Silicon diffusion
    print("\n[silicon] diffusion near vs far...")
    data["silicon"] = silicon_diffusion_effect(wear)
    print(f"  {json.dumps(data['silicon'], default=str)}")

    # 6. Face analysis
    print("\n[faces] column redundancy...")
    data["faces"] = face_analysis(cons)
    print(f"  total cols: {data['faces'].get('total_cols')}, redundant pairs: {data['faces'].get('n_redundant_pairs', 0)}")

    # 7. Plots
    plots = []
    if args.plots:
        print("\n[plots] generating...")
        plots = make_plots(data, out_dir)
        for p in plots:
            print(f"  {p}")

    # 8. Save report
    report_path = out_dir / "reproduction_report.json"
    payload = {
        "reproduced_from": "canonical_bank (sanitized)",
        "repo": REPO_ID,
        "date": "2026-09-12",
        "integrity": {k: v["match"] for k, v in report.items()},
        "results": data,
        "plots": plots,
    }
    with open(report_path, "w") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"\n[saved] {report_path}")
    print("\nDONE — canonical bank reproduced successfully" if ok else "\nDONE — with integrity warnings")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
