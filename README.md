# Projeto-final-desafio-DIO




O que faz: gera um arquivo keystrokes_simulated.txt baseado em um input_sim.txt (textos que você cria), adiciona timestamps e mostra como um keylogger formataria logs — não captura eventos do sistema.

# scripts/simulate_keylogger.py
"""
Simulação de keylogger para fins educacionais.
NÃO captura teclado do usuário. Apenas lê um arquivo de entrada simulado e grava um log.
"""

import os
import time
from datetime import datetime

BASE = os.path.join(os.path.dirname(__file__), '..', 'lab_files')
INPUT_FILE = os.path.join(BASE, 'input_sim.txt')
OUTPUT_FILE = os.path.join(BASE, 'keystrokes_simulated.txt')

# Se input_sim.txt não existir, cria um exemplo
if not os.path.exists(INPUT_FILE):
    with open(INPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("usuario_digitou_hello\nusuario_digitou_senha123\nusuario_digitou_enter\n")

with open(INPUT_FILE, 'r', encoding='utf-8') as fin, open(OUTPUT_FILE, 'w', encoding='utf-8') as fout:
    for line in fin:
        kt = line.strip()
        timestamp = datetime.utcnow().isoformat() + 'Z'
        fout.write(f"{timestamp} - {kt}\n")
        # simula intervalo entre teclas
        time.sleep(0.1)

print(f"Log simulado escrito em: {OUTPUT_FILE}")






--------
O que faz: gera um arquivo keystrokes_simulated.txt baseado em um input_sim.txt (textos que você cria), 
adiciona timestamps e mostra como um keylogger formataria logs — não captura eventos do sistema.
