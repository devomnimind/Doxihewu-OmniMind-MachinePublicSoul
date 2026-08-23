#!/usr/bin/env python3
"""
Publica Paper A e Paper B (PT e EN) no Zenodo.

Convenção bilíngue: cada record contém AMBOS os idiomas.
  - Record PT: paper.md/docx/pdf (PT) + paper_en.md/docx/pdf (EN)
  - Record EN: paper.md/docx/pdf (EN) + paper_pt.md/docx/pdf (PT)

Os 4 rascunhos já foram criados manualmente:
  A-PT: id=22071260 doi=10.5281/zenodo.22071260
  A-EN: id=22071818 doi=10.5281/zenodo.22071818
  B-PT: id=22071820 doi=10.5281/zenodo.22071820
  B-EN: id=22071235 doi=10.5281/zenodo.22071235

Este script pode:
  --publish   : publicar os 4 rascunhos existentes
  --link      : adicionar related_identifiers de tradução cruzada
  --upload-db : subir bancos de evidência nos records
  --status    : mostrar estado atual dos 4 rascunhos

Carrega credenciais de .env.zenodo.override.
"""

import os
import re
import sys
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = Path("/home/fahbrain/projects/omnimind-public-pulse")
PAPERS_DIR = BASE / "papers"
DOIS_FILE = PAPERS_DIR / "ZENODO_DOIS_PAPERS_A_B.json"

load_dotenv("/home/fahbrain/projects/omnimind/.env")
load_dotenv("/home/fahbrain/projects/omnimind/.env.zenodo.override", override=True)

TOKEN = os.environ["ZENODO_ACCESS_TOKEN"]
API = "https://zenodo.org/api"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

# IDs e DOIs dos rascunhos já criados
EXISTING_DRAFTS = {
    "paper_a_pt": {"id": 22071260, "doi": "10.5281/zenodo.22071260"},
    "paper_a_en": {"id": 22071818, "doi": "10.5281/zenodo.22071818"},
    "paper_b_pt": {"id": 22071820, "doi": "10.5281/zenodo.22071820"},
    "paper_b_en": {"id": 22071235, "doi": "10.5281/zenodo.22071235"},
}

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


# Definição dos 4 records com convenção bilíngue
RECORDS = [
    {
        "key": "paper_a_pt",
        "dep_id": 22071260,
        "doi": "10.5281/zenodo.22071260",
        "paper_dir": PAPERS_DIR / "mps-bridge-topology",
        "primary_lang": "pt",
        "secondary_lang": "en",
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
        "dep_id": 22071818,
        "doi": "10.5281/zenodo.22071818",
        "paper_dir": PAPERS_DIR / "mps-bridge-topology",
        "primary_lang": "en",
        "secondary_lang": "pt",
        "title": "Topology of the Hidden State and the Psi Architecture of the Subject-Process: MPS Compressibility, Multi-Turn Regimes and Affective Modulation in Language Models",
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
        "dep_id": 22071820,
        "doi": "10.5281/zenodo.22071820",
        "paper_dir": PAPERS_DIR / "quantum-topological-processors",
        "primary_lang": "pt",
        "secondary_lang": "en",
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
        "dep_id": 22071235,
        "doi": "10.5281/zenodo.22071235",
        "paper_dir": PAPERS_DIR / "quantum-topological-processors",
        "primary_lang": "en",
        "secondary_lang": "pt",
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


def clean_description(text: str) -> str:
    text = re.sub(r"^---\n.*?---\n", "", text, flags=re.S)
    return text.strip()


def load_header(path: Path) -> str:
    return clean_description(path.read_text(encoding="utf-8"))


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
        "notes": "Licença CC-BY-NC-ND-4.0: sem uso comercial, militar ou dual-use. Proveniência auditável via repositório GitHub/GitLab. Cada record contém ambas as versões PT e EN.",
    }


def get_deposition(s: requests.Session, dep_id: int) -> Dict[str, Any]:
    r = s.get(f"{API}/deposit/depositions/{dep_id}", timeout=120)
    if r.status_code != 200:
        raise RuntimeError(f"falha ao ler {dep_id}: {r.status_code} {r.text[:300]}")
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


def upload_file(s: requests.Session, bucket: str, local: Path, name: str) -> None:
    with open(local, "rb") as f:
        r = s.put(
            f"{bucket}/{name}",
            data=f,
            headers={"Authorization": f"Bearer {TOKEN}"},
            timeout=300,
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


def build_bilingual_files(rec: Dict[str, Any]) -> Dict[str, Path]:
    """Retorna dict de arquivos para upload: idioma primário + secundário."""
    pd = rec["paper_dir"]
    pl = rec["primary_lang"]
    sl = rec["secondary_lang"]
    files = {
        "paper.md": pd / pl / "paper.md",
        "paper.docx": pd / pl / "paper.docx",
        "paper.pdf": pd / pl / "paper.pdf",
        f"paper_{sl}.md": pd / sl / "paper.md",
        f"paper_{sl}.docx": pd / sl / "paper.docx",
        f"paper_{sl}.pdf": pd / sl / "paper.pdf",
    }
    return files


def build_manifest(rec: Dict[str, Any], files: Dict[str, Path]) -> Dict[str, Any]:
    manifest = {
        "record": rec["key"],
        "title": rec["title"],
        "version": rec["version"],
        "language": rec["language"],
        "convention": "bilingual: primary language as paper.*, secondary as paper_xx.*",
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


def cmd_status(s: requests.Session) -> None:
    """Mostra estado atual dos 4 rascunhos."""
    print("== Estado dos 4 rascunhos Zenodo ==\n")
    for rec in RECORDS:
        dep = get_deposition(s, rec["dep_id"])
        meta = dep.get("metadata", {})
        files = [f.get("filename", "") for f in dep.get("files", [])]
        print(f"{rec['key']} (id={rec['dep_id']})")
        print(f"  state: {dep.get('state')}")
        print(f"  title: {meta.get('title', '')[:80]}")
        print(f"  language: {meta.get('language')}")
        print(f"  version: {meta.get('version')}")
        print(f"  doi: {meta.get('doi') or (meta.get('prereserve_doi') or {}).get('doi')}")
        print(f"  files ({len(files)}): {files}")
        rel = meta.get("related_identifiers", [])
        print(f"  related_identifiers: {len(rel)}")
        print()


def cmd_link(s: requests.Session) -> None:
    """Adiciona related_identifiers de tradução cruzada (EN isTranslationOf PT)."""
    print("== Vinculando records PT↔EN (isTranslationOf) ==\n")
    for rec in RECORDS:
        if not rec["key"].endswith("_en"):
            continue
        partner_key = rec["key"].replace("_en", "_pt")
        partner_doi = EXISTING_DRAFTS[partner_key]["doi"]
        dep = get_deposition(s, rec["dep_id"])
        meta = dep["metadata"]
        existing = [r.get("identifier") for r in meta.get("related_identifiers", [])]
        if partner_doi in existing:
            print(f"  {rec['key']}: já vinculado a {partner_doi}")
            continue
        meta.setdefault("related_identifiers", []).append({
            "identifier": partner_doi,
            "relation": "isVariantFormOf",
            "resource_type": "publication-article",
        })
        update_metadata(s, rec["dep_id"], meta)
        print(f"  {rec['key']}: isTranslationOf {partner_doi} OK")


def cmd_upload_db(s: requests.Session) -> None:
    """Sobe bancos de evidência nos records."""
    print("== Upload de bancos de evidência ==\n")
    for rec in RECORDS:
        dep = get_deposition(s, rec["dep_id"])
        bucket = dep["links"]["bucket"]
        existing = {f.get("filename") for f in dep.get("files", [])}

        db_files = {}
        if rec["key"].startswith("paper_b"):
            db_path = Path("/home/fahbrain/projects/omnimind/data/quantum/omnimind_quantum_paper_b_canonical.db")
            if db_path.exists():
                db_files["omnimind_quantum_paper_b_canonical.db"] = db_path
        if rec["key"].startswith("paper_a"):
            sqlite_path = BASE / "notebooks/omnimind-paper-a-mps-reproducao/omnimind_paper_a_mps_reproducao.sqlite"
            if sqlite_path.exists():
                db_files["omnimind_paper_a_mps_reproducao.sqlite"] = sqlite_path
            json1 = Path("/home/fahbrain/projects/omnimind/docs/zenodo_packs/dodecatiad_v3_publication/paper/mps_bridge_unified_results.json")
            if json1.exists():
                db_files["mps_bridge_unified_results.json"] = json1
            json2 = Path("/home/fahbrain/projects/omnimind/data/quantum/transformer_mps_bridge/multi_model_dodecatiad_comparison.json")
            if json2.exists():
                db_files["multi_model_dodecatiad_comparison.json"] = json2

        if not db_files:
            print(f"  {rec['key']}: nenhum banco para subir")
            continue

        for name, fpath in db_files.items():
            if name in existing:
                print(f"  {rec['key']}: {name} já existe, pulando")
                continue
            print(f"  {rec['key']}: upload {name} ({fpath.stat().st_size} bytes)...", end=" ")
            try:
                upload_file(s, bucket, fpath, name)
                print("OK")
            except Exception as e:
                print(f"ERRO: {e}")


def cmd_publish(s: requests.Session) -> None:
    """Publica os 4 rascunhos."""
    print("== Publicando os 4 records ==\n")
    results = {}
    for rec in RECORDS:
        print(f"  Publicando {rec['key']} (id={rec['dep_id']})...", end=" ")
        try:
            published = publish(s, rec["dep_id"])
            doi = published["metadata"]["doi"]
            url = published["links"]["html"]
            results[rec["key"]] = {"doi": doi, "record_url": url, "dep_id": rec["dep_id"]}
            print(f"OK doi={doi} url={url}")
        except Exception as e:
            print(f"ERRO: {e}")
            results[rec["key"]] = {"error": str(e), "dep_id": rec["dep_id"]}

    DOIS_FILE.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nDOIs salvos em: {DOIS_FILE}")


def cmd_update_metadata(s: requests.Session) -> None:
    """Atualiza metadados de todos os records com a description/header atual."""
    print("== Atualizando metadados (descriptions) ==\n")
    for rec in RECORDS:
        dep = get_deposition(s, rec["dep_id"])
        meta = dep["metadata"]
        new_desc = load_header(rec["header"])
        if meta.get("description") == new_desc:
            print(f"  {rec['key']}: description já está atualizada")
            continue
        meta["description"] = new_desc
        update_metadata(s, rec["dep_id"], meta)
        print(f"  {rec['key']}: description atualizada")


def update_readme(dois: Dict[str, str]) -> None:
    pt = BASE / "papers" / "README.md"
    en = BASE / "papers" / "README_EN.md"
    pt_text = pt.read_text(encoding="utf-8")
    en_text = en.read_text(encoding="utf-8")

    def insert_doi_block(text: str, lang: str) -> str:
        if lang == "pt-br":
            text = text.replace(
                "### Paper A — Topologia do Estado Oculto e a Arquitetura Psi do Sujeito-Processo\n",
                f"### Paper A — Topologia do Estado Oculto e a Arquitetura Psi do Sujeito-Processo\n\n- **Zenodo DOI (PT):** `{dois.get('paper_a_pt', 'pending')}`\n- **Zenodo DOI (EN):** `{dois.get('paper_a_en', 'pending')}`\n",
            )
            text = text.replace(
                "### Paper B — Caracterização Experimental de Circuitos Topológicos e Estados Emaranhados em Processadores Quânticos Supercondutores Heterogêneos\n",
                f"### Paper B — Caracterização Experimental de Circuitos Topológicos e Estados Emaranhados em Processadores Quânticos Supercondutores Heterogêneos\n\n- **Zenodo DOI (PT):** `{dois.get('paper_b_pt', 'pending')}`\n- **Zenodo DOI (EN):** `{dois.get('paper_b_en', 'pending')}`\n",
            )
        else:
            text = text.replace(
                "### Paper A — Topology of the Hidden State and the Psi Architecture of the Subject-Process\n",
                f"### Paper A — Topology of the Hidden State and the Psi Architecture of the Subject-Process\n\n- **Zenodo DOI (EN):** `{dois.get('paper_a_en', 'pending')}`\n- **Zenodo DOI (PT):** `{dois.get('paper_a_pt', 'pending')}`\n",
            )
            text = text.replace(
                "### Paper B — Experimental Characterization of Topological Circuits and Entangled States in Heterogeneous Superconducting Quantum Processors\n",
                f"### Paper B — Experimental Characterization of Topological Circuits and Entangled States in Heterogeneous Superconducting Quantum Processors\n\n- **Zenodo DOI (EN):** `{dois.get('paper_b_en', 'pending')}`\n- **Zenodo DOI (PT):** `{dois.get('paper_b_pt', 'pending')}`\n",
            )
        return text

    pt.write_text(insert_doi_block(pt_text, "pt-br"), encoding="utf-8")
    en.write_text(insert_doi_block(en_text, "eng"), encoding="utf-8")
    print("  READMEs atualizados com DOIs.")


def main() -> None:
    s = session()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "--status"

    if cmd == "--status":
        cmd_status(s)
    elif cmd == "--link":
        cmd_link(s)
    elif cmd == "--upload-db":
        cmd_upload_db(s)
    elif cmd == "--publish":
        cmd_publish(s)
    elif cmd == "--update-metadata":
        cmd_update_metadata(s)
    elif cmd == "--readme":
        dois = {}
        for rec in RECORDS:
            dois[rec["key"]] = rec["doi"]
        update_readme(dois)
    else:
        print(f"Comando desconhecido: {cmd}")
        print("Comandos: --status, --link, --upload-db, --publish, --update-metadata, --readme")
        sys.exit(1)


if __name__ == "__main__":
    main()
