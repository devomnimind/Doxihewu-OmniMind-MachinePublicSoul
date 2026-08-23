#!/usr/bin/env bash
# ======================================================================
# sync_public_remotes.sh — Conciliação GitLab ↔ GitHub do Machine Public Soul
# ======================================================================
# Mantém os dois remotes (GitLab = fonte canônica; GitHub = espelho) alinhados.
# Puxa o mais novo de qualquer remote, faz merge no local, e faz push para
# AMBOS. Assim, publicar no GitLab primeiro não deixa o GitHub para trás (e
# vice-versa).
#
# Uso:
#   ./sync_public_remotes.sh              # sync (pull ambos + push ambos)
#   ./sync_public_remotes.sh --dry-run    # mostra o que faria sem alterar
#
# Nota (2026-08-19): bases de evidência (.sqlite) NÃO são versionadas no
# git — vivem no release/Zenodo (links no README). Os PDFs dos artigos atuais
# são versionados em papers/, sem Git LFS.
# ======================================================================
set -euo pipefail

REPO="/home/fahbrain/projects/omnimind-public-pulse"
GITLAB="origin"     # https://gitlab.com/zephyrix/Doxihewu-OmniMind-MachinePublicSoul
GITHUB="github"     # https://github.com/devomnimind/Doxihewu-OmniMind-MachinePublicSoul
BRANCH="main"

DRY=""
[ "${1:-}" = "--dry-run" ] && DRY="--dry-run"

do_git() {
    if [ -n "$DRY" ]; then
        echo "  [dry-run] git $*"
    else
        echo "  git $*"
        git "$@"
    fi
}

cd "$REPO"

echo "=== HEAD atual ==="
echo "local : $(git rev-parse --short HEAD)"
echo "GitLab: $(git ls-remote "$GITLAB" "refs/heads/$BRANCH" | cut -c1-7 || echo '?')"
echo "GitHub: $(git ls-remote "$GITHUB" "refs/heads/$BRANCH" | cut -c1-7 || echo '?')"

echo
echo "=== Pull de ambos (sem fast-forward, para não perder divergência) ==="
do_git pull "$GITLAB" "$BRANCH" --no-ff --no-edit || true
do_git pull "$GITHUB" "$BRANCH" --no-ff --no-edit || true

# Coaliza para frente também no local (caso haja commit local não publicado)
echo
echo "=== Push para AMBOS ==="
do_git push "$GITLAB" "$BRANCH"
do_git push "$GITHUB" "$BRANCH"

echo
echo "=== Resultado ==="
echo "local : $(git rev-parse --short HEAD)"
echo "GitLab: $(git ls-remote "$GITLAB" "refs/heads/$BRANCH" | cut -c1-7)"
echo "GitHub: $(git ls-remote "$GITHUB" "refs/heads/$BRANCH" | cut -c1-7)"

echo
if [ -n "$DRY" ]; then
    echo "DRY-RUN — nada foi alterado."
else
    echo "OK — GitLab e GitHub alinhados."
fi
