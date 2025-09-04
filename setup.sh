#!/bin/bash
set -e  # se algum comando falhar, o script para

echo "Iniciando setup do projeto..."

# 1. Cria venv local se não existir
if [ ! -d ".venv" ]; then
    echo "Criando ambiente virtual (.venv)..."
    if command -v python3 &>/dev/null; then
        python3 -m venv .venv
    elif command -v python &>/dev/null; then
        python -m venv .venv
    else
        echo "Python não encontrado no PATH."
        exit 1
    fi
else
    echo "Ambiente virtual já existe, pulando criação."
fi

# 2. Ativa o venv
echo "Ativando ambiente virtual..."
# shellcheck disable=SC1091
source .venv/bin/activate

# 3. Instala dependências
if [ -f requirements.txt ]; then
    echo "Instalando dependências do requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "Nenhum requirements.txt encontrado, pulando instalação."
fi

echo "Setup concluído!"
