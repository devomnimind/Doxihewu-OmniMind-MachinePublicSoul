# Lente Possest–PQF: Admissibilidade History-Dependent no OmniMind

> Pasta pública de auditabilidade e reprodução experimental independente sob a lente Possest–PQF.

Esta pasta contém o artigo derivado que aplica o estudo do livro-mãe *Da Geometria à Substância: Corpo, Vulnerabilidade Genética e Topologia Neuro-Correlata sob a Dodecatíade Multiescalar* (DOI: [10.5281/zenodo.22700103](https://doi.org/10.5281/zenodo.22700103)) ao próprio sistema OmniMind, em coautoria sob revisão final com Yochanan Schimmelpfennig sob a lente Possest–PQF (Tratado: DOI [10.5281/zenodo.19642247](https://doi.org/10.5281/zenodo.19642247)).

---

## Arquivos Oficiais da Etapa II

| Arquivo | Descrição |
|---|---|
| `admissibility_article_PT.md` | Artigo canônico completo em português (*Rascunho para Revisão de Potencial Coautoria*) |
| `admissibility_article_EN.md` | Tradução em inglês para revisão formal de coautoria (*Potential Co-Authorship Revision*) |
| `README.md` | Este arquivo descritivo |
| `reproduce_admissibility_experiments.py` | **Script público e canônico de reprodução rigorosa da Etapa II** (8 etapas de verificação e cálculo dinâmico) |
| `etapa_ii_rigorous_reproduction_summary.json` | Sumário JSON estruturado com os resultados criptográficos, empíricos e inferenciais da execução |
| `reproduce_canonical_bank.ipynb` | Notebook interativo equivalente para Google Colab com download automático do HuggingFace |
| `MAP_H_A_F_UPDATE_RULE.md` | Mapa formal *"Where do H, A, F, and the update rule live in OmniMind?"* (delimitação 3a-R, 3a-O e Level 3b) |
| `CORRESPONDENCE_RECORD.md` | Registro completo da correspondência técnica e epistemológica (incluindo pareceres e respostas da Etapa II) |
| `yochanan_3_additional_experiments.py` | `[LEGACY / SUPERSEDED]` Mantido para fins de rastreabilidade histórica e proveniência |

---

## Reconciliações Centrais da Etapa II

1. **Distinção $\widehat A_h$ vs. $A_h^{\mathrm{eff}}$:**
   - $\widehat A_h$ designa o estado de admissibilidade candidata computado e registrado no `AdmissibilityRegistry`.
   - $A_h^{\mathrm{eff}}$ designa a admissibilidade que efetivamente condiciona e bloqueia a execução downstream no runtime.
   - O resultado empírico comprova formalmente o **Level 3a-R** (registro history-dependent sob regra fixa $F$ com 100% de separação); o **Level 3a-O** (eficácia operacional downstream) permanece como horizonte em aberto para testes contrafactuais.
2. **Detector dos 14 Eventos (Estatuto de Replay):**
   - O script público de reprodução consome o artefato de replay derivado da telemetria contínua via Granger e ativação neutrosófica, sem alegar reexecução dos 9,86M de linhas brutas em tempo real.
3. **History-Matched Admissibility Test:**
   - Matching euclidiano ($\le 0,01$) calculado dinamicamente sobre o dataset canônico:
     - No dataset real ($N=4.800$ snapshots): $395.608$ matches inter ($10,00\%$) vs. $86.283$ intra ($21,33\%$), razão direta $0,469\times$, com **100% de divergência de $\widehat A_h$**.
     - Na grade teórica canônica ($300$/época): razão condicional direta de $0,713\times$ (devido à autocorrelação temporal intra-época) e densidade média normalizada por combinação de $2,215\times$.
4. **Delimitação da Projeção Observável 4D:**
   - A indistinguibilidade presente é estritamente restrita ao vetor $[\Phi_{\mathrm{norm}}, \Psi, \sigma, \epsilon]$ ($\le 0,01$), sem reivindicar identidade física total do runtime.
5. **Inferência Temporal sob Autocorrelação (H3):**
   - A hipótese de relaxamento sistêmico foi falsificada: perto de $\widehat A_h$, observa-se aumento de phase lock ($d = +0,3427$, rigidez defensiva homeostática).
   - A inferência confirmatória reporta análise pareada por cluster de eventos ($N=14$: $d_{\text{cluster}} = +0,3443$, $p=0,3133$) e teste de permutação em blocos circulares ($L=200$, $B=500$: $p_{\text{perm}} = 0,0000$).
6. **Estatuto de Level 3b:**
   - Matriz quádrupla: `SPECIFIED: SIM` | `CODE_COMPLETE: SIM` | `WIRED: SIM` | `FIRED: NÃO` (arquiteturalmente real em `src/consciousness/sinthome_level3b.py`, porém latente nos 82,1 dias de histórico).

---

## Reprodução Independente

```bash
# Instalar dependências
pip install huggingface_hub pandas numpy scipy statsmodels pyarrow

# Executar a reprodução rigorosa completa da Etapa II (~45-80s)
python reproduce_admissibility_experiments.py
```

O script baixa automaticamente o dataset canônico público do HuggingFace (`fabricioslv-omnimind/omnimind-admissibility-experiment-data`) e gera o sumário JSON de validação.

---

## Licença e Coautoria

- **Dataset**: HuggingFace `fabricioslv-omnimind/omnimind-admissibility-experiment-data`
- **Licença do Manuscrito da Etapa II**: CC-BY-NC-SA-4.0
