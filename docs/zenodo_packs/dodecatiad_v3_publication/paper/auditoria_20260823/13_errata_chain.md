# 13_errata_chain.md — Cadeia de erratas e atualizações do Paper B

## Regra de registro
Cada marcador de errata/atualização contém: `marcador`, `data`, `secao`, `afirmacao_original`, `valor_canonico_atual`, `propagado_para_resumo`, `propagado_para_conclusao`, `status`.

## Registros

### 1. Contagem de runs e shots
| campo | valor |
|---|---|
| marcador | ATUALIZADO 2026-08-08, 2026-08-21, 2026-08-23 |
| data | 2026-08-23 |
| secao | Cabecalho, Resumo, Introducao, Conclusao, Apendice V.0, V.7 |
| afirmacao_original | 645 runs, 489 hardware_encounters, 4.919.370 shots; 713 runs, 5.00M shots |
| valor_canonico_atual | 723 runs (719 IBM + 4 Grover Wukong), 496 hardware_encounters, 5.013.322 milhoes de shots |
| propagado_para_resumo | sim |
| propagado_para_conclusao | sim |
| status | resolvido |
| observacao | Contagem final obtida de `quantum_runs` + `hardware_encounters`; 4.919.370 era pre-ingestao final |

### 2. GHZ-8 cadeia otima WK_C180_2
| campo | valor |
|---|---|
| marcador | ATUALIZADO 2026-08-21 |
| data | 2026-08-21 |
| secao | Q.7.5, Resumo, Conclusao |
| afirmacao_original | GHZ-8 coerencia 0.8636, cadeia original (5/7 adjacentes) |
| valor_canonico_atual | GHZ-8 cadeia otima: coerencia 0.9163 ± 0.0045, paridade 0.8387 ± 0.0085, 4 replicas; cadeia original 0.8636 ± 0.0114, 3 replicas; expandida problematica 0.6104 ± 0.3996, 10 replicas |
| propagado_para_resumo | sim |
| propagado_para_conclusao | sim |
| status | resolvido |
| observacao | Cadeia [38,47,56,65,74,84,75,66] elimina estado |00001111> com 99.97% de reducao |

### 3. Borromean C3/C4
| campo | valor |
|---|---|
| marcador | ERRATA TECNICA 2026-08-23 |
| data | 2026-08-23 |
| secao | Resumo, Q.8, Tabela Q.48, Conclusao |
| afirmacao_original | C3 = 0.514 ± 0.060, C4 = 1.888 ± 0.131; limiar C4 > 1.0 |
| valor_canonico_atual | E (ibm_kingston): C3 = 0.352 ± 0.025, C4 = 1.213 ± 0.068 (n=15); C4 > 0 (indice de covariancia/amplificacao escalado 16x, nao fidelidade 1-normalizada) |
| propagado_para_resumo | sim |
| propagado_para_conclusao | sim |
| status | resolvido |
| observacao | Valores anteriores superestimados; formula correta aplicada sobre counts_json |

### 4. CHSH 360 grid
| campo | valor |
|---|---|
| marcador | Nota de auditoria 2026-08-23 |
| data | 2026-08-23 |
| secao | Q.4.1, Resumo, Conclusao |
| afirmacao_original | S_max = 2.901 em (190, 235); 50.2% violacoes; grid no banco canônico |
| valor_canonico_atual | S_max = 2.943 em (60, 105); 2590/5184 violacoes (49.96%); grid e simulacao Aer ideal em `data/quantum/frontier_experiments.json` (kaggle_cpu), nao hardware |
| propagado_para_resumo | sim |
| propagado_para_conclusao | sim |
| status | resolvido |
| observacao | Tsirelson = 2.828; excedente 0.115 atribuivel a ruido estatistico finito (1024 shots) |

### 5. E7 GHZ-8 star DD+ZNE
| campo | valor |
|---|---|
| marcador | Nota de auditoria 2026-08-23 |
| data | 2026-08-23 |
| secao | Q.9.4, Q.49, Resumo, Conclusao |
| afirmacao_original | dd_zne scale=2 = 0.843 ± 0.026 (n=3); 0.8426; 0.8421 sem distincao de coorte |
| valor_canonico_atual | 0.8421 e media de ghz_coherence_zne para estrategia dd_zne (n=9, re-execucao 2026-07-30, Tabela V.49b); dd_zne scale=2 bruto = 0.836 ± 0.005 (n=3, campanha original); dd_zne scale=2 original = 0.843 ± 0.026 (n=3) e valor do relatorio original, nao bruto canônico |
| propagado_para_resumo | sim |
| propagado_para_conclusao | sim |
| status | parcialmente resolvido |
| observacao | Duas coortes (2026-07-29 original e 2026-07-30 re-execucao) com estimadores diferentes; nao intercambiaveis. Tabela V.49b detalhada por scale: zne scale=2 N=2 (r0 faltante d9ld8ujjf64c739jc7jg); dd_zne ZNE agregado n=3 (scale=1) => 0.8421 |

### 6. Q.47a ibm_fez N=8-star
| campo | valor |
|---|---|
| marcador | Nota de auditoria 2026-08-23 |
| data | 2026-08-23 |
| secao | Q.7.7, Tabela Q.47a, Q.9.4, Conclusao |
| afirmacao_original | coh = 0.634, par = 0.711, depth = 43 para ibm_fez N=8-star |
| valor_canonico_atual | media dos 4 runs sem mitigacao: coh = 0.723 ± 0.064, par = 0.787 ± 0.053; 0.634 e pior run (id=96, job_id=d9kvr48ii2cc); depth=43 nao localizado (transpiled_depth=NULL) |
| propagado_para_resumo | sim (qualificado) |
| propagado_para_conclusao | sim (qualificado) |
| status | resolvido com ressalva |
| observacao | depth=43 permanece com proveniencia nao reconciliada |

### 7. Contagem ibm_job_queue
| campo | valor |
|---|---|
| marcador | Nota de integridade 2026-08-21 |
| data | 2026-08-21 |
| secao | Inicio (evidence summary) |
| afirmacao_original | 375 jobs na fila podem contaminar contagens |
| valor_canonico_atual | 375 registros em ibm_job_queue (176 CANCELLED, 69 ERROR, 10 QUEUED, 120 DONE/COMPLETED) sao separados de quantum_runs; 43 job_ids em ambas as tabelas sao DONE/COMPLETED |
| propagado_para_resumo | sim |
| propagado_para_conclusao | nao |
| status | resolvido |
| observacao | ZERO jobs CANCELLED/ERROR/QUEUED contaminam os 723 runs |

### 8. E7 cross-backend ibm_kingston QUEUED
| campo | valor |
|---|---|
| marcador | Pendencia V.6 [~] |
| data | 2026-07-30 / reauditoria 2026-08-23 |
| secao | V.6, Q.9.4 |
| afirmacao_original | 16 jobs QUEUED em 2026-07-30, coleta pendente |
| valor_canonico_atual | 26 runs GHZ-8 star em ibm_kingston coletados e DONE (job_queue status=DONE); media coh = 0.812 ± 0.025, par = 0.855 ± 0.020; todos sem mitigacao |
| propagado_para_resumo | nao |
| propagado_para_conclusao | nao ainda |
| status | resolvido |
| observacao | Atualizar V.6 e Q.9.4 se desejar incluir ibm_kingston no comparativo E7 |

### 9. QTDA proveniencia
| campo | valor |
|---|---|
| marcador | [ATUALIZADO / nota em V.6] |
| data | 2026-08-23 |
| secao | Q.10, Conclusao ponto 4 |
| afirmacao_original | job_id d9l8t8gii2cc73eh61k0 corrigido; quantum_runs.run_id nao cruzado |
| valor_canonico_atual | QTDA rsi_borromean em ibm_kingston: id=26 na tabela qtda_betti_experiments, job_id d9l8t8gii2cc73eh61k0, P(000) 0.3943/0.1941/0.1750, beta0/1/2 = 1.536/4.152/4.713; prova de conceito de baixa resolucao |
| propagado_para_resumo | sim |
| propagado_para_conclusao | sim |
| status | resolvido |
| observacao | Nao esta em quantum_runs, mas em qtda_betti_experiments |

### 10. Anomalia bit-ordering WK_C180
| campo | valor |
|---|---|
| marcador | ERRATA 2026-08-21; ATUALIZADO 2026-08-21 |
| data | 2026-08-21 |
| secao | Q.4.1b, Q.14 |
| afirmacao_original | Diferenca de bit-ordering pyqpanda3 vs Qiskit |
| valor_canonico_atual | pyqpanda3 usa mesma convencao de bit-ordering que Qiskit (q0 = LSB); anomalia de paridade negativa em 558/605/606/608 e explicada por viés de readout/inicializacao |
| propagado_para_resumo | nao |
| propagado_para_conclusao | nao |
| status | resolvido |
| observacao | Ver Apendice Q.14 |

### 11. Kernel ZZ silhouette 0.5712 (run 610)
| campo | valor |
|---|---|
| marcador | ATUALIZADO 2026-08-21 |
| data | 2026-08-21 |
| secao | Q.2, Apendice Q.2.7 |
| afirmacao_original | silhouette 0.5712 run 610 como dado auditado |
| valor_canonico_atual | 0.5712 e uma replica adicional nao reconciliada; valor canônico positivo e silhouette_quantum = 0.6412 (WK_C180 run 609) |
| propagado_para_resumo | sim (0.6412) |
| propagado_para_conclusao | sim (0.6412) |
| status | resolvido |
| observacao | 0.5712 deve ser mantido como B1/Tier C com nota se citado |

## Cadeia de custodia
Para cada errata acima, o valor canonico atual foi obtido de:
- `data/quantum/omnimind_quantum_paper_b_canonical.db` (tabelas `quantum_runs`, `ghz_ladder_experiments`, `borromean_knot_experiments`, `chsh_multi_basis_experiments`, `qtda_betti_experiments`, `quantum_kernel_experiments`)
- `data/quantum/frontier_experiments.json` (CHSH 360)
- `data/quantum/omnimind_quantum_paper_b_canonical.db` (banco sanitizado publico, dataset Kaggle)

### 12. Lacuna E7 zne scale=2 r0
|| campo | valor |
||---|---|
|| marcador | ATUALIZADO 2026-08-23 |
|| data | 2026-08-23 |
|| secao | Apendice V.3, Q.9.3, Tabela V.49b, Tabela Q.49 |
|| afirmacao_original | zne scale=2 N=3 na re-execucao; r0 coletado |
|| valor_canonico_atual | zne scale=2 N=2 (r1, r2) na re-execucao; r0 (d9ld8ujjf64c739jc7jg) expirou e nao foi coletado. Lacuna aceita; nao substituida por dados Wukong. Tabelas ajustadas para N=2. dd_zne permanece N=9 (3+3+3). |
|| propagado_para_resumo | nao |
|| propagado_para_conclusao | nao |
|| status | resolvido com ressalva |
|| observacao | Decisao editorial: nao reproduzir no Wukong por incompatibilidade arquitetural (180q esparsa, pyqpanda3, API de mitigacao distinta). |

## Recomendacoes finais
- Nenhum valor antigo permanece sem ponteiro para o canonico.
- Pendencias menores: (a) depth=43 em Q.47a; (b) Paper A ainda cita §3.1.6/§3.1/§3.5 (secionamento do artigo unificado) que nao mapeia 1:1 para Paper B split.
