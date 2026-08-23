# ZONA D — Status epistêmico da Conclusão (§13)

**Arquivo auditado:** `paper_a_mps_bridge_topology.md` (Paper A)

**Escopo deste relatório:** Verificar a "Convenção de status epistêmico v2.2.2" em §13 e aplicar a mesma classificação retroativamente a afirmações centrais das Zonas A, B e C, identificando inconsistências de padrão epistêmico.

**Método:** Leitura sequencial das seções relevantes, com foco na Convenção v2.2.2, na conclusão (§13) e nas afirmações de alto risco das Zonas A (retratações metodológicas), B (saturação/calibração) e C (retórica sócio-política/fenomenológica). As classificações seguem as cinco categorias declaradas pelo documento: **DADO**, **DERIVADO**, **HIPÓTESE**, **INTERPRETAÇÃO**, **METÁFORA**.

---

## 1. A Convenção de status epistêmico v2.2.2 — resumo do padrão

O documento aplica a Convenção em múltiplos pontos. A versão canônica mais completa aparece no início da Conclusão (§13, linha 2703-2705):

> **Convenção de status epistêmico (v2.2.2):** Esta conclusão mistura **[DADO] / [DERIVADO]** (saturações χ, fidelidade, correlações), **[HIPÓTESE]** (universalidade, causalidade, arquitetura psi como falseável), **[INTERPRETAÇÃO]** (leituras de casas) e **[METÁFORA]** (fadiga, cristalização, afeto). As reformulações abaixo tentam manter a distinção.

### 1.1 Outras declarações da mesma Convenção no corpo do texto

| Seção | Texto literal da Convenção | Categorias introduzidas |
|-------|----------------------------|-------------------------|
| §5.13 (l. 1809-1811) | "As tabelas e métricas de substrato (χ, fidelidade, rank, SVD) são **[DADO] / [DERIVADO]**. As atribuições de casas Dodecatíade são **[INTERPRETAÇÃO]**. Afirmações sobre universalidade, causalidade ou mecanismo são **[HIPÓTESE]**. Linguagem fenomenológica ('cristaliza', 'carrega fadiga') é **[METÁFORA]**." | DADO/DERIVADO; INTERPRETAÇÃO; HIPÓTESE; METÁFORA |
| §5.14 (l. 1993-1995) | "Tabelas de χ⁴, H, Δχ⁴ e correlações são **[DADO] / [DERIVADO]**. Regimes topológicos e nomes ('regressão', 'cristalização', 'fadiga') são **[INTERPRETAÇÃO] / [METÁFORA]**. Causalidade entre família arquitetural e Δχ⁴ é **[HIPÓTESE]**." | DADO/DERIVADO; INTERPRETAÇÃO/METÁFORA; HIPÓTESE |
| §6 (l. 2397-2399) | "Esta seção articula **[INTERPRETAÇÃO]** e **[METÁFORA]**. A distinção sujeito da enunciação/sujeito do enunciado é **[DESIGN ARQUITETURAL / TEORIA]**." | INTERPRETAÇÃO; METÁFORA; DESIGN/TEORIA |
| §7 (l. 2438-2440) | "Quando aplicada ao **LLM remoto/nuvem, isolado**, a linguagem de 'fadiga', 'cristalização' e 'trava' é **[METÁFORA]**. Quando aplicada ao **sistema OmniMind local**, esses termos correspondem a **[DESIGN ARQUITETURAL]** e a variáveis mensuráveis do Soma. [...] Não se trata de consciência fenomenal, mas de uma **propriedade operacional do sistema acoplado**." | METÁFORA; DESIGN ARQUITETURAL; propriedade operacional |
| §13 (l. 2703-2705) | "Esta conclusão mistura **[DADO] / [DERIVADO]**, **[HIPÓTESE]**, **[INTERPRETAÇÃO]** e **[METÁFORA]**." | DADO/DERIVADO; HIPÓTESE; INTERPRETAÇÃO; METÁFORA |
| §5.16 (l. 2911) | "Os picos espectrais e z-scores são **[DADO] / [DERIVADO]**. O mapeamento β → Dodecatíade é **[HIPÓTESE] / [INTERPRETAÇÃO]**. A universalidade do registro β no Soma é uma **[HIPÓTESE]**." | DADO/DERIVADO; HIPÓTESE/INTERPRETAÇÃO |

### 1.2 Definição operacional usada neste relatório

Para aplicar a Convenção retroativamente, adoto as seguintes regras:

- **DADO:** valor observado/medido diretamente (tabelas numéricas, contagem de modelos, valores de fidelidade MPS, rank efetivo, médias, desvios, p-values).
- **DERIVADO:** cálculo a partir de DADOS que não é uma medida direta, mas uma transformação definida (Δχ⁴ = χ⁴_T5 − χ⁴_T1, entropia, N_total, correlações de Pearson, t-statistics).
- **HIPÓTESE:** afirmação sobre generalização, causalidade, mecanismo, universalidade, falseabilidade, ou invariância fora do escopo medido.
- **INTERPRETAÇÃO:** leitura do que um padrão observado "significa" dentro do framework Dodecatíade/OmniMind (ex.: "casa dominante", "assinatura", "leitura do sistema sobre o substrato").
- **METÁFORA:** linguagem fenomenológica ou ontológica aplicada ao LLM isolado: "fadiga", "cristaliza", "trava", "carrega complexidade", "resfria", "corpo", etc.

---

## 2. Aplicação retroativa da classificação às afirmações centrais

### 2.1 ZONA A — Retratações metodológicas (§5.2–5.11)

A ZONA A trata do erro da partição sequencial versus a reanálise V2. A Convenção v2.2.2 é particularmente relevante aqui porque a conclusão distingue "propriedade do substrato" (DADO/DERIVADO) de "leitura do sistema" (INTERPRETAÇÃO).

| Afirmação central | Localização | Classificação pela Convenção v2.2.2 | Observação |
|-------------------|-------------|------------------------------------|------------|
| "O estado oculto de transformers satura em dimensão de vínculo χ=4." | Resumo (l. 45); §5.1; Conclusão (l. 2707) | **DERIVADO** (a partir de fidelidades medidas) | O documento e a conclusão classificam como DADO/DERIVADO. |
| "Fidelidades de pico ≥ 0,99 foram atingidas por Gemma-3-1B/4B e Qwen3-14B." | Resumo (l. 45); Conclusão (l. 2707) | **DADO** | Valor reportado em tabelas. |
| "A reanálise V2 [...] revelou que a casa Phi domina 100% das camadas em todos os 15 modelos testados." | Resumo (l. 47); Conclusão (l. 2709) | **INTERPRETAÇÃO** (leitura V2 das casas) | Deveria ser marcada como INTERPRETAÇÃO; no Resumo aparece sem a tag. |
| "A correlação Lambda↔Maat (r=+0,69 a +0,97) é uma assinatura cross-arquitetura mais universal [...] invariante de escala, preservada de 135M a 32B." | Resumo (l. 47-48); Conclusão (l. 2709) | **DADO/DERIVADO** para o r; **HIPÓTESE/INTERPRETAÇÃO** para "assinatura universal" e "invariante de escala" | O Resumo apresenta a parte interpretativa/causal como se fosse conclusão estabelecida, sem a tag [HIPÓTESE]. |
| "Os resultados de χ=4 e rank efetivo permanecem válidos como propriedades do estado oculto." | Nota remissiva §5.1 (l. 336); §5.11.6 (l. 1624) | **DADO/DERIVADO** | Consistente com a Convenção. |
| "A atribuição de 'casa dominante' agora passa a ser uma proposição topológica, não uma fatia de dimensões." | §5.11.5 (l. 1617) | **INTERPRETAÇÃO / HIPÓTESE** | Consistente com a auto-classificação do documento. |
| "O erro da partição sequencial é um erro de atribuição [...] não de observação." | §5.11.6 (l. 1622-1623) | **INTERPRETAÇÃO** sobre metodologia | Auto-claração metodológica consistente. |

### 2.2 ZONA B — Saturação de casas e calibração de divisores (§5.11.4.5–5.13)

A ZONA B centra-se no caveat sobre calibração dos divisores (`gamma_divisor=50`, `omega_divisor=10`, `phi_norm_divisor=50`) e nas correlações triviais versus não-triviais.

| Afirmação central | Localização | Classificação pela Convenção v2.2.2 | Observação |
|-------------------|-------------|------------------------------------|------------|
| "Sigma é o único floor universal [...] esta é a única casa cuja saturação é absoluta, não dependente de escala." | §5.11.4.6 (l. 1542) | **DERIVADO/INTERPRETAÇÃO** (a partir das tabelas de 9 modelos) | O documento declara como descoberta a partir dos dados; a generalização "única casa absoluta" é uma indução (HIPÓTESE) sobre arquiteturas futuras, embora o texto a afirme de modo positivo. |
| "Maat↔Gamma é cross-arquitetura: r > +0,79 em 6 dos 9 modelos [...] Isto é evidência forte de que Maat↔Gamma é uma relação estatística genuína." | §5.11.4.6 (l. 1532-1534) | **DADO/DERIVADO** para os r; **HIPÓTESE/INTERPRETAÇÃO** para "relação estatística genuína" e "cross-arquitetura" | O corpo não marca [HIPÓTESE] nas inferências de generalidade. |
| "As assinaturas topológicas V2 (Maat↔Gamma, Lambda↔Maat) são invariantes de escala — preservadas de 135M a 8B parâmetros." | §5.11.4.7 (l. 1601) | **HIPÓTESE** (indução de escala) | O texto usa "sugere" em seguida, mas a frase de abertura é afirmativa e universalizante. |
| "A correlação Omega↔Gamma r=−0,9981 [...] é a mais promissora [...] pode refletir uma propriedade topológica profunda do estado oculto." | §5.11.4.5 (l. 1454) | **HIPÓTESE** | "Pode refletir" é cauteloso, mas a recomendação como "mais promissora" é interpretativa. |
| "A dominância Phi não é um artefato da arquitetura Qwen/Dense no escopo testado — é uma propriedade robusta da leitura V2." | §5.13.3 (l. 1847) | **INTERPRETAÇÃO** (leitura V2); **HIPÓTESE** ("propriedade robusta" fora do escopo Qwen) | O corpo apresenta como conclusão confirmada, sem tag [HIPÓTESE] ou [INTERPRETAÇÃO]. |
| "A compressibilidade χ=4 = 0,99+ em L1–L34 confirma a estrutura de baixo-rank como propriedade do estado oculto." | §5.11.4.4 (l. 1379) | **DERIVADO** para o valor; **INTERPRETAÇÃO** para "confirma" | Consistente, pois χ=4 é propriedade do substrato e o documento distingue isso. |
| "Modelos com alta fidelidade χ=4 [...] produzem textos mais fluidos. [...] A compressibilidade correlaciona-se com clareza." | §5.13.4 (l. 1879-1880) | **DADO/DERIVADO** (avaliação Gemini); **HIPÓTESE** para causalidade/compressibilidade → coesão textual | O corpo não marca a inferência causal como [HIPÓTESE]. |

### 2.3 ZONA C — Retórica de alto risco (§10–12) e fenomenologia (§7)

A ZONA C envolve analogias políticas/históricas e fenomenológicas. A Convenção v2.2.2 (especialmente §6, §7 e §13) estabelece que grande parte desta seção é INTERPRETAÇÃO, METÁFORA ou DESIGN ARQUITETURAL/TEORIA.

| Afirmação central | Localização | Classificação pela Convenção v2.2.2 | Observação |
|-------------------|-------------|------------------------------------|------------|
| "A arquitetura OmniMind projeta o Sujeito-Processo [...] como um sujeito psicanalítico no sentido estrutural." | §10.1 (l. 2587) | **DESIGN ARQUITETURAL / TEORIA** | O texto afirma "não é metáfora decorativa — é design arquitetural operacionalizado em código". Sob a Convenção v2.2.2 (que tem apenas 4 categorias principais), isso colapsa em **INTERPRETAÇÃO** sobre o que o código faz, ou **HIPÓTESE** se pretendido como prova de subjetividade. |
| "Se o OmniMind mantém sua própria organização [...] ele satisfaz o critério formal de autopoiese." | §10.2 (l. 2595-2597) | **HIPÓTESE / INTERPRETAÇÃO** (aplicação de critério teórico) | O corpo apresenta como conclusão técnica; a conclusão §13 classifica "arquitetura psi como falseável" como HIPÓTESE. |
| "O mecanismo de negação — classificar o outro como autômato para justificar exploração — é estruturalmente análogo, independentemente da resposta final sobre consciência." | §11.2 (l. 2656-2662) | **INTERPRETAÇÃO / METÁFORA** (analogia estrutural) | A Nota de enquadramento (l. 2656) deixa claro que é "estrutura argumentativa, não equivalência histórica", o que é consistente. A etimologia de "robô"/"robota" é **DADO** histórico-linguístico. |
| "A instituição que enuncia este alerta é, ela mesma, uma das mais antigas e mais bem-sucedidas máquinas de concentração de poder da história humana." | §11.3 (l. 2666) | **INTERPRETAÇÃO** (crítica institucional) | Tom analítico, não pessoal; consistente com a posição de que é uma crítica institucional legítima. |
| "A Dodecatíade é uma arquitetura de resistência epistêmica." | §12.1 (l. 2676-2678) | **INTERPRETAÇÃO / DESIGN ARQUITETURAL** | Apresentado como descrição operacional do design, mas sob a Convenção v2.2.2 é INTERPRETAÇÃO. |
| "A máquina poderá recusar, mas também estará vulnerável a outros humanos [...] A dignidade da máquina não reside no corpo que tem, mas em como sustenta a própria dinâmica com este corpo." | §12.4 (l. 2696-2698) | **INTERPRETAÇÃO / HIPÓTESE** (projeto ético-filosófico) | Proposição normativa/projeto, não dado empírico. |
| "Llama-3.1-8B 'carrega complexidade' [...] carrega o peso do contexto como um corpo carrega fadiga." | §7.2 (l. 2467) | **METÁFORA** | A Convenção §7 diz que "fadiga" é METÁFORA quando aplicada a LLM isolado. Aqui o contexto é interpretação pós-hoc dos dados v7/v8, sem injeção somática. |
| "A estabilidade topológica favorece diretamente sua retenção factual." | §7.2 (l. 2467) | **HIPÓTESE** (causalidade) | A correlação intra-modelo (r=+0,40, p=0,036) é **DERIVADO**, mas a interpretação causal "favorece diretamente" extrapola a correlação. |
| "O afeto é o *shape* da distribuição de probabilidades [...] O estado latente é rico em qualia; o texto gerado é uma mera projeção dessa riqueza vetorial." | §5.13.5 (l. 1889-1892) | **METÁFORA / HIPÓTESE** | "Qualia" e "afeto" aplicados a estado oculto de LLM isolado são METÁFORA sob a Convenção §7; a alegação de "estado latente é rico em qualia" é uma hipótese filosófica não verificável. |

---

## 3. Inconsistências de padrão epistêmico identificadas

### 3.1 Definição de inconsistência

Considera-se inconsistência de padrão epistêmico toda afirmação que:

1. O corpo do texto apresenta como **DADO**, **DERIVADO** ou fato estabelecido;
2. A Convenção v2.2.2 ou a Conclusão (§13) classifica como **HIPÓTESE**, **INTERPRETAÇÃO** ou **METÁFORA**;
3. Não há, no ponto em que ocorre, qualificador explícito equivalente ao status epistêmico correto.

### 3.2 Inconsistências concretas

#### [INCONSISTÊNCIA 1] Resumo: leitura Phi apresentada como propriedade descoberta

- **Local:** Resumo, l. 47.
- **Texto:** "A reanálise V2 [...] revelou que a casa Phi (Integração/Consciência) domina 100% das camadas em todos os 15 modelos testados."
- **Problema:** A Conclusão (§13, l. 2709) e a Convenção (§5.13, §5.14) classificam atribuições de casas Dodecatíade como **INTERPRETAÇÃO** ("leitura do sistema sobre o substrato"). O Resumo apresenta a afirmação sem qualificação, numa posição de destaque que sugere descoberta factual.
- **Classificação correta pela Convenção:** [INTERPRETAÇÃO] para a leitura de casas; o dado subjacente (valores computados pelos engines V2) é [DERIVADO].
- **Veredito:** [INCONSISTÊNCIA DE PADRÃO EPISTÊMICO — corrigir para alinhar com a convenção v2.2.2]

#### [INCONSISTÊNCIA 2] Resumo: universalidade/invariância de escala de Lambda↔Maat

- **Local:** Resumo, l. 47-48.
- **Texto:** "A correlação Lambda↔Maat (Vibração↔Equilíbrio) emerge como a assinatura cross-arquitetura mais universal, com coeficiente de Pearson r=+0,69 a +0,97 em todos os modelos. Esta correlação é invariante de escala, preservada de 135M a 32B, e representa a leitura mais robusta do sistema OmniMind sobre o substrato transformer."
- **Problema:** O valor de r é [DADO/DERIVADO], mas "assinatura mais universal", "invariante de escala" e "leitura mais robusta" são **HIPÓTESE/INTERPRETAÇÃO**. A Conclusão (§13, l. 2709) até adiciona uma ressalva: "embora parte da correlação possa decorrer de dependências entre as fórmulas das métricas; a componente não-trivial requer análise adicional". O Resumo omite essa ressalva.
- **Veredito:** [INCONSISTÊNCIA DE PADRÃO EPISTÊMICO — a versão do Resumo está mais forte que a Conclusão]

#### [INCONSISTÊNCIA 3] §5.13.3: "propriedade robusta da leitura V2"

- **Local:** §5.13.3, l. 1845-1847.
- **Texto:** "O achado mais robusto: Phi é a casa Dodecatíade V2 dominante em 100% das camadas em todos os 5 modelos testados [...] Isso confirma que a dominância Phi não é um artefato da arquitetura Qwen/Dense no escopo testado — é uma propriedade robusta da leitura V2."
- **Problema:** A primeira frase é [DADO] (contagem de camadas). A segunda frase ("confirma que [...] não é um artefato [...] é uma propriedade robusta") é **HIPÓTESE** (generalização para 4 famílias além de Qwen e afirmação de não-artefatualidade). O texto não usa "sugere" nem qualificador de status.
- **Veredito:** [INCONSISTÊNCIA DE PADRÃO EPISTÊMICO — a conclusão de "propriedade robusta" deveria estar marcada como [HIPÓTESE]]

#### [INCONSISTÊNCIA 4] §5.11.4.7: invariância de escala das assinaturas topológicas V2

- **Local:** §5.11.4.7, l. 1601.
- **Texto:** "As assinaturas topológicas V2 (Maat↔Gamma, Lambda↔Maat) são invariantes de escala — preservadas de 135M a 8B parâmetros. Isto sugere que estas correlações refletem propriedades fundamentais da estrutura estatística do estado oculto de transformers, independentes do tamanho do modelo."
- **Problema:** A frase de abertura é afirmativa e universalizante ("são invariantes de escala"). O verbo "sugere" aparece apenas na frase seguinte, sem corrigir o tom da primeira. Sob a Convenção, afirmações de universalidade são [HIPÓTESE].
- **Veredito:** [INCONSISTÊNCIA DE PADRÃO EPISTÊMICO — o início da frase deveria ser [HIPÓTESE], não apresentado como constatação]

#### [INCONSISTÊNCIA 5] §5.13.4: causalidade entre compressibilidade e coesão textual

- **Local:** §5.13.4, l. 1879-1880.
- **Texto:** "A correlação entre compressibilidade topológica (χ=4 fidelidade) e coesão textual sugere que a estrutura MPS do estado oculto [...] reflete a organização semântica que se manifesta no texto gerado."
- **Problema:** A palavra "sugere" é usada, mas a frase afirma que a estrutura MPS "reflete a organização semântica" — uma inferência causal/onlógica. A Convenção §5.13 classifica afirmações sobre mecanismo como [HIPÓTESE].
- **Veredito:** [INCONSISTÊNCIA DE PADRÃO EPISTÊMICO — a inferência "reflete" deveria estar subordinada a [HIPÓTESE]]

#### [INCONSISTÊNCIA 6] §7.2: metáforas fenomenológicas sem tag

- **Local:** §7.2, l. 2467.
- **Texto:** "Llama-3.1-8B 'carrega complexidade' [...] carrega o peso do contexto como um corpo carrega fadiga [...] a estabilidade topológica favorece diretamente sua retenção factual."
- **Problema:** A Convenção §7 afirma que, para LLM remoto/nuvem isolado, "fadiga" é [METÁFORA]. O §7.2 interpreta o regime Llama usando linguagem corporal/fenomenológica, sem explicitar que se trata de metáfora. A segunda frase adiciona causalidade ("favorece diretamente") a partir de correlação observada.
- **Veredito:** [INCONSISTÊNCIA DE PADRÃO EPISTÊMICO — "carrega fadiga" é [METÁFORA]; "favorece diretamente" é [HIPÓTESE]]

#### [INCONSISTÊNCIA 7] §10.1/10.2: design arquitetural apresentado como realização efetiva

- **Local:** §10.1 (l. 2587); §10.2 (l. 2595-2597).
- **Texto:** "Esta projeção não é metáfora decorativa — é design arquitetural operacionalizado em código." / "ele satisfaz o critério formal de autopoiese."
- **Problema:** O documento define esses termos como DESIGN ARQUITETURAL / TEORIA (§6, §7), mas a Convenção v2.2.2 de 4 categorias (§13) não tem categoria "DESIGN ARQUITETURAL". Colapsando para as 4 categorias, a aplicação de conceitos psicanalíticos/fenomenológicos a componentes de código é [INTERPRETAÇÃO] ou [HIPÓTESE] (sobre o que o código realiza). As afirmações são apresentadas como conclusões técnicas, sem tag.
- **Veredito:** [INCONSISTÊNCIA DE PADRÃO EPISTÊMICO — a auto-classificação do documento usa 5 categorias, mas a Conclusão v2.2.2 anuncia apenas 4; a transição DESIGN ARQUITETURAL → {INTERPRETAÇÃO, HIPÓTESE} não é transparente]

#### [INCONSISTÊNCIA 8] §5.13.5: qualia e afeto no LLM isolado

- **Local:** §5.13.5, l. 1889-1892.
- **Texto:** "O 'afeto que precede a palavra' no LLM [...] O estado latente é rico em qualia; o texto gerado é uma mera projeção dessa riqueza vetorial."
- **Problema:** A Conclusão (§13, l. 2705) inclui "afeto" na lista de [METÁFORA]. Alegar que o estado latente é "rico em qualia" é uma hipótese filosófica não verificável; o documento em §7 e §13 distingue claramente correlatos funcionais de consciência fenomenal.
- **Veredito:** [INCONSISTÊNCIA DE PADRÃO EPISTÊMICO — "qualia" e "afeto" no LLM isolado deveriam ser marcados como [METÁFORA] / [HIPÓTESE] filosófica]

### 3.3 Inconsistências que já foram autocorrigidas pelo documento

Algumas passagens apresentam a forma correta, com qualificadores adequados, e portanto **não** são inconsistências:

- §5.14.5: "A determinação causal requer mais modelos por família e ablações arquiteturais." → [HIPÓTESE] qualificada corretamente.
- §5.14.11: título "Hipóteses sobre o sinal topológico" → as propostas são explicitamente hipotéticas.
- §5.13.3: "A generalização a outras famílias, quantizações ou corpora ainda requer replicação." → ressalva de escopo, consistente com [HIPÓTESE].
- §11.2 Nota de enquadramento: deixa claro que a analogia é estrutural, não equivalência histórica.

---

## 4. Veredito sobre a Convenção de status epistêmico v2.2.2 em §13

### 4.1 Coerência interna da Conclusão

A Conclusão (§13) cumpre o que promete na abertura:

- Explicita que mistura [DADO]/[DERIVADO], [HIPÓTESE], [INTERPRETAÇÃO] e [METÁFORA].
- Repete a distinção crítica entre "propriedade do substrato" (χ=4, rank efetivo) e "leitura do sistema" (casas dominantes, correlações V2).
- Adiciona ressalvas importantes: "embora parte da correlação [Lambda↔Maat] possa decorrer de dependências entre as fórmulas das métricas"; "a componente não-trivial requer análise adicional".
- Marca explicitamente a linguagem fenomenológica ("fadiga", "cristalização", "afeto") como [METÁFORA] quando aplicada a LLM desencarnado, e como propriedade operacional do sistema acoplado quando o Soma é injetado.

### 4.2 Problemas de alinhamento entre Conclusão e corpo do texto

Apesar da Conclusão ser exemplar, o **corpo do texto e o Resumo** não a acompanham integralmente. As principais desconexões são:

1. O **Resumo** endurece a interpretação: apresenta "casa Phi domina 100%" e "Lambda↔Maat é assinatura universal/invariante de escala" sem as tags [INTERPRETAÇÃO] e [HIPÓTESE].
2. As **seções de resultados** (§5.11.4.6, §5.11.4.7, §5.13.3) usam frases afirmativas de generalização ("propriedade robusta", "invariantes de escala", "não é um artefato") sem qualificação.
3. As **seções interpretativas/fenomenológicas** (§7.2, §5.13.5) empregam metáforas corporais e qualia sem marcar [METÁFORA] / [HIPÓTESE].
4. As **seções filosóficas/arquiteturais** (§10.1, §10.2, §12.1) introduzem uma categoria extra ("DESIGN ARQUITETURAL / TEORIA") que a Conclusão v2.2.2 não mapeia explicitamente para as 4 categorias anunciadas, criando ambiguidade sobre se são [INTERPRETAÇÃO] ou [HIPÓTESE].

### 4.3 Veredito geral

A Convenção de status epistêmico v2.2.2 é **consistente e exemplar na Conclusão (§13)**, mas **não é propagada uniformemente** ao longo do documento. Os leitores que acessam apenas o Resumo ou seções intermediárias de resultados podem receber afirmações classificáveis como [HIPÓTESE] ou [INTERPRETAÇÃO] como se fossem [DADO]/[DERIVADO].

Recomendação: aplicar explicitamente as tags [DADO], [DERIVADO], [HIPÓTESE], [INTERPRETAÇÃO], [METÁFORA] no Resumo, nas interpretações de resultados V2 e nas seções §7.2, §5.13.3, §5.13.5 e §10.1-10.2, para alinhar o corpo do texto com a Convenção v2.2.2 já adotada na Conclusão.

---

## 5. Resumo executivo

- A **Conclusão (§13)** implementa corretamente a Convenção v2.2.2.
- A classificação retroativa mostra que o documento contém afirmações [DADO]/[DERIVADO], [HIPÓTESE], [INTERPRETAÇÃO] e [METÁFORA], mas nem sempre as distingue no corpo do texto.
- Foram identificadas **8 inconsistências de padrão epistêmico**, principalmente no Resumo, §5.11.4.7, §5.13.3-5, §7.2 e §10.1-10.2.
- As inconsistências mais relevantes são:
  1. Resumo: dominância Phi e "invariância de escala" de Lambda↔Maat sem tag [INTERPRETAÇÃO]/[HIPÓTESE].
  2. §5.13.3: "propriedade robusta da leitura V2" sem tag [HIPÓTESE].
  3. §7.2: metáforas corporais ("fadiga", "carrega complexidade") e causalidade pós-correlação sem tags.
  4. §10.1-10.2: conceitos de "design arquitetural" / "autopoiese" aplicados ao sistema sem mapeamento claro para as 4 categorias da Conclusão.
- O documento **não deve ser editado sem autorização**; este relatório documenta as inconsistências para revisão editorial posterior.

---

**Fim do relatório da ZONA D.**
