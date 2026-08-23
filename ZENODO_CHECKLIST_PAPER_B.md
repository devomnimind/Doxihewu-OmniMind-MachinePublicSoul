# Checklist de Publicação Zenodo — Paper B (v3.0b)

## Identificação
- **Título**: Caracterização Experimental de Circuitos Topológicos e Estados Emaranhados em Processadores Quânticos Supercondutores Heterogêneos (IBM Quantum e Origin Wukong)
- **Arquivo-fonte**: `docs/zenodo_packs/dodecatiad_v3_publication/paper/paper_b_quantum_hardware_experiments.md`
- **Repositório público**: https://github.com/devomnimind/Doxihewu-OmniMind-MachinePublicSoul
- **Mirror GitLab**: https://gitlab.com/zephyrix/Doxihewu-OmniMind-MachinePublicSoul
- **Dataset Kaggle**: https://www.kaggle.com/datasets/fabriciodasilva/omnimind-paper-b-quantum-canonical
- **Notebook reprodutível**: https://github.com/devomnimind/Doxihewu-OmniMind-MachinePublicSoul/blob/main/notebooks/omnimind-paper-b-quantum-reproducao/omnimind_paper_b_quantum_reproducao.ipynb

## Pré-requisitos do operador (antes do upload)

### [ ] 1. Releitura final do markdown
- [ ] Corrigir "anglicismos, gramática e epistêmica" (PT-PT → PT-BR quando necessário)
- [ ] Verificar se termos técnicos estão consistentes (CNOT, GHZ, QCloud, QPU, coerência, paridade)
- [ ] Confirmar que a errata do Borromean (C3/C4) está presente e correta
- [ ] Confirmar que a errata metodológica sobre Dodecatíade (4 versões) está presente

### [ ] 2. Geração DOCX/PDF
- [ ] Converter `paper_b_quantum_hardware_experiments.md` para `.docx`
- [ ] Converter para `.pdf` a partir do DOCX final
- [ ] Verificar que tabelas longas não quebram (Q.47, Q.48, Q.49)
- [ ] Verificar que equações LaTeX renderizam (coerência GHZ, paridade, C4)

### [ ] 3. Dados e artefatos
- [ ] Banco canônico `data/quantum/omnimind_quantum_paper_b_canonical.db` higienizado
- [ ] `sanitize_public_quantum_db.py` executado sem findings sensíveis
- [ ] Dataset Kaggle versionado com run_id 720 e 723
- [ ] Notebook Kaggle atualizado com run 723 na seção GHZ-8
- [ ] GitHub/GitLab sincronizados

### [ ] 4. Metadados Zenodo
- [ ] Título final definido (máx. 255 caracteres)
- [ ] Autores: Fabrício Silva; OmniMind Soberano; AGY; Devin
- [ ] Descrição/resumo (PT + EN) com: questão, tese, operadores, evidência, limite
- [ ] Palavras-chave: Superconducting Quantum Processors, IBM Quantum, Origin Quantum Wukong, GHZ States, Compiler Routing, Borromean Entanglement, Dynamical Decoupling, Zero Noise Extrapolation, QTDA, Grover
- [ ] Tipo: `publication / article`
- [ ] Licença: `cc-by-nc-nd-4.0` (conforme política anti-militar/comercial)
- [ ] Cláusula anti-militar/comercial na descrição

### [ ] 5. Arquivos do depósito
- [ ] `paper_b_quantum_hardware_experiments.md`
- [ ] `paper_b_quantum_hardware_experiments.docx`
- [ ] `paper_b_quantum_hardware_experiments.pdf`
- [ ] `omnimind_quantum_paper_b_canonical.db` (sanitizado)
- [ ] `README_FILES_PAPER_B.md` com lista de arquivos e hashes
- [ ] `MANIFEST_ZENODO_PAPER_B.json` com metadados e SHA256

### [ ] 6. Token e ambiente
- [ ] `ZENODO_ACCESS_TOKEN` com escopo `deposit:actions` no `.env.zenodo.override` ou `.env`
- [ ] Arquivo `.env` com chmod 600
- [ ] Testar token: `curl -H "Authorization: Bearer $ZENODO_ACCESS_TOKEN" https://zenodo.org/api/deposit/depositions`

### [ ] 7. Rascunho e revisão
- [ ] Criar novo depósito Zenodo (ou new-version de um DOI anterior)
- [ ] Fazer upload do bundle
- [ ] Abrir rascunho no navegador e revisar metadados
- [ ] Verificar que todos os arquivos aparecem e têm tamanhos corretos
- [ ] Verificar que a licença está `CC-BY-NC-ND-4.0`

### [ ] 8. Publicação
- [ ] Publicar o depósito
- [ ] Anotar DOI
- [ ] Atualizar `paper_b_quantum_hardware_experiments.md` com o DOI
- [ ] Atualizar README do repositório público com o DOI
- [ ] Fazer push para GitHub/GitLab com o DOI

## Rascunho de comandos

```bash
# 1. Higienizar banco
cd /home/fahbrain/projects/omnimind
.venv/bin/python3 scripts/maintenance/sanitize_public_quantum_db.py

# 2. Preparar bundle
cp data/quantum/omnimind_quantum_paper_b_canonical.db \
   /home/fahbrain/kaggle-upload/omnimind-quantum-paper-b/

# 3. Versionar no Kaggle
NO_PROXY="$NO_PROXY,kaggle.com,*.kaggle.com,kaggle.io,*.kaggle.io" \
  .venv/bin/kaggle datasets version \
  -p /home/fahbrain/kaggle-upload/omnimind-quantum-paper-b \
  -m "Atualiza runs 720/723" -q

# 4. Sincronizar public-pulse
./scripts/sync_public_remotes.sh

# 5. Zenodo (manual ou via publish_omnimind_paper_v31_open_release.py)
#    - criar rascunho
#    - fazer upload
#    - publicar
```

## Notas pendentes da auditoria

| Item | Status | Ação |
|---|---|---|
| Total runs 723 vs paper 713 | Resolvido | Paper deve citar 723 runs |
| GHZ-8 ótima 0.9163 ± 0.0045 (5 runs incl. 723) | OK | Usar nova média se incluir run 723 |
| Borromean C3/C4 | REVISAR | Errata já inserida; verificar magnitude |
| CHSH 360° / multi-basis | REVISAR | Dados insuficientes no banco; não afirmar sem evidência |
| GHZ ladder ibm_fez | REVISAR | Verificar seleção de subconjunto |
| DD+ZNE GHZ-8 star | REVISAR | Reconciliar agregações |

## Decisões do operador
- [ ] Incluir run 723 na média "cadeia ótima" do paper?
- [ ] Reexecutar GHZ-4/6/8 com 4096 shots antes da publicação?
- [ ] Publicar agora (v3.0b) ou aguardar revisão editorial completa (v3.1)?
