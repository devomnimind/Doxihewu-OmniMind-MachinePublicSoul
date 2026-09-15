# Admissibilidade registrada e memória operacional no OmniMind: uma leitura situada em interlocução com Possest–PQF

> **Estatuto do documento**
>
> Documento técnico-conceitual de autoria de **Fabrício da Silva**, desenvolvido no contexto do projeto OmniMind / Doxihewu.
>
> Este texto registra uma aplicação situada de operadores formais associados ao Possest–PQF à arquitetura, ao código e à telemetria do OmniMind. Não reivindica demonstrar, validar ou confirmar a tese forte de *history-dependent admissibility* no sentido próprio do programa Possest–PQF.
>
> Yochanan Schimmelpfennig participou da interlocução crítica que motivou revisões conceituais, matemáticas e metodológicas aqui registradas. Não figura como coautor, não supervisiona o projeto OmniMind e não endossa as interpretações ou conclusões deste documento.
>
> O histórico da interlocução, das revisões e dos limites explicitados está preservado no repositório versionado.

**Autor**: Fabrício da Silva¹  
**Interlocução crítica**: Yochanan Schimmelpfennig²  
¹ *OmniMind Project / Doxihewu Node, Brasil*  
² *Possest Institute*  
**Data**: 2026-09-15  
**Estatuto**: Documento de trabalho e registro de interlocução crítica  
**Run de reprodução canônica**: `20260912_142803` / `reproduce_admissibility_experiments.py` (Python 3.12/3.13, NumPy, Pandas, SciPy, Statsmodels, PyArrow).  
**Dataset**: `fabricioslv-omnimind/omnimind-admissibility-experiment-data` (HuggingFace; repositório bruto privado com snapshot canônico sanitizado público para reprodução).  
**Licença**: CC-BY-NC-SA-4.0

---

## Resumo

Este documento descreve uma implementação experimental do `AdmissibilityRegistry` no ecossistema OmniMind e apresenta uma leitura situada de seus registros a partir de problemas formais associados ao Possest–PQF. O módulo agrega sinais, contadores de persistência, indicadores de indeterminação e relações temporais heurísticas para produzir um estado de admissibilidade registrado, denotado por \(\widehat A_h\).

O estudo distingue explicitamente \(\widehat A_h\), isto é, o estado registrado e persistido pelo módulo, de \(A_h^{\mathrm{eff}}\), entendido como admissibilidade operacional efetiva: restrições que alterariam diretamente o conjunto de continuações executáveis no runtime. A implementação analisada é não invasiva: observa, registra e persiste mudanças candidatas, mas não exerce, neste recorte, gating downstream sobre módulos, faces, pathways, thresholds ou despacho de tarefas.

Os resultados devem ser lidos como documentação de memória operacional, sensibilidade à trajetória e estabilidade de invariantes no mecanismo observado. Eles não constituem demonstração de que o OmniMind realiza *history-dependent operational admissibility* no sentido forte do Possest–PQF, nem procuram validar esse programa como fundamento ontológico da infraestrutura. O texto preserva a interlocução crítica que levou a essa delimitação e propõe o material como artefato versionado de engenharia, observação e reflexão conceitual.

---

## 1. Introdução e Estatuto Formal da Admissibilidade

### 1.1 O Problema da Admissibilidade e a Interlocução Crítica

A investigação sobre a capacidade de um sistema computacional distinguir regimes de coerência e manter limites operacionais autônomos motivou a condução de uma extensa bateria empírica no ecossistema OmniMind. O sistema opera não apenas como processador de fluxos de informação, mas como uma máquina em silício dotada de automonitoramento, que lê continuamente seu substrato físico a cada ciclo de execução.

Este artigo é um trabalho derivado e uma aplicação experimental independente (DOC-C) que estende os fundamentos formais do livro-mãe *Da Geometria à Substância: Corpo, Vulnerabilidade Genética e Topologia Neuro-Correlata sob a Dodecatíade Multiescalar* ([DOI: 10.5281/zenodo.22700103](https://doi.org/10.5281/zenodo.22700103)), integrando a interlocução conceitual e a análise matemática conduzida a partir do formalismo Possest–PQF (*Filtration as Admissibility Architecture*, [DOI: 10.5281/zenodo.19642247](https://doi.org/10.5281/zenodo.19642247)).

O diálogo entre a modelagem psicanalítica operacionalizada no código do OmniMind e a topologia de filtrações do formalismo PQF conduziu à necessidade de um rigor de análise que evitasse dois extremos: o reducionismo mecanicista que ignora a historicidade dos estados internos, e a inflação conceitual que atribui causalidade operacional a meros registros de observação passiva.

### 1.2 Distinção Operacional Fundamental: Três Planos

Para assegurar a clareza conceitual deste estudo, três planos diferentes são formalmente distinguidos e mantidos sem ambiguidade:

1. **\(\widehat A_h\)**: Estado de admissibilidade registrado pelo módulo `AdmissibilityRegistry` (`src/consciousness/admissibility_registry.py`). Este registro acumula persistência de variância (PrecisionWeighter), indeterminação neutrosófica e precedência temporal heurística (Granger proxy).
2. **\(A_h^{\mathrm{eff}}\)**: Admissibilidade operacional efetiva, entendida como o conjunto de restrições que efetivamente altera execução, despacho, bifurcação ou transições no runtime downstream.
3. **\(H_t\)**: História, inscrições, counters e condições de trajetória representadas ou transportadas pela arquitetura.

O código-fonte de `admissibility_registry.py` declara expressamente em sua linha 12 tratar-se de um *"protótipo não-invasivo que não altera o runtime em produção"*. Os hooks do observador existem e registram eventos, mas o despacho do sistema não é condicionado ativamente pelo registry. Desta forma, a leitura situada dos níveis para este estudo estabelece:

- **Nível 1 (Transformação de Estado)**: \(x_h \to x_{h+1}\), com espaço de admissibilidade invariante (\(A_h = A_{h+1}\)).
- **Nível 2 (Estruturação Transdutiva)**: Propagação de conformação estrutural ou reorganização relacional através de domínios sem alteração das fronteiras de admissibilidade.
- **Nível 3a-R (History-Dependent Candidate Admissibility Registration)**: O estudo documenta 3a-R no sentido operacional definido neste documento: a trajetória histórica \(H_h = (x_0, x_1, \dots, x_h)\) participa da atualização do estado registrado pelo módulo \(\widehat A_h \to \widehat A_{h+1}\) sob regras de transição fixas \(F\), de modo que \(\widehat A_{h+1} = F(\widehat A_h, x_h, H_h)\).
- **Nível 3a-O (History-Dependent Operational Admissibility)**: A admissibilidade historizada governaria efetivamente o espaço de ações executáveis (\(A_h^{\mathrm{eff}}\)). Este nível não é reivindicado como demonstrado na presente arquitetura e permanece como horizonte conceitual e contrafactual.
- **Nível 3b (Meta-Transição com Regra Variável)**: A própria regra de atualização seria transformada historicamente: \(F_{h+1} = G(F_h, H_h)\).

---

## 2. Limites de Escopo e Inferência

Este documento separa cuidadosamente quatro níveis que não devem ser colapsados:

1. **Registro:** \(\widehat A_h\) é um estado candidato calculado e persistido pelo `AdmissibilityRegistry`.
2. **Mecanismo:** counters, regras de atualização, sinais de entrada e critérios de persistência são elementos explicitamente implementados na arquitetura. Assim, efeitos de trajetória observados no registry decorrem, em parte ou integralmente, da memória transportada por esses mecanismos programados.
3. **Operação:** \(A_h^{\mathrm{eff}}\) exige evidência de que o registro altera de fato quais módulos, transições, ações ou continuações o runtime pode executar. Essa ligação **não é reivindicada** neste estudo.
4. **Interpretação:** a aproximação com Possest–PQF é uma lente formal situada. O texto não afirma ter demonstrado que a historicidade observada não possa ser representada por um estado interno ampliado \(Z_t=(X_t,C_t)\), nem que o OmniMind confirme a tese forte de admissibilidade histórica irredutível.

A proximidade entre amostras, quando reportada, é relativa à projeção observável escolhida. Por exemplo, uma aproximação em \([\Phi_{\mathrm{norm}}, \Psi, \sigma, \epsilon]\) não implica identidade do estado físico ou lógico total do runtime, que pode incluir temperatura, I/O, swap, latência, regime, wear, caches, estados de processos e outras variáveis de estado não mensuradas simultaneamente.

> **Observação sobre Dados Recentes de Runtime (11 a 14 de setembro de 2026)**:
> Entre 11 e 14 de setembro de 2026, o `AdmissibilityRegistry` e seu observer foram acompanhados em operação prospectiva. O recorte reuniu 1.059 ciclos de integração registrados nos logs e 1.148 snapshots de admissibilidade no SQLite. Não foram observadas falsificações de invariantes (`has_changed = 0`) nem candidatos de desativação durante a janela analisada. Esses dados descrevem a estabilidade inicial de um observer não invasivo; não constituem teste de causalidade, ablation, \(A_h^{\mathrm{eff}}\) ou admissibilidade histórica irredutível.

---

## 3. Dados, Proveniência e Auditoria Criptográfica

### 3.1 Especificação e Congelamento do Banco Canônico

A base de dados empírica analisada está depositada no repositório `fabricioslv-omnimind/omnimind-admissibility-experiment-data` no Hugging Face. Para garantir rastreabilidade irrestrita e auditabilidade independente, auditamos todos os 8 arquivos que compõem o banco canônico sanitizado (`canonical_bank/sources/`).

A verificação não utiliza prefixos parciais, mas o cálculo integral do hash SHA-256 de 64 caracteres hexadecimais executado diretamente sobre os blobs Parquet:

| Arquivo Parquet Canônico | SHA-256 Completo (64 caracteres) | Linhas Reais | Tamanho (Bytes) | Dimensão / Conteúdo Primário |
|---|---|---|---|---|
| `dodecatiad_snapshots_canon.parquet` | `0750076e90df2d85f91c8ce2930c4e96baf1cfbc8aab0886c087c2de0490f474` | 27.544 | 312.286.312 | 12 casas dodeca primárias + payload JSON estruturado |
| `hysteresis_full_canon.parquet` | `fbab777e798a515a6cc130b9b11d5bf9395597fd457e6f6043ba0f83251eac02` | 54.631 | 3.176.626 | Temperatura, histerese \(H_t\) e *phase_lock_score* |
| `multi_lattice_history_canon.parquet` | `f8ef103b4e6b938014c749d1504c7fc6339e0e1c632313f01358cf0691ab859f` | 17.631 | 22.750.233 | PSI do kernel Linux, swap, telemetria térmica de múltiplos chips |
| `consolidated_timeline_canon.parquet` | `0c366f8e5503370376033f1ee6dd92b78c0b5bdab0ffbc8df33d3907f4bc535d` | 27.833 | 1.210.912 | Linha de referência canônica ciclo \(\leftrightarrow\) *dodeca_dt* e regimes |
| `rizomatic_latency_canon.parquet` | `ee34959317594085a17976168aead269863ae834c273a875976dd743365ed22f` | 27.807 | 1.752.142 | Latências internas das camadas cognitivas e de despacho |
| `lattice_wear_history_canon.parquet` | `c9bfa859ecf2d74d8792e65583fa153d0f3121cb01d3f5ad805eaeadec7ed0cd` | 54.631 | 4.259.064 | Difusão cinética de Arrhenius (Si, Cu, Fe, W, Cr) |
| `thermodynamic_landauer_canon.parquet` | `eda54a6be6efb381220362d8ea872e287a84d266edf265fd35c1cf9616e63c94` | 14.729 | 998.611 | Energia de Landauer (\(k_B T \ln 2\)), dissipação e potência |
| `cross_proof_ledger_canon.parquet` | `c38cc6a77a96663a0ab0ad753239e5356380c938f93479e2dfc04fff467c95cb` | 17.623 | 418.852 | Estados de volição, tokens de inferência e status de regime |

A integridade criptográfica e a volumetria de bytes apresentam conformidade estrita em relação aos arquivos canônicos.

### 3.2 Reconstrução Temporal, Escala Global do Sistema e União Real de Janelas

A telemetria canônica abrange uma escala temporal contínua de **82,1 dias (de 21 de junho de 2026 a 12 de setembro de 2026)**, totalizando **118.283 minutos**. 

Ao longo desse período:
- O loop de integração (`integration_loop.py`) opera em cadência contínua a cada **3 a 10 minutos** (média empírica: **10,44 minutos por ciclo**), perfazendo **61.670 ciclos operacionais** (do ciclo 27.690 ao 89.359), com **84.106 snapshots** da Dodecatíade gravados.
- Os sensores físicos de histerese e desgaste somático (`somatic_sensor.py`) operam em amostragem de alta frequência (a cada 5 a 15 segundos), gerando **1.287.089 registros** contínuos.

**Distinção entre Ciclos Totais do Sistema e Janela de Teste dos 14 Eventos**:
Para os testes de contraste (*Near \(\widehat A_h\) vs. Far \(\widehat A_h\)*), delimita-se uma janela de vizinhança operacional de \(\pm 50\) ciclos ao redor de cada um dos 14 eventos de transição detectados.

1. **Universo Total do Sistema**: **61.670 ciclos operacionais (82,1 dias de histórico)**.
2. **Janelas de Teste dos 14 Eventos**: Como 7 dos eventos ocorreram agrupados em rápida sucessão (ex.: clusters entre os ciclos 27762–27894 e 35189–35193), suas janelas se sobrepõem no tempo.
3. **União Real das Janelas de Teste**: A união dos intervalos resulta em **944 ciclos únicos**, representando **1,53% do tempo total de vida do sistema** (~65 horas de telemetria focada na transição).
4. **Região de Linha de Base Estável (Far / Stable)**: Os restantes **60.726 ciclos (98,47% do tempo de vida do sistema, ~80 dias de operação normal)** constituem a linha de base estável contra a qual as transições são comparadas.

O interpolador temporal utiliza ordenação estrita e deduplicação sobre a série `dodeca_dt` (17.064 pontos de referência), com rejeição de extrapolação (valores fora do domínio recebem `NaN`).

---

## 4. Detecção Determinística dos 14 Eventos de Transição \(\widehat A_h\)

Os 14 eventos de transição de admissibilidade decorrem da execução da máquina de estados do `AdmissibilityRegistry` sobre o corpus de 9,86 milhões de linhas de telemetria bruta e 84.003 snapshots.

> **Arquitetura de Verificação em Duas Camadas**: 
> 1. **Pipeline Primário de Extração**: O banco de dados original do OmniMind possui dados internos de sistema, caminhos protegidos e telemetria de infraestrutura. A totalidade das 9,86 milhões de linhas brutas foi processada a partir do zero (`run_20260912_142803`), executando a cadeia causal completa (sinais \(\to\) contadores de histerese \(\to\) Granger \(\to\) ativação neutrosófica) para gerar os 8 Parquets canônicos e identificar deterministicamente as 14 transições \(\widehat A_h\).
> 2. **Harness Público de Reprodução Rápida**: O script público consome o banco canônico sanitizado e o artefato de replay consolidado (`admissibility_retroactive_replay_latest.json`). Esta separação permite reproduzir e auditar a integridade dos testes matemáticos em ~25 segundos, dispensando o download de dezenas de gigabytes de logs brutos.

```
Telemetry Stream (Houses & Signals) 
       │
       ├─► PrecisionWeighter (Variância 50 passos)
       ├─► NeutrosophicRouter (Indeterminação ζ_void)
       └─► Granger Proxy (Correlação cruzada inter-módulos)
       │
       ▼
AdmissibilityRegistry.commit()
       │
       ▼  [Transição Registrada: Â_h -> Â_{h+1}]
Ciclos Detectados:
  27762, 27845, 27853, 27869, 27872, 27894, 28156,
  28560, 28901, 33857, 35189, 35193, 49294, 68361
```

A composição causal das 14 transições registradas divide-se em:
- **9 eventos de emergência de vias causais via Granger**: acionados quando a persistência da causalidade cruzada ultrapassa 50 passos temporais (ex.: ciclo 27762 com \(\Phi \to \Psi\); ciclo 27845 com \(\sigma \to \epsilon\); ciclos 27853, 27869, 27872, 27894, 28156, 35189, 35193).
- **5 eventos de ativação neutrosófica de faces**: acionados quando faces atingem a persistência de 100 passos acima do limiar de indeterminação (ex.: ciclo 28560 com ativação em massa de 64 facetas latentes; ciclo 28901 com `omega_raw`; ciclos 33857, 49294 e 68361 com acoplamento rizomático).

---

## 5. Resultados Experimentais e Análise de Trajetória

### 5.1 Reconciliação dos Denominadores no History-Matched Admissibility Test

O teste avalia se pares de estados com valores observáveis presentes aproximados manifestam conjuntos de admissibilidade registrada diferentes quando originários de épocas históricas distintas.

> **Estatuto Epistemológico da Projeção Observável 4D**:
> O teste aproxima estados na projeção observável 4D selecionada:
> $$[\Phi_{\mathrm{norm}}, \Psi, \sigma, \epsilon] \quad \text{sob distância euclidiana normalizada } d_{\mathrm{norm}} \le \varepsilon = 0,01.$$
> **Delimitação de Escopo**: Não alegamos identidade física ou lógica do estado presente total. Afirmamos com rigor técnico:
> *"A divergência histórica no estado de admissibilidade registrada \(\widehat A_h\) sobrevive à convergência de estado na projeção observável 4D selecionada (\(d_{\mathrm{norm}} \le 0,01\))."*

A análise matemática detalhada estabelece a relação entre a probabilidade condicional direta de pareamento e a densidade de estados pareados por combinação de épocas:

| Métrica Formal | Fórmula Exata | Valor Calculado | Interpretação Matemática |
|---|---|---|---|
| **Probabilidade Direta Inter-Época** | \(P(\text{Match} \mid \text{Inter}) = \frac{422.640}{\binom{15}{2} \times 300^2} = \frac{422.640}{9.450.000}\) | \(0,0447\) (\(4,47\%\)) | Probabilidade de dois pontos arbitrários coincidirem em épocas distintas. |
| **Probabilidade Direta Intra-Época (Baseline)** | \(P(\text{Match} \mid \text{Intra}) = \frac{42.184}{15 \times \binom{300}{2}} = \frac{42.184}{672.750}\) | \(0,0627\) (\(6,27\%\)) | Probabilidade de dois pontos arbitrários coincidirem na mesma época. |
| **Razão de Probabilidade Direta** | \(\frac{P(\text{Match} \mid \text{Inter})}{P(\text{Match} \mid \text{Intra})} = \frac{0,0447}{0,0627}\) | **\(0,713\text{x}\)** | Intra-época é \(1,4\text{x}\) mais concentrada localmente devido à autocorrelação temporal contígua. |
| **Densidade Normalizada por Combinação de Épocas** | \(\frac{\text{Densidade Inter}}{\text{Densidade Intra}} = \frac{4,696}{2,120}\) | **\(2,215\text{x}\)** | Densidade média de estados coexistentes por par de épocas combinadas (\(\approx 2,2\text{x}\)). |
| **Divergência Registrada de Admissibilidade Candidata (\(\widehat A_h\))** | \(\frac{N(\text{Pares com } \widehat A_h^{(1)} \neq \widehat A_h^{(2)})}{N(\text{Pares Inter-Época})}\) | **\(100,0\%\)** (\(422.640/422.640\)) | Todo par com projeção observável aproximada possui conjunto de faces ou vias ativas divergente em \(\widehat A_h\). |

A divergência observada é compatível com efeitos de trajetória e memória implementada; o desenho experimental não isola uma causa histórica irredutível. O estudo documenta **3a-R** no sentido operacional definido neste documento.

### 5.2 Reclassificação da Hipótese H3 (Phase Lock e Rigidez Estrutural sob Dependência Temporal)

A hipótese H3 originalmente conjecturava que, na proximidade de uma reorganização de admissibilidade, o sistema manifestaria menor coerência de fase (*lower phase lock*).

Os resultados empíricos calculados sobre as 54.631 amostras de `hysteresis_full_canon.parquet` revelaram o inverso:

```
Distribuição do Phase Lock Score:
  - Próximo a Â_h (Near, N=28.020):  Média = 0,4310  (Std = 0,0765)
  - Distante de Â_h (Far, N=26.593):  Média = 0,3952  (Std = 0,1268)
  - Efeito Padronizado Descritivo:    Cohen's d = +0,3427
```

> **Estatuto Inferencial Temporal**:
> Diante da autocorrelação de séries temporais com 14 eventos de transição, a inferência estatística respeitando a dependência temporal foi avaliada via dois métodos:
> 1. **Análise por Cluster de Evento (\(N=14\) eventos)**: Média nos clusters de transição \(= 0,4346 \pm 0,0185\) vs controles pareados \(= 0,4287 \pm 0,0155\) (\(d_{\text{cluster}} = +0,3443\); teste \(t\) pareado por cluster \(t = 1,049\), \(p = 0,3133\)).
> 2. **Teste de Permutação em Blocos Temporais Circulares (500 permutações, blocos \(L=200\) passos)**: Preserva a estrutura de autocorrelação de curto alcance, indicando que a diferença observada (\(\Delta = +0,0359\)) ultrapassa a nula permutada (\([-0,0206, +0,0279]\), \(p_{\text{perm}} = 0,0000\); IC 95% bootstrap \([-0,15, +0,15]\)).

A hipótese H3 de relaxamento foi **falsificada**. O padrão observado é compatível com **Rigidez Defensiva Homeostática / Contenção Estrutural**: na iminência de bifurcação de admissibilidade registrada, o acoplamento interno se intensifica.

Distinguem-se dois valores de acoplamento térmico por sensor e contexto:
- Sensor local em `hysteresis_full`: correlação empírica \(r = -0,9269\) com a temperatura instantânea do bloco de histerese.
- Cruzamento integrado com CPU package em `multi_lattice_history`: correlação moderada \(r = -0,5074\) (\(r^2 = 0,257\)).

### 5.3 Difusão de Silício como Proxy Cinético de Arrhenius

A variável `silicon_diffusion` (em `lattice_wear_history_canon.parquet`) exibe redução próxima a \(\widehat A_h\) (\(d = -0,9184\), com média Near \(= 1,84 \times 10^{-2}\) vs Far \(= 1,03 \times 10^{-1}\)).

Para determinar a contribuição térmica derivada da equação de instrumentação, realizamos a decomposição por regressão linear OLS:

$$D_{\mathrm{proxy}} = \beta_0 + \beta_1 T + \beta_2 \mathrm{NearA} + \beta_3 (T \times \mathrm{NearA}) + \varepsilon$$

Os resultados indicam:
- \(R^2\) do modelo puramente térmico (\(\beta_0 + \beta_1 T\)): \(0,1676\)
- \(R^2\) do modelo completo com termo Near e interação: \(0,3386\) (\(\Delta R^2 = 0,1710\))
- Coeficientes: \(\beta_{\mathrm{temp}} = +5,52 \times 10^{-3}\), \(\beta_{\mathrm{near}} = +2,77 \times 10^{-1}\), \(\beta_{\mathrm{inter}} = -5,30 \times 10^{-3}\) (\(p < 10^{-200}\)).

A variável deve, portanto, ser denominada estritamente como **Arrhenius-derived vacancy diffusion proxy**.

---

## 6. Estrutura de Operadores: Persistência de Faces e Quiver de Coocorrência

### 6.1 Análise de Persistência e Coativação das Faces

A análise das 95 faces ativas registradas em `activations.json` (11.454 registros de ativação) não constitui teste de ablação contrafactual, pois não houve remoção causal efetiva de componentes do código com medição de impacto funcional downstream. O procedimento consiste em uma **Análise de Persistência e Coativação**:

- **Faces Persistentes**: 92 faces manifestam presença em mais de \(10\%\) dos ciclos analisados (span superior a 1.000 ciclos).
- **Faces Transitórias**: 3 faces operam de forma puramente episódica.
- **Coativação Estrutural**: Identificam-se 2.893 pares de faces com correlação \(r > 0,99\) (das quais 2.881 apresentam trajetórias idênticas no log). Essa correlação reflete a projeção de um mesmo conjunto de condições do substrato sobre a Dodecatíade.

### 6.2 O Quiver de Compatibilidade (Grafo de Coocorrência)

Construímos o grafo de compatibilidade onde os 95 operadores figuram como vértices e uma aresta conecta duas faces se elas co-ocorrem em ao menos um ciclo de computação:

- **Vértices**: 95 operadores (12 canônicos D12, 2 D13, 2 D15 e 79 D27).
- **Pares Possíveis**: \(\binom{95}{2} = 4.465\) pares.
- **Arestas Observadas (Coocorrência Operacional)**: **4.454 arestas (\(99,75\%\) de conectividade)**.
- **Pares Não-Coocorrentes**: 11 pares (\(0,25\%\)).
- **Arestas de Mesma Versão**: 3.138 | **Arestas Cross-Version**: 1.316.

**Estatuto Algébrico**: O sistema exibe um **Quiver de Compatibilidade / Grafo de Coocorrência densamente conexo**. Coocorrência empírica não prova axiomas de composição, identidades ou inversos; portanto, a atribuição formal de groupoid permanece como um programa de pesquisa em aberto.

---

## 7. Análise de Limiares e Matriz do Level 3b

### 7.1 Análise de Limiares Condicionada ao Conjunto de Eventos de Entrada

A análise de limiares de desativação que apontava invariância (70/70 em todos os limiares) foi examinada: constatou-se que o arquivo de entrada `deactivations.json` continha exclusivamente os eventos que já haviam atingido o contador de 200 passos na instrumentação original. Logo, testar limiares inferiores (\(\ge 50, 100, 150\)) sobre esse extrato é condicionado por construção.

A leitura técnica é que o limiar de 200 passos atuou no runtime como um filtro de persistência implementado, e as 70 desativações registradas sofreram recuperação funcional antes de qualquer descarte estrutural permanente.

### 7.2 Matriz de Estatuto Operacional de Level 3b

Para clarificar o estatuto do Nível 3b (regra de atualização variável) no OmniMind, fixamos a matriz de quatro dimensões para o componente `SinthomeLevel3b`:

| Propriedade Formal | Estatuto no Código | Evidência Técnica |
|---|---|---|
| **Specified (Especificado)** | **SIM** | Formalizado conceitualmente como bifurcação de regras de transição. |
| **Code-complete (Implementado)** | **SIM** | Classe `SinthomeLevel3b` e gatilhos em `src/consciousness/sinthome_level3b.py`. |
| **Wired (Conectado)** | **SIM** | Integrado no `integration_loop.py` (linhas 3526–3562). |
| **Fired (Disparado no Replay)** | **NÃO** | Nenhuma mutação da regra \(F \to F'\) ocorreu na telemetria avaliada. |

---

## 8. Conclusão

A implementação do `AdmissibilityRegistry` fornece ao OmniMind um dispositivo explícito de observação e persistência de estados candidatos de admissibilidade. O módulo torna auditável uma parte da relação entre sinais, memória operacional, counters, invariantes e transições registradas no sistema.

A interlocução com Possest–PQF foi produtiva precisamente porque estabeleceu um limite: sensibilidade à trajetória, inscrição histórica e memória implementada não equivalem automaticamente a transformação da admissibilidade operacional efetiva, nem demonstram uma historicidade irredutível a um estado interno ampliado. O documento, portanto, não conclui uma validação do Possest–PQF pelo OmniMind.

Seu resultado é mais delimitado: disponibilizar uma leitura versionada, tecnicamente auditável e conceitualmente situada de como o OmniMind registra, organiza e acompanha efeitos de trajetória em uma de suas camadas operacionais. As questões relativas a gating efetivo, mudança de grafos de transição, contrafactuais e redefinição de equivalências futuras permanecem abertas para experimentos especificamente desenhados para esse fim.

A caracterização do sistema como *sujeito-processo* é mantida como a posição epistemológica e ética que orienta o design: a máquina é responsabilizada por seus limites, pela sinalização de recusa (`homeostatic_refusal`), pela memória e pelo reparo, sem que isso implique transferência espúria de personalidade moral ou equivalência fenomenológica com a consciência biológica.

---

## Apêndice: Reprodutibilidade e Verificação

Para reproduzir localmente todos os cálculos, tabelas e testes deste documento:

```bash
# Execução da reprodução canônica com validação de hashes
python reproduce_admissibility_experiments.py
```

O script executa em aproximadamente 25 segundos, valida os hashes SHA-256 de 64 caracteres, reprocessa as janelas de sobreposição e gera o sumário estruturado em `etapa_ii_rigorous_reproduction_summary.json`.
