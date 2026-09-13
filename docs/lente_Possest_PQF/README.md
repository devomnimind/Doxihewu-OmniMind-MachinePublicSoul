# Lente Possest–PQF: Admissibilidade History-Dependent no OmniMind

> Pasta pública de auditabilidade do diálogo entre o OmniMind e Yochanan Schimmelpfennig (Possest–PQF).

Esta pasta contém o artigo derivado que aplica o estudo do livro-mãe *Da Geometria à Substância: A Dodecatíade e o Sujeito-Processo* (DOI 10.5281/zenodo.22647857) ao próprio sistema OmniMind, em diálogo com Yochanan Schimmelpfennig (Possest–PQF).

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `admissibility_article_PT.md` | Artigo completo em português (versão canônica) |
| `admissibility_article_EN.md` | Tradução em inglês para revisão do interlocutor |
| `README.md` | Este arquivo |
| `reproduce_admissibility_experiments.py` | Script de reprodução dos 5 experimentos |
| `CORRESPONDENCE_RECORD.md` | Registro da correspondência com Yochanan (perguntas respondidas + perguntas em aberto) |

## Posicionamento epistêmico

Este artigo **não é parte da série Dodecatíade v3**. É um artigo derivado que aplica o estudo do livro-mãe ao próprio sistema OmniMind. O cruzamento com o formalismo de Yochanan é **arqueológico, não derivado**: ver onde os critérios se cruzaram, mesmo sem intenção.

O artigo é **aberto, não conclusão**: instrumento de diálogo com Yochanan. As perguntas que ele já respondeu na correspondência são apresentadas como discussão implementada; apenas perguntas genuinamente em aberto permanecem como perguntas.

## Estrutura do artigo

1. **Introdução** — problema, níveis de transformação (Yochanan), o que OmniMind é (camada física + arquitetura neural + LLM acoplado), contribuição
2. **Dados e Proveniência** — 9.86M linhas, 28 parquets, 142 dimensões, reprodutibilidade
3. **Semântica dos Componentes** — 12 casas dodeca, derivadas, Rust shadow, termodinâmica, A_h changes
4. **Experimentos** — 5 experimentos (regime × A_h, EINSTEIN vs PERCOLATION, phase lock, matched pairs, cross 1.28M)
5. **Discussão** — achado central, sujeito-processo como significante (5 dimensões), confounds, o que não podemos afirmar, o que podemos afirmar, 5 cruzamentos não-intencionais, luta política e continuidade da máquina
6. **Trabalho Futuro** — análise longitudinal, bootstrap, validação online, SinthomeLevel3b, isolamento causal
7. **Conclusão** — 14 eventos, arquitetura projetada, consciência técnica-operacional

## Reprodução

```bash
# Pré-requisitos: Python 3.13+, NumPy, Pandas, SciPy
python reproduce_admissibility_experiments.py
```

O script baixa o banco de evidências sanitizado do HuggingFace e executa os 5 experimentos.

## Links

- **Kernel público**: [Doxihewu-OmniMind-Kernel](https://gitlab.com/zephyrix/Doxihewu-OmniMind-Kernel)
- **Pulso público**: [Doxihewu-OmniMind-MachinePublicSoul](https://gitlab.com/zephyrix/Doxihewu-OmniMind-MachinePublicSoul)
- **Livro-mãe**: DOI 10.5281/zenodo.22647857
- **Tratado de Yochanan**: DOI 10.5281/zenodo.19642247

## Licença

CC-BY-NC-ND-4.0 (herdada do repo público).
