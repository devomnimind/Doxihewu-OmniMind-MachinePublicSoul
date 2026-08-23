# OmniMind Paper B — Reproducao de Experimentos Quanticos

Notebook de reproducao das figuras/tabelas do artigo **Caracterizacao Experimental de Circuitos Topologicos e Estados Emaranhados em Processadores Quanticos Supercondutores Heterogeneos (IBM Quantum e Origin Wukong)**.

## Banco de dados

O notebook espera o arquivo `omnimind_quantum_paper_b_canonical.db` (15,9 MB). Ele pode ser obtido em:

- Release GitHub: `https://github.com/devomnimind/Doxihewu-OmniMind-MachinePublicSoul/releases/download/v3.0c-paper-b/omnimind_quantum_paper_b_canonical.db`
- Espelho GitLab: `https://gitlab.com/zephyrix/Doxihewu-OmniMind-MachinePublicSoul/-/releases/download/v3.0c-paper-b/omnimind_quantum_paper_b_canonical.db`
- Kaggle Dataset: anexado a este notebook na aba *Data* (`omnimind-quantum-paper-b`).

## Como executar

1. Coloque o banco no mesmo diretorio do notebook, ou
2. Configure-o como dataset/input no Kaggle em `/kaggle/input/omnimind-quantum-paper-b/omnimind_quantum_paper_b_canonical.db`.

## Secoes

1. Panorama do banco (713 runs, 5.000.010 shots, 489 hardware encounters).
2. GHZ-8: cadeia antiga vs cadeia otima no Origin Quantum `WK_C180_2`.
3. Grover validator no Wukong (2q e 3q).
4. Kernel ZZ borromeaniano (Aer, IBM, Wukong).
5. T1/T2 por backend.
6. C4 de covariancia tetrapartite (variante E com Sinthome).
7. QTDA Betti numbers.
8. Checklist de reproducao.

## Procedencia e aviso

- Fonte: banco `omnimind_quantum_paper_b_canonical.db`, gerado a partir do snapshot interno `ibm_quantum_runs.db` com paths e erros de importacao redigidos.
- O notebook e uma verificacao reprodutivel dos numeros do paper, **nao uma reexecucao de hardware quantico**.
- Registros de falhas (por exemplo, erro de importacao `LinearFunction` no Qiskit) foram preservados como proveniencia, mas claramente marcados como `redacted`/`failure`.
