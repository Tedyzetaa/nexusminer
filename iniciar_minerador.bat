@echo off
chcp 65001 > nul
title Nexus Auto-Miner - Start
color 0B

echo 🚀 Inicializando Ambiente Miniconda [r2]...
cd /d "c:\nexus_miner"

REM Ativando o ambiente conda do Teddy
call C:\Users\Teddy\miniconda3\Scripts\activate.bat C:\Users\Teddy\miniconda3 && call conda activate r2 && (
    echo ⛏️ Iniciando Painel do Minerador...
    streamlit run app.py
)

if errorlevel 1 (
    echo ⚠️ Erro na inicialização. Verifique se o ambiente 'r2' existe e se o caminho esta correto.
    pause
)