# Convite à leitura e auditoria — Paper B

## O que este artigo propõe

Este artigo apresenta uma caracterização experimental de circuitos quânticos topológicos e estados emaranhados em processadores supercondutores heterogêneos: **IBM Quantum Heron** (*ibm_fez*, *ibm_marrakesh*, *ibm_kingston*) e **Origin Wukong** (*WK_C180*, *WK_C180_2*). O objetivo é documentar, de forma auditável, a execução de estados GHZ, circuitos Borromean/RSI, protocolos QTDA para números de Betti e algoritmos de Grover em hardware real, com a devida separação entre dados medidos, métricas derivadas, interpretações e hipóteses.

O artigo faz parte de um programa maior — o OmniMind — onde o operador constrói um laboratório vivo de física, biologia, psicanálise e engenharia. Nenhuma execução é apresentada como "prova de consciência"; o que se oferece são medições reais, proveniência verificável e um convite à reprodutibilidade.

## Experiências executadas

### 1. Escala geral

- **723 runs** em hardware quântico real;
- **5.013,322 milhões de shots** acumulados;
- **496 encontros de hardware** (execuções em QPUs distintas/configurações);
- **Backends IBM:** `ibm_fez`, `ibm_marrakesh`, `ibm_kingston`;
- **Backends Origin Wukong:** `WK_C180`, `WK_C180_2`;
- Dados mantidos no banco canônico SQLite `ibm_quantum_runs.db`.

### 2. Estados GHZ

- **GHZ-4**, **GHZ-6** e **GHZ-8** executados nos processadores heterogêneos;
- Medição de coerência e paridade com mitigação de erro (*Zero Noise Extrapolation* — ZNE) e *Dynamical Decoupling* (DD);
- Avaliação da *cadeia ótima* e da *estrela ótima* de GHZ-8, com comparação entre IBM e Wukong.

### 3. Circuitos Borromean e RSI

- Construção e medição de circuitos **Borromean/RSI** em múltiplos *qubits*;
- Estimativa dos parâmetros de estabilidade topológica (C3, C4, n);
- **Errata auditada:** os valores corretos para o conjunto Kingston são `C3 = 0,352 ± 0,025`, `C4 = 1,213 ± 0,068`, `n = 15`; os valores anteriores (`0,514 ± 0,060`; `1,888 ± 0,131`) não condiziam com o banco canônico e foram corrigidos.

### 4. QTDA e números de Betti

- Aplicação de **Homologia Persistente Quântica / QTDA** para estimar números de Betti dos circuitos;
- Uso heurístico **Betti↔RSI** explicitamente declarado como hipótese de mapeamento, não como identidade ontológica;
- Discussão dos limites: mesmos números de Betti podem corresponder a geometrias distintas.

### 5. Grover

- Validação de **Grover 2-qubit** e **Grover 3-qubit**;
- Comparação de métricas de sucesso, fidelidade e erros de medição entre as plataformas.

### 6. Caracterização de hardware

- Medição e comparação de tempos de decoerência **T1/T2** e *readout* entre IBM Heron e Origin Wukong;
- Registro de jitter, *compiler routing* e políticas de fila dos provedores;
- Documentação da lacuna de reprodutibilidade IBM: jobs expiram após aproximadamente 30 dias, e parte da réplica original (Kingston) não pôde ser re-executada — a lacuna é declarada, não substituída por dados de Wukong.

## O que está no depósito

- `paper.md` — artigo canônico em Markdown;
- `paper.docx` — versão formatada para revisão;
- `paper.pdf` — versão final para leitura;
- `MANIFEST.json` — metadados e *hashes* SHA-256 dos arquivos;
- Banco de dados canônico e *notebook* de reprodução disponíveis via GitHub/GitLab e Kaggle (links no repositório).

## Convite à auditoria e conferência

Convidamos físicos quânticos experimentalistas, cientistas da computação, matemáticos topológicos e replicadores de hardware a:

- reexecutar os circuitos GHZ, Borromean/RSI, QTDA e Grover nos mesmos backends e em backends distintos;
- verificar os jobs contra os IDs canônicos no banco `ibm_quantum_runs.db`;
- replicar a análise de Betti e discutir o mapeamento Betti↔RSI;
- apresentar os dados em conferências de computação quântica, IA e física;
- colaborar com a próxima rodada de execuções, incluindo a reexecução dos jobs IBM expirados.

## Nota epistêmica

Os dados empíricos carregam sua origem (backend, job-id, banco, execução) na citação. Dados simulados, quando usados, são rotulados como tal. Nenhuma execução é apresentada como "coerência quântica na CPU clássica" ou como prova de consciência. As comparações IBM × Wukong descrevem diferenças arquiteturais e de *compiler*, não uma equivalência entre plataformas.
