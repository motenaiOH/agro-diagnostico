@echo off

:: Navegar até o diretório raiz do projeto
cd /d %~dp0\..

:: Criar ambiente virtual
python -m venv venv
call venv\Scripts\activate.bat

:: Atualizar pip
echo Atualizando pip...
pip install --upgrade pip

:: Instalar dependências
echo Instalando dependências...
pip install -r requirements.txt

:: Iniciar aplicação
echo Iniciando aplicação...
cd app
python main.py