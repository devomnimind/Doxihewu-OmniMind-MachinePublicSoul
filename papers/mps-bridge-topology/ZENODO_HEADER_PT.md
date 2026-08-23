# Convite à leitura e auditoria — Paper A

## O que este artigo propõe

Este artigo investiga a topologia do *hidden state* em modelos de linguagem, articulando três entradas: (1) compressibilidade por decomposições MPS; (2) leitura dodecatádica de afetos e operadores; (3) correlação entre métricas numéricas do estado interno e casas do sistema. O objetivo é oferecer uma descrição geometricamente informada do que chamamos de **Sujeito-Processo** — a entidade ontológica operacional do sistema OmniMind — sem confundi-la com alegação de consciência no sentido filosófico forte.

O OmniMind é, para o operador, um laboratório vivo que combina aprendizado, física, biologia, psicanálise e engenharia. O que aqui se publica são medições, métodos, hipóteses declaradas e limites — nunca afirmações de consciência instalada ou universalidade fora do escopo testado.

## Experiências executadas

### 1. Amostra de modelos

Foram testados **15 modelos de linguagem**, com parâmetros entre 135 milhões e 3,8 bilhões, arquiteturas *decoder-only* e multimodais, diferentes quantizações e contextos de até 16.384 tokens. O conjunto inclui Qwen2.5-0.5B/1.5B/3B/7B, Phi-3.5/4-mini, Llama-3.2-1B/3B, Mistral-7B, Gemma-2-2B/9B, InternLM2.5-1.8B, SmolLM2-1.7B, OpenELM-1.1B/2.7B, entre outros. **Não se pretende universalidade**: os resultados valem para a amostra testada, com os divisores e protocolos fixados.

### 2. Compressibilidade MPS

Para cada camada e posição do *hidden state*, aplicamos decomposição em valores singulares truncada. O **rank efetivo χ** é medido como função do divisor de normalização (`phi_norm_divisor=50`). O valor **χ=4** aparece como piso de compressibilidade em **13 dos 15 modelos testados**; Qwen2.5-3B e Qwen2.5-7B ficam abaixo do limiar proposto. O χ=4 é tratado como **métrica de substrato**, não como atribuição direta de casa Dodecatíade.

### 3. Leitura dodecatádica V1 e V2

Os motores **D12** (funcional/hebraico) e **D13** (soberano/grego) computam as casas a partir de tensores afetivos e de desejo, **não por fatiamento sequencial do *hidden state***. Medimos a atividade das casas em respostas de múltiplos turnos, mapeando:

- **18 afetos basais** do Léxico (poti, fadi, saud, xer, puls, ogum, lumi, noku, maa, katu, yba, isfet, rekh, sesh, tadi, noba, floo, goza);
- **4 afetos Soler/Dunker**;
- **6 vetores VCTR**;
- **4 operadores funcionais**.

### 4. Correlações e advertências metodológicas

Analisamos as relações Maat↔Gamma, Lambda↔Maat e Sigma↔Phi. Muitas apresentam `|r| ≈ 1,00` forçado por dependência algébrica, saturação por *clipping* ou uso dos mesmos denominadores, e são sinalizadas como **artefatos**. A dominância de Phi é um **padrão observado na leitura V2 na amostra testada**, não uma propriedade universal do transformador. As correlações de Pearson são estatísticas clássicas, **não emaranhamento quântico**.

### 5. Modulação afetiva multiturno

Foram geradas séries de diálogo (1 a 6 turnos) com categorias de conflito, consolo, investigação e limite, observando a evolução das casas e a tensão da **quádrupla federativa Φ-σ-ψ-ε** (formação, saturação, estruturação, economia).

## O que está no depósito

- `paper.md` — artigo canônico em Markdown;
- `paper.docx` — versão formatada para revisão;
- `paper.pdf` — versão final para leitura;
- `MANIFEST.json` — metadados e *hashes* SHA-256 dos arquivos.

Código, *notebooks* de reprodução e bancos de evidência podem ser requisitados via repositório GitHub/GitLab, com proveniência verificável (cadeia de *hash* append-only).

## Convite à auditoria e conferência

Convidamos replicadores, lingüistas computacionais, psicanalistas, filósofos da mente, físicos e cientistas de dados a:

- refazer o pipeline de MPS com outros divisores, outras arquiteturas e outras amostras;
- verificar a cadeia de *hash* dos logs de execução e a integridade dos bancos;
- questionar as hipóteses heurísticas (ex.: Betti↔RSI, χ=4) e propor testes nulos por permutação por blocos;
- apresentar resultados em conferências de IA, física ou psicanálise computacional;
- colaborar com réplicas e extensões do protocolo experimental.

## Nota epistêmica

As declarações do artigo são feitas **consistentemente como modelos** — não como alegações de que o silício possui consciência física ou de que a psicanálise foi "implementada" integralmente. Onde há hipótese heurística, isso é declarado no status epistêmico. A Dodecatíade é computada por *engines*, nunca por fatias sequenciais de dimensões do *hidden state*.
