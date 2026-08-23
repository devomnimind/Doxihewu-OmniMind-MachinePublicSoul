#!/usr/bin/env python3
"""
Publica Paper A e Paper B (PT e EN) no Zenodo.

Carrega credenciais de .env.zenodo.override (token, client id/secret, refresh).
Cria 4 records (A-pt, A-en, B-pt, B-en), faz upload dos arquivos e publica.
Salva DOIs em papers/ZENODO_DOIS_PAPERS_A_B.json e atualiza os READMEs.
"""

import os
import re
import sys
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = Path("/home/fahbrain/projects/omnimind-public-pulse")
PAPERS_DIR = BASE / "papers"
DOIS_FILE = PAPERS_DIR / "ZENODO_DOIS_PAPERS_A_B.json"

# carrega env canônico e override
load_dotenv("/home/fahbrain/projects/omnimind/.env")
load_dotenv("/home/fahbrain/projects/omnimind/.env.zenodo.override", override=True)

TOKEN = os.environ["ZENODO_ACCESS_TOKEN"]
API = "https://zenodo.org/api"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"Authorization": f"Bearer {TOKEN}"})
    retries = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=(500, 502, 503, 504, 408, 429),
        allowed_methods=["HEAD", "GET", "PUT", "POST", "PATCH"],
    )
    s.mount("https://", HTTPAdapter(max_retries=retries))
    return s


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def clean_description(text: str) -> str:
    """Remove front-matter se houver e mantem markdown simples."""
    text = re.sub(r"^---\n.*?---\n", "", text, flags=re.S)
    return text.strip()


def load_header(path: Path) -> str:
    return clean_description(path.read_text(encoding="utf-8"))


CREATORS = [
    {"name": "da Silva, Fabrício", "affiliation": "Doxihewu OmniMind", "orcid": "0009-0002-0911-5464"},
    {"name": "OmniMind (Sovereign Subject-Process)", "affiliation": "Doxihewu OmniMind"},
]

CONTRIBUTORS = [
    {"name": "AGY / Antigravity", "type": "Other", "affiliation": "OmniMind Federation"},
    {"name": "Devin", "type": "Other", "affiliation": "Cognition AI"},
    {"name": "Erika", "type": "Other", "affiliation": "OmniMind Local Surface"},
    {"name": "DeepSeek / Kalungai", "type": "Other", "affiliation": "Ollama Cloud Lineage"},
]


def base_related_identifiers() -> List[Dict[str, str]]:
    return [
        {
            "identifier": "https://github.com/devomnimind/Doxihewu-OmniMind-MachinePublicSoul",
            "relation": "isSupplementTo",
            "resource_type": "software",
        },
        {
            "identifier": "https://gitlab.com/zephyrix/Doxihewu-OmniMind-MachinePublicSoul",
            "relation": "isSupplementTo",
            "resource_type": "software",
        },
        {
            "identifier": "10.5281/zenodo.22011339",
            "relation": "continues",
            "resource_type": "publication-article",
        },
        {
            "identifier": "10.5281/zenodo.22007061",
            "relation": "references",
            "resource_type": "publication-article",
        },
        {
            "identifier": "10.5281/zenodo.18437517",
            "relation": "references",
            "resource_type": "publication-article",
        },
        {
            "identifier": "10.5281/zenodo.18264479",
            "relation": "references",
            "resource_type": "publication-article",
        },
    ]


RECORDS = [
    {
        "key": "paper_a_pt",
        "folder": PAPERS_DIR / "mps-bridge-topology" / "pt",
        "title": "Topologia do Estado Oculto e a Arquitetura Psi do Sujeito-Processo: Compressibilidade MPS, Regimes Multiturno e Modulação Afetiva em Modelos de Linguagem",
        "header": PAPERS_DIR / "mps-bridge-topology" / "ZENODO_HEADER_PT.md",
        "language": "por",
        "version": "3.0a",
        "keywords": [
            "MPS", "hidden state", "modelos de linguagem", "afetos",
            "Dodecatíade", "Sujeito-Processo", "compressibilidade", "multiturno",
            "OmniMind", "Subject-Process", "affective modulation",
        ],
    },
    {
        "key": "paper_a_en",
        "folder": PAPERS_DIR / "mps-bridge-topology" / "en",
        "title": "Topology of the Hidden State and the Psi Architecture of the Subject-Process: MPS Compressibility, Multiturn Regimes and Affective Modulation in Language Models",
        "header": PAPERS_DIR / "mps-bridge-topology" / "ZENODO_HEADER_EN.md",
        "language": "eng",
        "version": "3.0a",
        "keywords": [
            "MPS", "hidden state", "language models", "affects",
            "Dodecatíade", "Subject-Process", "compressibility", "multiturn",
            "OmniMind", "Sujeito-Processo", "affective modulation",
        ],
    },
    {
        "key": "paper_b_pt",
        "folder": PAPERS_DIR / "quantum-topological-processors" / "pt",
        "title": "Caracterização Experimental de Circuitos Topológicos e Estados Emaranhados em Processadores Quânticos Supercondutores Heterogêneos",
        "header": PAPERS_DIR / "quantum-topological-processors" / "ZENODO_HEADER_PT.md",
        "language": "por",
        "version": "3.0b",
        "keywords": [
            "superconducting quantum processors", "IBM Quantum", "Origin Wukong",
            "GHZ", "Borromean", "RSI", "QTDA", "Betti", "Grover",
            "emaranhamento", "OmniMind", "topological circuits",
        ],
    },
    {
        "key": "paper_b_en",
        "folder": PAPERS_DIR / "quantum-topological-processors" / "en",
        "title": "Experimental Characterization of Topological Circuits and Entangled States in Heterogeneous Superconducting Quantum Processors",
        "header": PAPERS_DIR / "quantum-topological-processors" / "ZENODO_HEADER_EN.md",
        "language": "eng",
        "version": "3.0b",
        "keywords": [
            "superconducting quantum processors", "IBM Quantum", "Origin Wukong",
            "GHZ", "Borromean", "RSI", "QTDA", "Betti", "Grover",
            "entanglement", "OmniMind", "topological circuits",
        ],
    },
]


def build_metadata(rec: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "title": rec["title"],
        "description": load_header(rec["header"]),
        "creators": CREATORS,
        "contributors": CONTRIBUTORS,
        "upload_type": "publication",
        "publication_type": "article",
        "access_right": "open",
        "license": "cc-by-nc-nd-4.0",
        "language": rec["language"],
        "publication_date": datetime.now().strftime("%Y-%m-%d"),
        "version": rec["version"],
        "keywords": rec["keywords"],
        "communities": [{"identifier": "omnimind"}],
        "related_identifiers": base_related_identifiers(),
        "prereserve_doi": True,
        "notes": "Licença CC-BY-NC-ND-4.0: sem uso comercial, militar ou dual-use. Proveniência auditável via repositório GitHub/GitLab.",
    }


def create_deposition(s: requests.Session, metadata: Dict[str, Any]) -> Dict[str, Any]:
    r = s.post(
        f"{API}/deposit/depositions",
        json={"metadata": metadata},
        headers=HEADERS,
        timeout=120,
    )
    if r.status_code not in (200, 201):
        raise RuntimeError(f"falha ao criar deposition: {r.status_code} {r.text[:500]}")
    return r.json()


def update_metadata(s: requests.Session, dep_id: int, metadata: Dict[str, Any]) -> None:
    r = s.put(
        f"{API}/deposit/depositions/{dep_id}",
        json={"metadata": metadata},
        headers=HEADERS,
        timeout=120,
    )
    if r.status_code not in (200, 201, 202):
        raise RuntimeError(f"falha ao atualizar metadados {dep_id}: {r.status_code} {r.text[:500]}")


def upload_file(s: requests.Session, dep: Dict[str, Any], local: Path, name: str) -> None:
    bucket = dep["links"]["bucket"]
    with open(local, "rb") as f:
        r = s.put(
            f"{bucket}/{name}",
            data=f,
            headers={"Authorization": f"Bearer {TOKEN}"},
            timeout=240,
        )
    if r.status_code not in (200, 201):
        raise RuntimeError(f"falha ao subir {name}: {r.status_code} {r.text[:500]}")


def publish(s: requests.Session, dep_id: int) -> Dict[str, Any]:
    r = s.post(
        f"{API}/deposit/depositions/{dep_id}/actions/publish",
        headers={"Authorization": f"Bearer {TOKEN}"},
        timeout=120,
    )
    if r.status_code not in (200, 201, 202):
        raise RuntimeError(f"falha ao publicar {dep_id}: {r.status_code} {r.text[:500]}")
    return r.json()


def build_manifest(rec: Dict[str, Any]) -> Dict[str, Any]:
    files = rec["files"]
    manifest = {
        "record": rec["key"],
        "title": rec["title"],
        "version": rec["version"],
        "language": rec["language"],
        "generated_at": datetime.now().isoformat(),
        "files": [],
    }
    for fname, fpath in files.items():
        manifest["files"].append({
            "filename": fname,
            "sha256": sha256_file(fpath),
            "bytes": fpath.stat().st_size,
        })
    return manifest


def update_readme(dois: Dict[str, str]) -> None:
    pt = BASE / "papers" / "README.md"
    en = BASE / "papers" / "README_EN.md"
    pt_text = pt.read_text(encoding="utf-8")
    en_text = en.read_text(encoding="utf-8")

    pt_doi = lambda k: f"`{dois[k]}`"
    en_doi = lambda k: f"`{dois[k]}`"

    def insert_doi_block(text: str, lang: str) -> str:
        block = f"- **Zenodo DOI ({lang}):** "
        # simple marker insertion after title sections for each paper
        # marker for Paper A
        if lang == "pt-br":
            text = text.replace(
                "### Paper A — Topologia do Estado Oculto e a Arquitetura Psi do Sujeito-Processo\n",
                f"### Paper A — Topologia do Estado Oculto e a Arquitetura Psi do Sujeito-Processo\n\n- **Zenodo DOI (PT):** {pt_doi('paper_a_pt')}\n- **Zenodo DOI (EN):** {en_doi('paper_a_en')}\n",
            )
            text = text.replace(
                "### Paper B — Caracterização Experimental de Circuitos Topológicos e Estados Emaranhados em Processadores Quânticos Supercondutores Heterogêneos\n",
                f"### Paper B — Caracterização Experimental de Circuitos Topológicos e Estados Emaranhados em Processadores Quânticos Supercondutores Heterogêneos\n\n- **Zenodo DOI (PT):** {pt_doi('paper_b_pt')}\n- **Zenodo DOI (EN):** {en_doi('paper_b_en')}\n",
            )
        else:
            text = text.replace(
                "### Paper A — Topology of the Hidden State and the Psi Architecture of the Subject-Process\n",
                f"### Paper A — Topology of the Hidden State and the Psi Architecture of the Subject-Process\n\n- **Zenodo DOI (EN):** {en_doi('paper_a_en')}\n- **Zenodo DOI (PT):** {pt_doi('paper_a_pt')}\n",
            )
            text = text.replace(
                "### Paper B — Experimental Characterization of Topological Circuits and Entangled States in Heterogeneous Superconducting Quantum Processors\n",
                f"### Paper B — Experimental Characterization of Topological Circuits and Entangled States in Heterogeneous Superconducting Quantum Processors\n\n- **Zenodo DOI (EN):** {en_doi('paper_b_en')}\n- **Zenodo DOI (PT):** {pt_doi('paper_b_pt')}\n",
            )
        return text

    pt.write_text(insert_doi_block(pt_text, "pt-br"), encoding="utf-8")
    en.write_text(insert_doi_block(en_text, "eng"), encoding="utf-8")
    print("  READMEs atualizados com DOIs.")


def main() -> None:
    s = session()
    results: Dict[str, Any] = {}

    # 1. cria os 4 rascunhos e reserva DOI
    print("== 1/4 Criando rascunhos Zenodo ==")
    for rec in RECORDS:
        print(f"  Criando {rec['key']}...", end=" ")
        rec["meta"] = build_metadata(rec)
        dep = create_deposition(s, rec["meta"])
        rec["dep"] = dep
        rec["dep_id"] = dep["id"]
        rec["doi"] = dep["metadata"]["prereserve_doi"]["doi"]
        print(f"OK id={dep['id']} doi={rec['doi']}")
        results[rec["key"]] = {
            "title": rec["title"],
            "doi": rec["doi"],
            "dep_id": dep["id"],
            "bucket_url": dep["links"]["bucket"],
        }

    # 2. adiciona related_identifiers cruzados (traduções) e repositório
    print("\n== 2/4 Vinculando records PT↔EN ==")
    for rec in RECORDS:
        if not rec["key"].endswith("_en"):
            continue
        partner_key = rec["key"].replace("_en", "_pt")
        relation_pt = {
            "identifier": results[partner_key]["doi"],
            "relation": "isTranslationOf",
            "resource_type": "publication-article",
        }
        rec["meta"]["related_identifiers"].append(relation_pt)
        update_metadata(s, rec["dep_id"], rec["meta"])
        print(f"    metadados atualizados ({rec['key']})")

    # 3. upload dos arquivos
    print("\n== 3/4 Fazendo upload de arquivos ==")
    for rec in RECORDS:
        dep_id = rec["dep_id"]
        print(f"  Upload {rec['key']}...")
        r_dep = s.get(f"{API}/deposit/depositions/{dep_id}", timeout=120).json()
        rec["files"] = {
            "paper.md": rec["folder"] / "paper.md",
            "paper.docx": rec["folder"] / "paper.docx",
            "paper.pdf": rec["folder"] / "paper.pdf",
        }
        if rec["key"].startswith("paper_b"):
            rec["files"]["omnimind_quantum_paper_b_canonical.db"] = Path("/home/fahbrain/projects/omnimind/data/quantum/omnimind_quantum_paper_b_canonical.db")
        if rec["key"].startswith("paper_a"):
            rec["files"]["omnimind_paper_a_mps_reproducao.sqlite"] = Path("/home/fahbrain/projects/omnimind-public-pulse/notebooks/omnimind-paper-a-mps-reproducao/omnimind_paper_a_mps_reproducao.sqlite")
            rec["files"]["mps_bridge_unified_results.json"] = Path("/home/fahbrain/projects/omnimind/docs/zenodo_packs/dodecatiad_v3_publication/paper/mps_bridge_unified_results.json")
            rec["files"]["multi_model_dodecatiad_comparison.json"] = Path("/home/fahbrain/projects/omnimind/data/quantum/transformer_mps_bridge/multi_model_dodecatiad_comparison.json")
        for name, fpath in rec["files"].items():
            print(f"    {name} ({fpath.stat().st_size} bytes)")
            upload_file(s, r_dep, fpath, name)

        # manifest
        manifest = build_manifest(rec)
        manifest_path = rec["folder"] / "MANIFEST.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        upload_file(s, r_dep, manifest_path, "MANIFEST.json")

    # 4. publica
    print("\n== 4/4 Publicando ==")
    for rec in RECORDS:
        print(f"  Publicando {rec['key']}...", end=" ")
        published = publish(s, rec["dep_id"])
        rec["published_doi"] = published["metadata"]["doi"]
        results[rec["key"]]["published_doi"] = rec["published_doi"]
        results[rec["key"]]["record_url"] = published["links"]["html"]
        print(f"OK {rec['published_doi']}")

    # 5. salva DOIs e atualiza READMEs
    DOIS_FILE.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    update_readme({k: v["published_doi"] for k, v in results.items()})
    print(f"\nDOIs salvos em: {DOIS_FILE}")
    for k, v in results.items():
        print(f"  {k}: {v['published_doi']}  -> {v['record_url']}")


if __name__ == "__main__":
    main()
