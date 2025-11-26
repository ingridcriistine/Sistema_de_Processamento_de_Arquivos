import json

def descompactar(entrada, saida):
    print("\n=== INICIANDO DESCOMPACTAÇÃO ===")

    with open(entrada, "rb") as f_in, open(saida, "w", encoding="utf-8") as f_out:

        tam_tab = int.from_bytes(f_in.read(4), "big")
        tabela_json = f_in.read(tam_tab).decode("utf-8")
        codigos = json.loads(tabela_json)

        codigos_inv = {v: k for k, v in codigos.items()}

        padding = f_in.read(1)[0]

        bits = ""
        while True:
            chunk = f_in.read(4096)
            if not chunk:
                break
            for byte in chunk:
                bits += f"{byte:08b}"

        if padding:
            bits = bits[:-padding]

        atual = ""
        for b in bits:
            atual += b
            if atual in codigos_inv:
                f_out.write(codigos_inv[atual])
                atual = ""
