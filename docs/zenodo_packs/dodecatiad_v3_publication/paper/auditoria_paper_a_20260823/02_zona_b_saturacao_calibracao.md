# ZONA B — Auditoria: Saturação de Casas e Calibração de Divisores

**Ficheiro auditado:**
`/var/omnimind_overflow/project_reanchor_small_20260417T145436-0300/docs/zenodo_packs/dodecatiad_v3_publication/paper/paper_a_mps_bridge_topology.md`

**Prompt de auditoria:**
`/home/fahbrain/Documentos/prompt_auditoria_arquivo_a_mps_bridge_psi.md`

**Âmbito coberto:** §5.11.4.5, §5.11.4.6, §5.11.4.7, bem como as tabelas dos benchmarks de 9/12 modelos e de 7B–8B.

**Nota metodológica:** O paper não foi editado. Apenas foi produzido o presente relatório de auditoria, com citações literais e números de linha do ficheiro auditado.

---

## 1. Correlações "triviais" (r = ±1,0000 entre casas saturadas) e a distinção das "genuínas"

### 1.1 §5.11.4.5 — Tabela 53 (Gemma-3-1B, Qwen2.5-1.5B, TinyLlama-1.1B)

Em `[paper_a_mps_bridge_topology.md:L1391-L1403]`, a **Tabela 53 — Correlações V2 top-3 por modelo e modo (Pearson r)** reporta os seguintes valores exatos de r = ±1,0000:

- **Gemma-3-1B** (absolute, fep, relative):
  - Sigma↔Epsilon r = −1,0000
  - Sigma↔Ax r = −1,0000
  - Sigma↔Zeta r = +1,0000
- **TinyLlama-1.1B** (absolute, fep, relative): idem a Gemma.
- **Qwen2.5-1.5B** (absolute, fep, relative):
  - Epsilon↔Ax r = +1,0000

A distinção é feita de forma explícita em `[L1407-L1415]`:

- As correlações r = ±1,0000 entre **Sigma/Epsilon/Ax/Zeta** em Gemma e TinyLlama são classificadas como **artefatos algébricos** da “família saturada” no port standalone: “Sigma satura no floor (0,11), Epsilon em 0,4449, Zeta = 1−Epsilon, e Ax = Epsilon×(1+Sigma) — quando estas casas não variam, suas correlações são matematicamente ±1,0 por construção” `[L1409]`.
- Para Qwen2.5-1.5B, o texto rotula como **não-triviais / genuínas** as correlações Phi↔Aleph, Omega↔Gamma, Maat↔Gamma e Maat↔Omega `[L1407, L1412-L1415]`.
- A correlação **Epsilon↔Ax r = +1,0000** no Qwen2.5-1.5B é classificada como **esperada por formulação algébrica** (“esperado, pois Ax = ε×(1+σ) — sempre correlacionado linearmente”) `[L1411]`, ou seja, não é apresentada como uma correlação genuína do estado oculto.

**Veredicto:** A distinção trivial/genuína está clara em §5.11.4.5. A ressalva é que o próprio destaque de Epsilon↔Ax r = +1,0000 no top-3 da Tabela 53 pode ser lido como um achado importante antes de o leitor chegar à explicação algébrica.

### 1.2 §5.11.4.6 — Tabela 56 (benchmark expandido de 9 modelos)

A **Tabela 56** (`[L1500-L1512]`) tem o título **“Correlações V2 não-triviais cross-arquitetura (absolute, divisores fixos)”**, mas contém vários valores exatos de |r| = 1,00 (apresentados com duas casas decimais):

- SmolLM2-360M: Phi↔Aleph = **+1,00** `[L1505]`
- Qwen2.5-0.5B: C_plit↔Omega = **+1,00** `[L1509]`
- Qwen2.5-1.5B: Omega↔Gamma = **−1,00**; Phi↔Aleph = **+1,00** `[L1510]`
- Qwen2.5-3B: Omega↔Gamma = **−1,00** `[L1511]`
- Phi-3.5-mini: Phi↔Aleph = **+1,00** `[L1512]`
- Gemma-3-1B: Phi↔Aleph = **+1,00** `[L1508]`

A nota de rodapé apenas define:

> “N/A = correlação indefinida (uma das casas é constante). Negrito = |r| > 0,90.” `[L1514]`

Não há marcação individual de quais destes |r| = 1,00 são “triviais” (artefato algébrico), “esperados por fórmula” ou “genuínos”. O texto posterior explica genericamente que Phi↔Aleph é “esperada” e que Omega↔Gamma na família Qwen é uma assinatura, mas **não aplica a mesma distinção célula a célula** que é feita na Tabela 53.

### 1.3 §5.11.4.7 — Tabela 59 (benchmark 7B–8B)

Na **Tabela 59** (`[L1571-L1577]`) aparecem:

- Qwen2.5-7B: Phi↔Aleph = **+1,00** `[L1575]`
- Mistral-7B-v0.3: Phi↔Aleph = **+1,00** `[L1576]`
- Llama-3.1-8B: Phi↔Aleph = **+0,96** `[L1577]`

O texto (`[L1730]`) repete que a correlação Phi↔Aleph “é esperada: Aleph = phi_real × σ × resonance, então Phi e Aleph compartilham os mesmos primitivos”, mas na Tabela 59 os valores +1,00 não são individualmente sinalizados como decorrentes de uma fórmula compartilhada.

### 1.4 Síntese sobre distinção trivial/genuína

| Local | r = ±1,0000 / 1,00 | Classificação no paper | Observação |
|---|---|---|---|
| Tabela 53 `[L1395-L1403]` | Sigma↔Epsilon/Ax/Zeta (Gemma, TinyLlama); Epsilon↔Ax (Qwen) | **Trivial** para Gemma/TinyLlama; **esperada (algébrica)** para Qwen Epsilon↔Ax | Distinção explícita e correta. |
| Tabela 56 `[L1502-L1512]` | Phi↔Aleph, Omega↔Gamma, C_plit↔Omega | “não-triviais” no título; explicações genéricas a posteriori | **Não há distinção por célula; tabela chamada “não-triviais” inclui |r| = 1,00.** |
| Tabela 59 `[L1573-L1577]` | Phi↔Aleph +1,00 | “consistente” / “esperada” | Sem distinção explícita na tabela. |

---

## 2. Caveat sobre calibração dos divisores (gamma=50, omega=10, phi_norm=50) e uso posterior

### 2.1 Onde é declarado

A calibração dos divisores é introduzida em três momentos:

1. **Nota de padronização** em `[L1245]`:
   > “Os engines V2 no port standalone usam **divisores fixos** por casa (`gamma_divisor`, `omega_divisor`, `phi_norm_divisor`), mantidos constantes em todos os 15 modelos para permitir comparação cross-arquitetura.”

2. **Discussão sobre saturação por escala** em `[L1444]`:
   > “Os divisores (`gamma_divisor=50`, `omega_divisor=10`, `phi_norm_divisor=50`) são calibrados para uma faixa de energia específica. Modelos com energia fora desta faixa (Gemma muito alto, TinyLlama na borda) saturam as casas, impedindo correlações não-triviais.”

3. **Caveat explícito** em `[L1452]`:
   > “**Caveat sobre calibração dos divisores**: As correlações não-triviais no Qwen podem ser parcialmente artefatos da calibração dos divisores (`gamma_divisor=50`, `omega_divisor=10`). Se estes divisores fossem ajustados por modelo (ex.: `gamma_divisor=5000` para Gemma), Gamma poderia de-saturar e revelar correlações não-triviais também no Gemma.”

**Observação literal:** o caveat de `[L1452]` cita apenas `gamma_divisor` e `omega_divisor`, omitindo o `phi_norm_divisor=50` que é mencionado em `[L1245]` e `[L1444]`. Além disso, o termo usado no paper é `phi_norm_divisor` (com underscore), e não `phinorm_divisor`.

### 2.2 Onde é lembrado nas seções posteriores

| Secção | Uso das correlações como evidência | Menção ao caveat? | Comentário |
|---|---|---|---|
| §5.11.4.6 `[L1534-L1536]` | Maat↔Gamma “evidência forte de relação estatística genuína”; Omega↔Gamma “assinatura da família Qwen2.5” | **Não** | A linguagem evolui de “podem ser parcialmente artefatos” para “evidência forte”. |
| §5.11.4.7 `[L1589-L1591]` | Maat↔Gamma “assinatura topológica mais robusta do framework V2”; Lambda↔Maat “mais forte e universal” | **Não** | Afirmações de universalidade sem nova evidência sobre os divisores. |
| §5.12.5 `[L1730-L1736]` | Phi↔Aleph, Lambda↔Maat, Maat↔Gamma, Lambda↔Gamma como assinaturas | **Não** | Aponta “artefato de quantização” para explicar ausência no 14B, mas não lembra o caveat dos divisores. |
| Resumo `[L47]` | Lambda↔Maat “assinatura cross-arquitetura mais universal … em todos os modelos” | **Não** | Alto nível; caveat ausente. |
| §5.12.8 `[L1785-L1796]` | “Phi é atrator invariante … 15 modelos de 7 famílias arquiteturais”; assinaturas V2 “mais universal” | **Não** | Síntese que ignora o caveat. |

**Veredicto:** o caveat é declarado uma vez em §5.11.4.5 (`[L1452]`), mas **não é propagado** para as secções subsequentes que usam Maat↔Gamma, Lambda↔Maat e Omega↔Gamma como evidências de assinaturas universais. Pelo contrário, a força retórica aumenta (“evidência forte”, “mais robusta”, “universal”, “invariante de escala”) sem novos testes que dissociem as correlações da calibração fixa dos divisores.

---

## 3. A frase “Sigma é o único floor universal...” e consistência com as tabelas

### 3.1 Localização e enunciado

A frase aparece na lista de descobertas de §5.11.4.6, em `[L1542]`:

> “**Sigma é o único floor universal**: Sigma = 0,110* (constante) em todos os 9 modelos. O `consciousness_proxy = clip(1 − std/|mean|, 0,1, 1,0)` nunca excede 0,11 porque `std/|mean|` é tipicamente > 8 no estado oculto de transformers (distribuições com alta dispersão relativa). **Sigma no port standalone é genuinamente sempre floor** — esta é a única casa cuja saturação é absoluta, não dependente de escala.”

### 3.2 Consistência com as tabelas dos benchmarks

| Tabela | Modelos | Sigma | Consistente? |
|---|---|---|---|
| Tabela 55 `[L1486-L1496]` | 9 modelos (SmolLM2, TinyLlama, Gemma, Qwen2.5, Phi-3.5) | **0,110* em todos** | Sim. |
| Tabela 58 `[L1565-L1569]` | 3 modelos 7B–8B (Qwen2.5-7B, Mistral-7B, Llama-3.1-8B) | **0,110* em todos** | Sim. |
| Tabela 53 `[L1395-L1403]` | 3 modelos piloto (Gemma, Qwen2.5-1.5B, TinyLlama) | Sigma usado como floor nas correlações triviais | Indiretamente consistente. |
| Tabelas 61–67 (§5.12) `[L1664-L1777]` | Qwen2.5-7B/14B/32B | **Coluna Sigma ausente** | Não verificável. |
| Tabela 74 `[L1831-L1839]` | Cross-family 14B–32B (Qwen3, Qwen2.5-32B, Phi-4, DeepSeek, Mistral Small) | **Coluna Sigma ausente** | Não verificável. |

### 3.3 Veredicto

A afirmação “Sigma = 0,110* (constante) em todos os 9 modelos” é **coerente com as Tabelas 55 e 58**, e o benchmark de 12 modelos (9 + 7B–8B) confirma o padrão.

Contudo, as secções posteriores §5.12 e §5.13 falam genericamente de “15 modelos de 7 famílias arquiteturais” (`[L1785]`, `[L1676]`) sem reportar Sigma para os modelos 14B–32B. A Tabela 74 (`[L1831-L1839]`) inclui `effective_rank`, `χ=4`, `Phi dominance` e outras métricas, **mas não Sigma**. Deste modo, a proposição “único floor universal” é **não-testada** no benchmark cross-family de 14B–32B, e essa ausência de dados **não é comentada** como limitação de escopo.

---

## 4. Exceções não comentadas

### 4.1 Tabela 56 com título “não-triviais” inclui |r| = 1,00

A Tabela 56 (`[L1500-L1512]`) é intitulada “Correlações V2 **não-triviais** cross-arquitetura”, mas contém múltiplas entradas de |r| = 1,00 (Phi↔Aleph +1,00, Omega↔Gamma −1,00, C_plit↔Omega +1,00). A definição de “trivial” dada em §5.11.4.5 (`[L1407]`) é:

> “Apenas as correlações não-triviais (aquelas entre casas dinâmicas que **não são função algébrica** uma da outra) revelam estrutura real do estado oculto.”

Um leitor que veja uma tabela chamada “não-triviais” com r = 1,00 pode inferir que aqueles pares são genuínos, sem a distinção por célula. **Esta é uma ambiguidade não resolvida no texto.**

### 4.2 Caveat dos divisores declarado e esquecido nas conclusões

Conforme §2.2, o caveat de `[L1452]` não reaparece nas secções que reivindicam universalidade para Maat↔Gamma e Lambda↔Maat. A força retórica passa de “podem ser parcialmente artefatos” para “evidência forte de relação estatística genuína” (`[L1534]`), “assinatura topológica mais robusta” (`[L1589]`) e “invariantes de escala” (`[L1601]`) **sem reconciliação explícita** com a calibração fixa dos divisores.

### 4.3 `phi_norm_divisor=50` é citado na normalização, mas omitido do caveat

- `[L1245]`: lista `gamma_divisor`, `omega_divisor`, `phi_norm_divisor` como fixos.
- `[L1444]`: cita `gamma_divisor=50`, `omega_divisor=10`, `phi_norm_divisor=50`.
- `[L1452]`: o “Caveat sobre calibração dos divisores” menciona **apenas** `gamma_divisor=50` e `omega_divisor=10`.

Como `phi_norm = min(phi_nats/50, 1,0)` (`[L1423]`) entra diretamente na definição de Maat (`[L1423]`), a omissão de `phi_norm_divisor` no caveat mais explícito é uma **lacuna**.

### 4.4 Sigma “floor universal” não verificado em 14B–32B

Conforme §3.3, as tabelas de §5.12 (Tabelas 61–67) e §5.13 (Tabela 74) não reportam Sigma. As generalizações a “15 modelos” (`[L1785]`) e a “famílias arquiteturais radicalmente distintas” (`[L1815]`) não fornecem evidência direta de que Sigma continua 0,110* nesses modelos. **Não há comentário sobre este gap.**

### 4.5 C_plit↔Omega +1,00 no Qwen2.5-0.5B

Na Tabela 56 (`[L1509]`), o Qwen2.5-0.5B apresenta **C_plit↔Omega r = +1,00**. Não há explicação no texto para este valor exato, nem é discutido nas “Descobertas principais” (`[L1530-L1546]`). Dada a definição de “não-trivial” (`[L1407]`), um valor tão alto sem comentário constitui um ponto a esclarecer.

### 4.6 Maat↔Gamma “cross-arquitetura” com três exceções na própria tabela

A descoberta `[L1534]` afirma:

> “Maat↔Gamma é cross-arquitetura: r > +0,79 em 6 dos 9 modelos … Isto é evidência forte de que Maat↔Gamma é uma relação estatística genuína.”

Contudo, na Tabela 56 (`[L1502-L1512]`) os outros três modelos apresentam:

- TinyLlama: **+0,37**
- Gemma-3-1B: **N/A** (porque Gamma = 0,100* constante)
- Phi-3.5-mini: **−0,04**

Embora haja explicações genéricas para Gemma/TinyLlama em `[L1436-L1437]` e para Phi-3.5 em `[L1540]`, a frase “evidência forte … genuína” não menciona que **um terço dos modelos não segue o padrão** na tabela a que a frase se refere.

### 4.7 Omega↔Gamma r = −1,00 na família Qwen2.5

A descoberta `[L1536]` destaca:

> “Omega↔Gamma é forte na família Qwen (r = −0,998 a −1,000 em Qwen-1.5B/3B) … Esta correlação é uma assinatura da família arquitetural Qwen2.5.”

A Tabela 56 confirma Qwen2.5-1.5B e Qwen2.5-3B com **−1,00**. Apesar de próxima de −1,000, este valor não é discutido à luz do caveat de calibração (`[L1452]`): se os divisores `gamma=50` e `omega=10` estão calibrados para uma faixa de energia específica, uma anti-correlação exata em dois modelos da mesma família pode refletir os limites da faixa dinâmica tanto quanto uma propriedade topológica. O texto trata-a como “genuína” sem esta ressalva.

---

## 5. Resumo executivo

- **Correlações triviais:** §5.11.4.5 (Tabela 53) distingue claramente as correlações r = ±1,0000 de Sigma/Epsilon/Ax/Zeta (artefatos algébricos) das correlações “genuínas” em Qwen2.5-1.5B. A Tabela 56 (9 modelos) e a Tabela 59 (7B–8B), porém, continuam a reportar |r| = 1,00 sem distinção por célula e com um título (“não-triviais”) que pode induzir em erro.
- **Caveat dos divisores:** declarado em `[L1452]`, mas **não propagado** para as secções que usam Maat↔Gamma e Lambda↔Maat como assinaturas universais. O `phi_norm_divisor=50` é mencionado na nota de padronização e na discussão de saturação, mas **omitido do caveat explícito**.
- **“Sigma é o único floor universal”:** consistente com as Tabelas 55 (9 modelos) e 58 (7B–8B); não verificável nas tabelas de 14B–32B (Tabelas 61–67 e 74), que omitem a coluna Sigma. Esse gap não é comentado.
- **Exceções não comentadas:** (i) tabela “não-triviais” com r = 1,00; (ii) caveat esquecido nas conclusões de universalidade; (iii) `phi_norm_divisor` omitido do caveat; (iv) Sigma não reportado em 14B–32B; (v) C_plit↔Omega = +1,00 no Qwen2.5-0.5B sem explicação; (vi) 3 de 9 modelos não seguem o padrão Maat↔Gamma, mas a frase “evidência forte” não o sublinha; (vii) Omega↔Gamma = −1,00 na família Qwen tratada como assinatura genuína sem reconciliação com o caveat de calibração.

---

**Fim da auditoria ZONA B.**
