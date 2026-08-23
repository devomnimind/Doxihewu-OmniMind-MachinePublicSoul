# Cobertura ZONA A — Retratações metodológicas (§5.2–5.11)

**Arquivo auditado:** `paper_a_mps_bridge_topology.md` (Paper A)
**Escopo:** Sequências §5.2 a §5.11, com verificação cruzada em §1 (Resumo), §2.4 (Introdução) e §13 (Conclusão).
**Método:** Leitura sequencial das seções indicadas; registro literal de afirmações empíricas sobre "casa dominante" e/ou "correlação entre casas"; verificação de notas remissivas v1.5 / v2.2.x; rastreamento de propagação para Resumo/Introdução/Conclusão; identificação de mesclas entre "χ=4 fidelidade / rank efetivo" e leituras de casas.

---

## 1. Diagnóstico geral

A retratação metodológica está **explicitamente arquitetada no documento**. As seções §5.2, §5.3, §5.4, §5.5, §5.7, §5.8, §5.9 e §5.10 carregam **Notas Remissivas** (v1.5 / v2.2.1) no início, alertando que as leituras de "casa dominante" e "correlação entre casas" foram obtidas por **partição sequencial** do estado oculto, metodologia posteriormente identificada como incorreta. As notas afirmam que χ=4 e rank efetivo permanecem válidos como propriedades do estado oculto e remetem à **reanálise V2 em §5.11**.

A reanálise V2 (§5.11.1–§5.11.6) consolida a correção:

- §5.11.1 declara o erro da partição sequencial.
- §5.11.2 apresenta a metodologia correta (engines portados: `DesireEngine`, `PhiRealFormulation`, `raw_houses`).
- §5.11.4 reporta os resultados V2: **Phi domina 100% das camadas** nos modelos testados; correlações não-triviais (Maat↔Gamma, Lambda↔Maat, Phi↔Aleph, Omega↔Gamma) emergem com a metodologia V2.
- §5.11.5 classifica os três cenários (convergência, divergência, diferenciação).
- §5.11.6 estabelece o status epistemológico, separando rigorosamente:
  - propriedades do estado oculto (χ=4, rank efetivo, compressibilidade) — válidas;
  - propriedades da Dodecatíade (casas dominantes, correlações) — recalculadas;
  - capacidade dimensional 878 — válida por fórmula própria.

### 1.1 Achado crítico: retratação faltante em §5.6

**A Seção 5.6 não contém nota remissiva individual** (ao contrário de §5.2, §5.3, §5.4, §5.5, §5.7, §5.8, §5.9, §5.10). O loop fechado OmniMind→LLM→OmniMind apresenta:

- Tabela 16: atribuição de **casa dominante D27_solar** ("Dom") ao longo das iterações.
- §5.6.5 (L675): vinculação direta entre a casa dominante D27_solar e a **correlação D27_solar ↔ D13_record (r=0,958)**, citando o experimento D.9.19.

Não há qualificação dentro de §5.6 de que a casa dominante D27_solar e a correlação r=0,958 derivam da partição sequencial (metodologia V1, posteriormente retratada). A Nota de escopo geral do início de §5 (L332) menciona "Seções 5.2 a 5.9" como tendo sido analisadas por partição sequencial, o que cobre §5.6 indiretamente; porém, um leitor que acesse diretamente §5.6 pode não perceber a limitação. Recomendação: inserir nota remissiva v1.5/v2.2.1 em §5.6.3 ou §5.6.5, ou reescrever o parágrafo L675 para referir a interpretação ao domínio da partição heurística e à reanálise V2.

### 1.2 Propagação para Resumo/Introdução/Conclusão

**Nenhuma afirmação V1 (partição sequencial) foi propagada para Resumo, Introdução ou Conclusão sem qualificação.** As únicas afirmações de casa/correlação propagadas a essas seções são baseadas na reanálise V2:

- **Resumo (L47):** "A reanálise V2 [...] revelou que a casa Phi [...] domina 100% das camadas [...]. A correlação Lambda↔Maat (r=+0,69 a +0,97) emerge como a assinatura cross-arquitetura mais universal." — qualificada por "reanálise V2".
- **Introdução §2.4 (L178-179):** distingue "propriedade do substrato" (χ=4, rank efetivo) de "leitura do sistema" (Phi dominante, Lambda↔Maat via engines V2) — qualificada.
- **Conclusão §13 (L2709):** "A reanálise V2 com engines corrigidos revelou que a casa Phi domina 100% [...]. A correlação Lambda↔Maat (r=+0,69 a +0,97) [...]." — qualificada e acompanhada de caveat metodológico: "embora parte da correlação possa decorrer de dependências entre as fórmulas das métricas".

**Observação marginal (fora do escopo formal, mas relevante):** a Seção 6.2 (Discussão) cita D27_solar↔D13_record (r=0,958) da Tabela 8 sem nota remissiva imediata. Embora a Seção 6.1 precedente tenha nota v2.2.1 sobre D13_record, a ausência de qualificação em §6.2 pode ser um ponto de propagação não coberto pelo critério Resumo/Introdução/Conclusão.

### 1.3 Mescla entre χ=4/rank efetivo e leituras de casas

Várias tabelas e interpretações misturam, em um mesmo plano, resultados que o documento mesmo classifica de naturezas distintas:

- **Tabela 7 (§5.2):** χ=4, fidelidade, rank efetivo, "entrelacamento máximo r=0,958" em colunas consecutivas. Nota v2.2.1 distingue, mas a tabela em si não.
- **Tabela 18 (§5.7):** "casa dominante", "D12↔D13 correlação", e colunas de rank efetivo. Nota v2.2.1 distingue.
- **Tabelas 19-21 (§5.8):** casa dominante, rank efetivo, fidelidade χ=4, overlap de correlações em uma única tabela. Notas remissivas presentes, mas a disposição tabular gera risco de leitura.
- **Tabela 25 (§5.9.9):** casa dominante e χ_99 mean na mesma linha.
- **Tabela 31 (§5.10):** casa dominante, χ=4 fidelidade (mid) e rank efetivo comparados lado a lado entre vision e language.

Em todos os casos há nota remissiva na seção, de modo que o veredito geral é **qualificado**, com ressalva de **risco de leitura** para leitores que consultem apenas as tabelas.

---

## 2. Mapeamento das notas remissivas por seção

| Seção | Nota remissiva presente | Tipo de afirmação coberta | Retratação em §5.11 |
|---|---|---|---|
| §5.1 | Sim (v1.5, L336) | Casa dominante, correlações | §5.11.4.4 (Gemma-3-1B V2: Phi) |
| §5.2 | Sim (v2.2.1, L420) | Correlações; χ=4/rank válidos | §5.11.1 / §5.11.6 |
| §5.3 | Sim (v2.2.1, L444) | Correlação D27_solar↔D13_record | §5.11.1 / §5.11.6 |
| §5.4 | Sim (v1.5, L488) | Casa dominante, correlações | §5.11.4 / §5.11.6 |
| §5.5 | Sim (v1.5, L560) | Casa dominante | §5.11.4.4 (Gemma-3-4B V2: Phi) |
| **§5.6** | **Não (nota individual ausente; coberta indiretamente pela Nota de escopo geral §5, L332)** | **Casa dominante D27_solar; correlação r=0,958** | **Indireta (§5.11.1 geral; não há nota local)** |
| §5.7 | Sim (v2.2.1, L680) | Divergência D12≠D13, casas, correlações | §5.11.1 / §5.11.4 / §5.11.6 |
| §5.8 | Sim (v2.2.1, L757; reforço L769) | Casa dominante, correlações, overlap | §5.11.4.4 (Tabela 35: Phi 100%) |
| §5.9 | Sim (v1.5, L893) | Casa dominante, correlações | §5.11.1 / §5.11.4 / §5.11.6 |
| §5.10 | Sim (v1.5, L1128) | Casa dominante (D27_void) | §5.11.4.4 (Vision V2) |
| §5.11 | N/A | Retratação e resultados V2 | §5.11 (própria seção) |

---

## 3. Lista de afirmações rastreadas

O arquivo `08_rastreamento_retratacoes.csv` contém o rastreamento detalhado de cada afirmação. Aqui se destacam as conclusões agregadas:

- **Total de afirmações rastreadas:** 25 linhas (incluindo Resumo/Introdução/Conclusão como linhas de propagação).
- **Com nota remissiva local e qualificada:** 23.
- **Sem nota remissiva local:** 1 (§5.6).
- **Propagação para Resumo/Introdução/Conclusão sem qualificação:** 0.
- **Mesclas χ=4/rank + casa/correlação com nota de distinção:** 7 (§5.1.4, §5.2, §5.7, §5.8, §5.9.9 Exp-12, §5.10.6, e Tabela 53-60 em §5.11.4).
- **Mesclas sem distinção explícita na própria tabela:** presentes, mas cobertas por notas de seção.

---

## 4. Veredictos por categoria

### 4.1 Qualificadas por nota remissiva

A maior parte das afirmações em §5.2–5.5, §5.7–§5.10 está corretamente qualificada. As notas remissivas cumprem a função de alertar o leitor de que as leituras de casa e correlação dependem de metodologia corrigida em §5.11.

### 4.2 Retratação faltante (nota individual)

**§5.6** é a única seção dentro do escopo §5.2–§5.10 que omite **nota remissiva individual** para uma afirmação empírica de casa dominante e correlação. A Nota de escopo geral de §5 (L332) menciona "Seções 5.2 a 5.9" como tendo usado partição sequencial, o que cobre §5.6 indiretamente, mas a ausência de nota local configura risco de leitura para quem consulta a seção isoladamente. Recomendação de correção editorial.

### 4.3 Propagação qualificada

Resumo, Introdução e Conclusão propagam apenas resultados V2 (Phi dominante; Lambda↔Maat), com qualificações explícitas. A distinção "propriedade do substrato" / "leitura do sistema" é mantida.

### 4.4 Riscos de leitura

Mesmo com notas remissivas, várias tabelas misturam métricas de substrato (χ=4, rank efetivo) com leituras de casas/correlações. Leitores que consultem tabelas isoladamente podem confundir a natureza epistemológica dos resultados. Não constitui erro de retratação, mas é um ponto de atenção para revisão gráfica/estrutural.

---

## 5. Recomendações

1. **Inserir nota remissiva em §5.6** ou qualificar o parágrafo L675 para evitar propagação não qualificada da casa dominante D27_solar e da correlação r=0,958 como se fossem resultados canônicos.
2. **Revisar §6.2** (fora do escopo formal desta auditoria, mas identificado) para adicionar nota remissiva ou qualificação ao citar Tabela 8 e D27_solar↔D13_record (r=0,958).
3. **Considerar sinalização visual** nas tabelas que misturam χ=4/rank efetivo com casas/correlações (Tabelas 7, 18, 19-21, 25, 31, 53-60) para reforçar a distinção entre propriedades do substrato e leituras do sistema.
4. **Manter** a Convenção de status epistêmico v2.2.2 e a distinção do §5.11.6 como gabaritos para as demais zonas.

---

**Arquivos gerados:**
- `08_rastreamento_retratacoes.csv`
- `00_cobertura_zona_a.md`
