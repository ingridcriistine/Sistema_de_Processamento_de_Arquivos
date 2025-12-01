import json

def buscar_substring_compactado(entrada, padrao):
    print(f"\n=== BUSCANDO '{padrao}' NO ARQUIVO COMPACTADO ===")

    m = len(padrao)

    resultados = []

    ultimo_final = ""   

    with open(entrada, "rb") as f_in:

        tam_tabela = int.from_bytes(f_in.read(4), "big")
        tabela_json = f_in.read(tam_tabela).decode("utf-8")
        codigos = json.loads(tabela_json)
        codigos_inv = {v: k for k, v in codigos.items()}

        while True:
            bloco_size_bytes = f_in.read(4)
            if not bloco_size_bytes:
                break

            bloco_size = int.from_bytes(bloco_size_bytes, "big")
            bloco_comp = f_in.read(bloco_size)

            indice_size = int.from_bytes(f_in.read(4), "big")
            indice_json = json.loads(f_in.read(indice_size).decode("utf-8"))

            start_global = indice_json["start_global"]
            end_global   = indice_json["end_global"]
            padding      = indice_json["padding"]

            bits = ""
            for byte in bloco_comp:
                bits += f"{byte:08b}"

            if padding:
                bits = bits[:-padding]

            texto = ""
            atual = ""
            for b in bits:
                atual += b
                if atual in codigos_inv:
                    texto += codigos_inv[atual]
                    atual = ""

           
            janela = ultimo_final + texto

       
            pos = janela.find(padrao)
            while pos != -1:
                pos_global = start_global - len(ultimo_final) + pos
                if start_global <= pos_global <= end_global:
                    resultados.append(pos_global)
                pos = janela.find(padrao, pos+1)
           
            ultimo_final = texto[-(m-1):] if m > 1 else ""

    return resultados
