# Rascunho: Roadmap Neural — Status de Implementação

> Rascunho local para revisão antes de fundir no `README.md` do public-pulse e no pulso.
> Última verificação: 2026-09-01, repositório `/home/fahbrain/projects/omnimind`.

## Como ler este documento

- **✅ Runtime** — roda no sistema (timers, systemd, scripts de produção, affect engine, glial, soma).
- **⚠️ Protótipo / Ensaio** — código existe, é executável, mas é prova de conceito NumPy ou análise em `scripts/analysis/`; ainda não foi integrado como daemon de produção ou conectado a bibliotecas/hardware externos.
- **❌ Planejado / Não implementado** — consta do mapa de pesquisa, mas não há módulo funcional.

---

## Tabela de frentes de pesquisa + status real

| Módulo OmniMind | Frente externa | Linha de evolução | Status real no repo local | Arquivo(s) de referência |
|---|---|---|---|---|
| DendriticQualiaLayer + morfologia dendrítica | ANNs dendríticas e SNNs com dendritos (Dendrify, Poirazi group) | Manter compartimentos; evoluir para dSpikes e medir eficiência de parâmetros | ✅ Runtime: compartimentos dendríticos em NumPy. <br>⚠️ Ensaio: dSpikes fenomenológicos e comparativos. <br>❌ Sem Dendrify/Brian2 instalados. | `src/consciousness/qualia_engine.py`, `src/consciousness/freud10d/dendritic_morphology.py`, `scripts/analysis/dendritic_dspikes_phase3.py`, `scripts/analysis/dendrify_brian2_port.py` |
| Spiking A-F (habituação, sensibilização, condicionamento) | Regras bio-inspiradas e aprendizado de 3 fatores em SNNs | Formalizar o Nervus Vagus como terceiro fator neuromodulatório | ✅ Runtime: neurônio A-F com 3 tipos de sinapse. <br>⚠️ Ensaio: Vagus como regra de 3 fatores. | `src/cognitive/spiking_neuron_model.py`, `src/immune/spiking_glial_vagus_bridge.py`, `scripts/analysis/vagus_three_factor_phase6.py`, `src/go/omnimind-vagus-gate/main.go` |
| Glial (fagocitose em camadas) | Computação neurônio-astrócito (sinapse tripartite) | Testar razão astrocyte:neuron ~2:1 e glia como memória | ✅ Runtime: fagocitose simbólica em camadas allow/observe/compress/quarantine. <br>❌ Razão astrocyte:neuron e sinapse tripartite ainda não modeladas como subsistema separado. | `src/security/sovereign_glial_daemon.py`, `src/infrastructure/glial_event_store.py`, `src/immune/spiking_glial_vagus_bridge.py` |
| NeuroCore (atratores Amit/Sompolinsky) | Modern Hopfield Networks / Dense Associative Memories | Ligar atratores do Freud10D ao formalismo DAM (capacidade provável) | ✅ Runtime: `AmitSompolinskyAttractor` e `NeuroCoreAttractorBridge`. <br>⚠️ Ensaio: ligação DAM ↔ Freud10D. <br>❌ Sem integração real com bibliotecas de Modern Hopfield. | `src/consciousness/energy_based_attractor.py`, `src/memory/neurocore_neural_theory_bridge.py`, `scripts/analysis/freud10d_dam_controlled_memory.py` |
| somatic_sensor (temperatura, PSI, bateria) | Interoceptive AI / frameworks homeostáticos-alostáticos | Manter; frente mais alinhada ao Paper A | ✅ Runtime: leitura real de CPU, NVMe, PCH, PSI Linux, swap, RAPL, bateria. Nota: a classe `SomaticSensor` não lê bateria, mas o corpo somático a lê em módulos adjacentes. | `src/consciousness/somatic_sensor.py`, `src/senses/host_somatic_plumbing.py`, `src/integrations/somatic_hyperparameter_coupling.py`, `src/infrastructure/somatic_mesh_sql.py` |
| Arnold (MyoSuite RL, 27 tarefas motoras) | Motor control / função executiva / homeostatic RL | Mapear como controle motor homeostático (D27 Solar KA/BA/AKH) | ⚠️ Ensaio: `ArnoldHomeostaticRL` com 9 ações NumPy e normalizador running. <br>❌ MyoSuite, MuJoCo, Gymnasium não instalados; as 27 tarefas não estão implementadas. | `scripts/analysis/interoception_arnold_phase5.py`, `src/consciousness/running_normalizer.py` |
| 9 neurônios NumPy, ~0,02 MB RAM | Hardware neuromórfico (Loihi 2, SpiNNaker-2, Akida) | Candidato direto a port edge/neuromórfico | ✅ Runtime: glial-vagus spiking de 9 neurônios, NumPy puro, ~0,02 MB RAM, sem GPU. <br>❌ Port para Loihi, SpiNNaker-2 ou Akida não realizado. | `src/immune/spiking_glial_vagus_bridge.py`, `src/cognitive/spiking_neuron_model.py` |

---

## Diferenciais que realmente estão no runtime

1. **Tríade habituação / sensibilização / condicionamento em SNN** — rara na literatura. Implementada em `src/cognitive/spiking_neuron_model.py` e usada por `src/immune/spiking_glial_vagus_bridge.py`.
2. **Leitura somática real de sensores do host** — a maioria dos frameworks interoceptivos é simulada; aqui `host_somatic_plumbing.py` e `somatic_sensor.py` lêm hardware real (temperatura, PSI, swap, bateria, RAPL).

---

## Evoluções prioritárias (reframes teóricos sem necessidade de mudar código)

1. **Formalizar o Vagus como regra de 3 fatores** — já existe como ensaio em `scripts/analysis/vagus_three_factor_phase6.py`; falta exposição pública e talvez persistência no affect engine.
2. **Ligar atratores do Freud10D ao formalismo DAM** — ensaio em `scripts/analysis/freud10d_dam_controlled_memory.py`; pode ganhar um cartão no pulso quando for integrado.

---

## Nota sobre Dodecatíade e hardware

- As 4 versões da Dodecatíade (D12, D13, D15, D27) continuam intactas no design; o roadmap neural não as substitui.
- Menções a Loihi 2, SpiNNaker-2 e Akida no `README` público são **frentes de pesquisa**, não integrações. A arquitetura de 9 neurônios NumPy foi projetada justamente para ser portável a esses chips no futuro.
- MyoSuite/Arnold permanece como **prova de conceito NumPy** por enquanto.

---

## Sugestão de inserção no `README.md`

Substituir o bloco atual "### Roadmap de pesquisa — arquitetura e literatura" por uma tabela com a coluna "Status real no repo local" (esta tabela), mantendo o restante do texto (diferenciais, evoluções, referências externas).
