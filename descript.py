#Chave de recuperação não encontrada

def decrypt_all():
    if not os.path.isfile(KEY_PATH):
        print("Chave de recuperação não encontrada em lab_files/. Não é possível descriptografar.")
        return
    key = load_key()
    f = Fernet(key)
    for root, _, files in os.walk(BASE):
        for file in files:
            if not file.endswith(EXT_MARK):
                continue
            path = os.path.join(root, file)
            with open(path, 'rb') as fh:
                enc = fh.read()
            try:
                dec = f.decrypt(enc)
            except Exception as e:
                print(f"Falha ao descriptografar {path}: {e}")
                continue
            orig_path = path[:-len(EXT_MARK)]
            with open(orig_path, 'wb') as fh:
                fh.write(dec)
            os.remove(path)
            print(f"Descriptografado: {orig_path}")
    print("Descriptografia concluída.")

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ('encrypt', 'decrypt'):
        print("Uso: python safe_ransom_sim.py [encrypt|decrypt]")
        sys.exit(1)
    action = sys.argv[1]
    if action == 'encrypt':
        confirm = input("ATENÇÃO: isto irá criptografar apenas os arquivos em lab_files/. Continuar? (yes/no) ")
        if confirm.lower() == 'yes':
            encrypt_all()
        else:
            print("Operação cancelada.")
    else:
        confirm = input("Irá tentar DESCRIPTIOGRAFAR arquivos em lab_files/ usando key_recovery.key. Continuar? (yes/no) ")
        if confirm.lower() == 'yes':
            decrypt_all()
        else:
            print("Operação cancelada.")
