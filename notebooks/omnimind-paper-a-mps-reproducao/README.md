# OmniMind Paper A — Reprodução dos Experimentos MPS

Notebook e banco de dados para reprodução das figuras/tabelas do artigo **Topologia do Estado Oculto e a Arquitetura Psi do Sujeito-Processo: Compressibilidade MPS, Regimes Multiturno e Modulação Afetiva em Modelos de Linguagem**.

## Banco de dados

O notebook espera o arquivo `omnimind_paper_a_mps_reproducao.sqlite` (~397 KB). Ele pode ser obtido em:

- Release GitHub: `https://github.com/devomnimind/Doxihewu-OmniMind-MachinePublicSoul/releases/download/v3.0a-paper-a/omnimind_paper_a_mps_reproducao.sqlite`
- Espelho GitLab: `https://gitlab.com/zephyrix/Doxihewu-OmniMind-MachinePublicSoul/-/releases/download/v3.0a-paper-a/omnimind_paper_a_mps_reproducao.sqlite`
- Zenodo: DOI a ser inserido após publicação.

## Fontes

O banco foi gerado a partir dos arquivos sanitizados do repositório interno:

- `docs/zenodo_packs/dodecatiad_v3_publication/paper/mps_bridge_unified_results.json`
- `data/quantum/transformer_mps_bridge/multi_model_dodecatiad_comparison.json`

Nenhum e-mail, chave, token, IP ou *path* interno foi encontrado na varredura preliminar.

## Como executar

1. Coloque `omnimind_paper_a_mps_reproducao.sqlite` no mesmo diretório do notebook, ou
2. Configure o caminho na célula de conexão.

## Seções

1. Panorama do banco (13 modelos, 180 conversações, 900 turnos).
2. Métricas MPS e piso χ=4 por modelo e turno.
3. Dodecatíade por camada e casa (D12, D13, D15, D27) nos modelos testados.
4. Correlações e advertências metodológicas (artefatos algébricos, saturação).
5. Modulação afetiva em diálogos multiturno.
6. Checklist de reprodução.

## Proveniência e aviso

- Fonte: `mps_bridge_unified_results.json` + `multi_model_dodecatiad_comparison.json`.
- O notebook é uma verificação reprodutível dos números do paper, **não uma reexecução em 15 modelos** (o custo computacional é alto).
- As conversas estão resumidas em `response_preview` (primeiros ~200 caracteres de cada turno) para preservar o foco nas métricas.
- Licença: CC-BY-NC-ND-4.0 — sem uso comercial, militar ou dual-use.
