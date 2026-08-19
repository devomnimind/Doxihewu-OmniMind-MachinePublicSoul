# Security & Data-Integrity Policy

## Objetivo

Garantir que este repositório público **nunca** exponha segredos, credenciais,
dados de runtime sensíveis ou **dados fabricados apresentados como reais**.

## Regra Zero (Integridade de Dados)

- **NUNCA** gerar "pulso soberano" a partir de `random` ou valores arbitrados.
- Cada campo do pulse carrega **provenance explícita** (`source`, `path`,
  `source_present`). Se a fonte real não estiver disponível, o campo é `null` e
  `source_present=false` — jamais um valor fictício.
- Dados gerados por script e marcados como simulação **nunca** são apresentados
  como evidência empírica, calibração ou dataset baixado.

## O que este repo NÃO contém

- Tokens, chaves de API, credenciais (HF, Kaggle, GitHub, Cloudflare) — proibidos.
- Runtime, daemon de telemetria, módulos de kernel, configs de proxy/segurança
  ofensiva ou ferramentas de penetração.
- Componentes internos não descritos na versão pública do artigo.

## Reportando vazamento

Se um segredo vazar neste repositório (história do git, artefatos, ações):

1. **ROTACIONE** o segredo imediatamente no painel da plataforma.
2. Reporte a `public-soul@omnimind.software` (ou via issue se pública).
3. Não force-push sem autorização — a rotação/invalidação do token é a prioridade.

## Nota histórica

Um repositório público anterior do OmniMind foi fechado (tornado privado) após
incidentes de vazamento. Este repositório **novo** é separado e segue esta
política para o pulso público. O repositório antigo permanece privado como
arquivo histórico e será eventualmente redesenhado.
