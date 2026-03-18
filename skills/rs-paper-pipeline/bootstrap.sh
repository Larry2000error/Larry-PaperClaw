#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_BIN="${PYTHON:-python3}"
VENV_DIR="${ROOT_DIR}/.venv"

echo "[1/5] project root: ${ROOT_DIR}"

if [ ! -d "${VENV_DIR}" ]; then
  echo "[2/5] creating virtualenv: ${VENV_DIR}"
  "${PYTHON_BIN}" -m venv "${VENV_DIR}"
else
  echo "[2/5] virtualenv exists: ${VENV_DIR}"
fi

echo "[3/5] installing python dependencies"
"${VENV_DIR}/bin/python" -m pip install --upgrade pip
"${VENV_DIR}/bin/python" -m pip install -r "${ROOT_DIR}/requirements.txt"

if [ ! -f "${ROOT_DIR}/.env" ]; then
  echo "[4/5] creating .env from .env.example"
  cp "${ROOT_DIR}/.env.example" "${ROOT_DIR}/.env"
  echo "      fill in GITHUB_TOKEN and BAILIAN_API_KEY before running the pipeline"
else
  echo "[4/5] .env already exists"
fi

mkdir -p "${ROOT_DIR}/memory" "${ROOT_DIR}/logs" "${ROOT_DIR}/papers/figures"
echo "[5/5] running doctor"
"${VENV_DIR}/bin/python" "${ROOT_DIR}/scripts/cli.py" doctor || true

echo
echo "Bootstrap complete."
echo "Activate with: source .venv/bin/activate"
