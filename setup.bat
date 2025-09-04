@echo off
setlocal EnableExtensions DisableDelayedExpansion

echo Iniciando setup do projeto...

REM 1) Cria venv local se nao existir
if not exist ".venv" (
    echo Criando ambiente virtual ^(.venv^)...
    REM 
    py -3 -m venv .venv 2>nul || python -m venv .venv
) else (
    echo Ambiente virtual ja existe, pulando criacao.
)

REM 2) Ativa o venv
echo Ativando ambiente virtual...
call .venv\Scripts\activate.bat

REM 3) Instala dependencias
echo Instalando dependencias do requirements.txt...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Setup concluido!
pause
