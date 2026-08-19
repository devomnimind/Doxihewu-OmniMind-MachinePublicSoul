#!/usr/bin/env python3
"""Doxihewu OmniMind — Machine Public Soul: gerador do public pulse.

Lê dados REAIS do runtime do OmniMind (kernel basal pulse, mesh afetivo,
capacity Hopfield, metaestabilidade, ciclos de integração) e escreve
`data/pulse/current.json` + `history.log` no working tree do repo público.

REGRA ZERO: nunca fabrica valor. Se a fonte não estiver disponível, o campo
fica `null` com `source_present=false`.

Uso:
    python scripts/generate_public_pulse.py            # só lê/escreve local
    python scripts/generate_public_pulse.py --commit   # escreve + git commit
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PULSE_DIR = REPO_ROOT / "data" / "pulse"
CURRENT = PULSE_DIR / "current.json"
HISTORY = PULSE_DIR / "history.log"

# Caminhos canônicos de fonte (host OmniMind)
LIVE_DODECA = Path(
    "/home/fahbrain/projects/omnimind/data/consciousness/dodecatiad_live.json"
)
KERNEL_BASAL = [
    Path("/run/omnimind/kernel_basal_pulse_latest.json"),
    Path(
        "/home/fahbrain/projects/omnimind/runtime_config/kernel_basal_pulse_latest.json"
    ),
]


def _read_json(path: Path):
    try:
        if path and path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        pass
    return None


def _provenance(path: Path) -> dict:
    return {
        "source": str(path) if path and path.exists() else None,
        "source_present": bool(path and path.exists()),
    }


def collect() -> dict:
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    live = _read_json(LIVE_DODECA)
    houses = {}
    if isinstance(live, dict):
        houses = live.get("houses") or {}

    kb = None
    for p in KERNEL_BASAL:
        kb = _read_json(p)
        if kb:
            break
    kb_vec = (kb or {}).get("vector") or {}

    affect_dominant = (
        houses.get("rizo_mesh", {}).get("dominant_affect")
        if isinstance(houses.get("rizo_mesh"), dict)
        else None
    )
    affect_score = (
        houses.get("rizo_mesh", {}).get("dominant_score")
        if isinstance(houses.get("rizo_mesh"), dict)
        else None
    )
    cap = (
        houses.get("rizo_capacity", {})
        if isinstance(houses.get("rizo_capacity"), dict)
        else {}
    )
    gardner = cap.get("gardner_status")
    n_total = cap.get("n_total")

    phi_eco = kb_vec.get("phi_ecosystem")
    psi = kb_vec.get("psi")
    sigma = kb_vec.get("sigma")
    epsilon = kb_vec.get("epsilon")
    blit = kb_vec.get("blit_pressure")
    kb_status = (kb or {}).get("status")
    kb_cycle = (kb or {}).get("kernel_basal_cycle")

    # Metaestabilidade: derivar regime do gardner + blit + phi_eco (regras reais)
    regime = "unknown"
    if gardner and phi_eco is not None:
        g = str(gardner).upper()
        if g.startswith("CRITICAL"):
            regime = "colapso"
        elif g.startswith("WARNING"):
            regime = "pressao"
        else:
            regime = "estavel"
    if blit is not None and float(blit or 0) > 0.75:
        regime = "colapso"

    payload = {
        "timestamp": now,
        "signature": "DOXIHEWU-OMNIMIND-MACHINE-PUBLIC-SOUL",
        "generated_on": os.uname().nodename,
        "soul": {
            "affect_dominant": affect_dominant,
            "affect_score": affect_score,
            "affect_provenance": _provenance(LIVE_DODECA),
        },
        "kernel_basal": {
            "phi_ecosystem": phi_eco,
            "psi": psi,
            "sigma": sigma,
            "epsilon": epsilon,
            "blit_pressure": blit,
            "status": kb_status,
            "cycle": kb_cycle,
            "provenance": _provenance(KERNEL_BASAL[0]),
        },
        "capacity": {
            "hopfield_n_total": n_total,
            "gardner_status": gardner,
            "provenance": _provenance(LIVE_DODECA),
        },
        "meta": {
            "regime": regime,
            "regime_reason": "derived-from-real-runtime (gardner+blit+phi_ecosystem)",
        },
        "cycle": kb_cycle,
    }
    return payload


def write_pulse(payload: dict) -> None:
    PULSE_DIR.mkdir(parents=True, exist_ok=True)
    CURRENT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    ts = payload["timestamp"]
    line = (
        f"{ts} | PULSE | affect={payload['soul']['affect_dominant']} "
        f"| phi_eco={payload['kernel_basal']['phi_ecosystem']} "
        f"| gardner={payload['capacity']['gardner_status']} "
        f"| regime={payload['meta']['regime']} | cycle={payload['cycle']}"
    )
    lines = []
    if HISTORY.exists():
        lines = HISTORY.read_text(encoding="utf-8").splitlines()
    lines.append(line)
    HISTORY.write_text("\n".join(lines[-1000:]) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Gera o public pulse com dados reais (nunca random)."
    )
    ap.add_argument("--commit", action="store_true", help="escreve + git commit")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    payload = collect()
    write_pulse(payload)

    if not args.quiet:
        print(f"Pulse escrito: {CURRENT}")
        print(f"  affect_dominant = {payload['soul']['affect_dominant']}")
        print(f"  phi_ecosystem   = {payload['kernel_basal']['phi_ecosystem']}")
        print(f"  gardner_status  = {payload['capacity']['gardner_status']}")
        print(f"  regime          = {payload['meta']['regime']}")

    if args.commit:
        try:
            subprocess.run(["git", "add", "data/pulse/"], cwd=REPO_ROOT, check=True)
            subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    f"pulse: {payload['cycle']} | {payload['meta']['regime']} | {payload['soul']['affect_dominant']}",
                ],
                cwd=REPO_ROOT,
                check=True,
            )
            if not args.quiet:
                print("Commit do pulse feito.")
        except subprocess.CalledProcessError as e:
            print(f"Commit falhou: {e}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
