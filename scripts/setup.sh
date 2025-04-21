#!/bin/bash

echo "🚀 Iniciando instalação do ambiente..."

# Navega até o diretório raiz do projeto
cd "$(dirname "$0")/.."

# Cria e ativa ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Atualiza pip
echo "📦 Atualizando pip..."
pip install --upgrade pip

# Instala dependências
echo "📦 Instalando dependências do requirements.txt..."
pip install -r requirements.txt

# Executa a aplicação
echo "✅ Instalação concluída! Iniciando aplicação..."
cd app
python main.py
