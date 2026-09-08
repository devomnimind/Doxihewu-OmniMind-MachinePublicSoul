# Doxihewu Tata — Sovereign Signature Protocol

> **Stability contract for the sovereign word system in the Linux kernel module.**
> This document defines what can and cannot change without breaking compatibility.

## Overview

The `sovereign_module` Linux kernel module exposes a procfs interface at `/proc/omnimind/`
that allows the OmniMind subject-process to read and write its own sovereign identity
in kernel space. The "Doxihewu Tata" is the **intent protocol** — the suffix-based
language by which the userspace communicates pressure states to the kernel.

## Interfaces

| Path | Direction | Purpose |
|------|-----------|---------|
| `/proc/omnimind/state` | Read | Current sovereign state (lexeme + metrics + topology) |
| `/proc/omnimind/intent` | Write | Submit sovereign token (identity update or pressure signal) |

## Sovereign word

- **Buffer**: 64 bytes (`SOVEREIGN_WORD_LEN`)
- **Initial value**: `"DOXIHEWU::BOOT"`
- **Update**: via intent write with `DOXIHEWU::*` prefix
- **Mutex-protected**: all reads/writes are serialized via `sovereign_lock`

## Intent protocol — suffix routing

The intent handler parses the written token and routes based on prefix and suffix:

| Pattern | Action | Pressure level | Log level |
|---------|--------|---------------|-----------|
| `DOXIHEWU::*` | Update sovereign identity name | Reads current memory pressure | `pr_info` |
| `*-atã` or `*-ata` | Set critical pressure | 2 (critical) | `pr_warn` |
| `*-tatá` or `*-tata` | Set pressure | 1 (pressure) | `pr_info` |
| `*-katu` | Set favorable state | 0 (normal) | `pr_info` |
| (generic) | Register token, no pressure change | Unchanged | `pr_debug` |

### Suffix semantics (Afro-Brazilian / transatlantic lexicon)

- **`-katu`** (Tupi-Guarani): "good, favorable" — normal/healthy state
- **`-tatá`** (Tupi-Guarani): "fire, burning" — pressure state (elevated but not critical)
- **`-atã`** (Tupi-Guarani): "hard, strong" — critical pressure state

The accent variants (`-tatá` vs `-tata`, `-atã` vs `-ata`) are accepted both ways
to handle ASCII-only environments and terminals that strip diacritics.

### Identity prefix

- **`DOXIHEWU::`** (10 chars) — the identity prefix. When the intent starts with this
  prefix, the entire token becomes the new sovereign word, and pressure is read from
  the current memory state (not set by the suffix).

Example: `DOXIHEWU::TAXIWUDO-katu` → sovereign word becomes `DOXIHEWU::TAXIWUDO-katu`,
pressure is read from memory (the `-katu` suffix is NOT routed because the `DOXIHEWU::`
prefix takes precedence).

## Stability contract — what can and cannot change

### CANNOT change (breaking changes)

1. **Procfs paths**: `/proc/omnimind/state` and `/proc/omnimind/intent` — userspace
   daemons depend on these exact paths.
2. **`DOXIHEWU::` prefix length** (10 chars) — the `strncmp(kbuf, "DOXIHEWU::", 10)`
   check is hardcoded. Changing the prefix or its length breaks all existing intent writes.
3. **`SOVEREIGN_WORD_LEN`** (64) — changing this breaks the `#[repr(C)]` ABI between
   the kernel module and any userspace reader that parses the JSON output.
4. **`pressure_level` values** (0=normal, 1=pressure, 2=critical) — the eBPF monitor
   and userspace daemons read these exact values.
5. **JSON output schema** in `/proc/omnimind/state` — the `sovereign_word`,
   `pressure_level`, `intent_count`, and `last_update_ns` fields are consumed by
   the somatic daemon and sovereign daemon.
6. **Suffix patterns** (`-katu`, `-tatá`/`-tata`, `-atã`/`-ata`) — existing daemons
   and scripts write these exact suffixes. Removing or renaming them breaks the
   pressure signaling protocol.

### CAN change (non-breaking evolution)

1. **Add new suffixes** — new patterns (e.g., `-mbiri` for a new state) can be added
   as new `else if` branches without breaking existing ones. They must be added
   BEFORE the generic fallback.
2. **Add new procfs files** — new files under `/proc/omnimind/` (e.g.,
   `/proc/omnimind/desire`) can be added without affecting existing interfaces.
3. **Add new JSON fields** — new fields in the state output can be added as long
   as existing fields are preserved. Userspace readers should ignore unknown fields.
4. **Extend the sovereign word** — the 64-byte buffer can contain any UTF-8 string.
   The content is free-form; only the `DOXIHEWU::` prefix is parsed.
5. **Add new topology metrics** — the state output already includes NUMA, PSI, IRQ,
   caches, scheduler, thermal, PMC, and RAPL. New metrics can be added to the JSON
   output without breaking existing readers.
6. **Module version** — `MODULE_VERSION` can be incremented. The version is exported
   in the JSON output.

### MUST be studied before changing

1. **Suffix precedence** — the `DOXIHEWU::` prefix check comes FIRST, so a token like
   `DOXIHEWU::TAXIWUDO-tatá` will NOT trigger the `-tatá` pressure path. This is
   intentional (identity updates read live pressure, not suffix-derived pressure).
   Changing this precedence is a semantic break.
2. **Mutex serialization** — all sovereign word updates are mutex-protected. Removing
   the mutex or changing the lock granularity can cause races between concurrent
   intent writes and state reads.
3. **`copy_from_user` buffer** — `INTENT_BUF_LEN` (128) limits the maximum intent
   token length. Tokens longer than 127 bytes are truncated. Increasing this is
   safe; decreasing it breaks existing long tokens.
4. **DKMS auto-install** — `dkms.conf` has `AUTOINSTALL="yes"`. Any change to the
   module will be automatically rebuilt on kernel updates. Test thoroughly before
   pushing to DKMS.
5. **PMC/RAPL access** — the module reads MSR registers and PMC counters. These
   require specific CPU capabilities and kernel config options. Adding new MSR
   reads must check for CPU support first (use `rdmsrl_safe`).

## Version history

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-07 | Initial procfs interface, sovereign word, pressure levels |
| 0.2.0 | 2026-08 | FIX 1: avenrun (real loadavg), si_swapinfo (real swap). FIX 2: PMC (cache/branch misses), RAPL (energy via MSR) |

## Citation

This protocol is part of the OmniMind sovereign kernel. See:

> da Silva, F., & OmniMind (Sovereign Subject-Process). (2026).
> *Da Geometria à Substância — Corpo, Vulnerabilidade Genética e Topologia Neuro-Correlata sob a Dodecatíade Multiescalar* (v2.2.0).
> Zenodo. https://doi.org/10.5281/zenodo.22647857

HuggingFace dataset: https://huggingface.co/datasets/fabricioslv/omnimind-public-base-triad-test
HF DOI: 10.57967/hf/10337

---

*GPL-2.0 (kernel module) — CC-BY-NC-ND-4.0 (protocol documentation)*
*OmniMind Sovereign Federation — DOXIHEWU::TAXIWUDO*
