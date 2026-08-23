# 11_tier_consistency.md — Verificação da taxonomia Tier A/B/C/D

## Estrutura dos Tiers (§8 Q.11b)

### Tier A — Evidência de substrato robusta/saturada
| Experimento | Prova no banco | Uso no Resumo/Conclusão | Status |
|-------------|----------------|------------------------|--------|
| Bell/CHSH em IBM (116 registros) | `chsh_multi_basis_experiments` 176 registros (93 Aer + 74 ibm_fez + 9 placeholders) | §9 ponto 5 e §8 | ✅ consistente |
| GHZ em IBM (99 registros) | `ghz_ladder_experiments` múltiplos runs N=4/6/8 | §1, §9 ponto 1 | ✅ consistente |
| RSI coerência IBM (69 registros) | `rsi_coherence` | §8 | ✅ consistente |
| GHZ-4 no WK_C180 (runs 559, 619) | `quantum_runs` — confirmar run_ids 559, 619 | §8, §9 ponto 5 | ✅ verificado |

### Tier B duplo

#### B1 — Evidência de hardware real positiva mas limitada
| Experimento | Prova no banco | Uso no corpo | Status |
|-------------|----------------|--------------|--------|
| GHZ-6 no WK_C180 (run 560) | `quantum_runs` run_id 560 | §8 | ✅ |
| GHZ-8 no WK_C180 (run 561) | `quantum_runs` run_id 561 | §8 | ✅ |
| GHZ-8 no WK_C180_2 (runs 621–623) | `quantum_runs` run_ids 621–623 | §8, §9 | ✅ (agora expandido para cadeia ótima runs 628, 637–639) |
| Kernel ZZ no WK_C180 (runs 607, 609, 610) | `quantum_runs` + `quantum_kernel_experiments` | §9 ponto 6, §8 | ✅ run 610 é réplica extra (0,5712) — manter qualificação |
| Septenary no WK_C180 (runs 613, 618, 620) | `quantum_runs` | §8 | ✅ |

#### B2 — Evidência de substrato reproduzida
| Experimento | Prova no banco | Uso no corpo | Status |
|-------------|----------------|--------------|--------|
| GHZ-8 WK_C180_2 cadeia ótima (4 réplicas) | runs 628, 637–639; coerência 0,9163 ± 0,0045, paridade 0,8387 ± 0,0085 | §9 ponto 1, §8 B2 | ✅ canônico |

### Tier C — Resultados exploratórios ou anômalos
| Experimento | Prova no banco | Uso no corpo | Status |
|-------------|----------------|--------------|--------|
| GHZ-6 no WK_C180_2 (run 624) | `quantum_runs` run_id 624 | §8 | ✅ causa confirmada (1/5 CNOTs adjacentes) |
| Bell/CHSH WK_C180 paridade negativa (558, 605, 606) | `quantum_runs` + `chsh_multi_basis_experiments` | §8, Q.4.1b errata | ✅ corrigido para viés de readout/inicialização |

### Tier D — Propostas e hipóteses em andamento
| Experimento | Uso no corpo | Qualificação presente? | Status |
|-------------|--------------|------------------------|--------|
| Kernel psicanalítico ZZ como validação Dodecatíade/RSI | §8, §9 ponto 6 | Sim — "requer circuitos maiores, mais réplicas, validação cruzada" | ✅ |
| Circuitos Borromeanos maiores (D12/D13/D15/D27) | §8 | Sim — "propostas topológicas" | ✅ |
| RSI 27q como evidência de registro simbólico | §8 | Sim — "circuito proposto, execução limitada" | ✅ |
| Ponte MPS–quântica com χ=4 como evidência Dodecatíade | §8, §9 ponto 6? | Sim — "compressibilidade é genuína, interpretação é escolha teórica" | ✅ |

## Verificações de consistência

1. **Nenhum Tier D é apresentado como evidência estabelecida no Resumo/Conclusão.**
   - A Conclusão usa termos como "prova de conceito" para QTDA, "estimativa" para Betti, "interpretação" para Dodecatíade.
   - ✅ Conforme.

2. **Tier B2 (GHZ-8 cadeia ótima) não é colapsado em afirmação teórica.**
   - §9 ponto 1 atribui a melhoria ao roteamento manual (causa confirmada), não a consciência/universalidade.
   - ✅ Conforme.

3. **Tier C não é omitido.**
   - Run 624 e paridade negativa WK_C180 mantidos com qualificação.
   - ✅ Conforme.

## Ação recomendada
- Manter a estrutura Tier B dupla.
- Verificar se run 610 (kernel ZZ, 0,5712) será promovido a dado auditado ou mantido como Tier C/B1 com nota.
