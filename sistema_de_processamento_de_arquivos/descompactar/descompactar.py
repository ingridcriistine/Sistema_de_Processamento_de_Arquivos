import json

# def descompactar(entrada, saida):
#     print("\n=== INICIANDO DESCOMPACTAÇÃO ===")

#     with open(entrada, "rb") as f_in, open(saida, "w", encoding="utf-8") as f_out:

#         tam_tab = int.from_bytes(f_in.read(4), "big")
#         tabela_json = f_in.read(tam_tab).decode("utf-8")
#         codigos = json.loads(tabela_json)

#         codigos_inv = {v: k for k, v in codigos.items()}

#         padding = f_in.read(1)[0]

#         bits = ""
#         while True:
#             chunk = f_in.read(4096)
#             if not chunk:
#                 break
#             for byte in chunk:
#                 bits += f"{byte:08b}"

#         if padding:
#             bits = bits[:-padding]

#         atual = ""
#         for b in bits:
#             atual += b
#             if atual in codigos_inv:
#                 f_out.write(codigos_inv[atual])
#                 atual = ""


def descompactar_bloco(codigos, compressed_bytes, padding):
    codigos_inv = {v: k for k, v in codigos.items()}

    bits = ""
    for byte in compressed_bytes:
        bits += f"{byte:08b}"

    if padding:
        bits = bits[:-padding]

    atual = ""
    resultado = []
    for b in bits:
        atual += b
        if atual in codigos_inv:
            resultado.append(codigos_inv[atual])
            atual = ""
    return "".join(resultado)

def descompactar(entrada, saida):
    print("\n=== INICIANDO DESCOMPACTAÇÃO POR BLOCOS ===")

    with open(entrada, "rb") as f_in, open(saida, "w", encoding="utf-8") as f_out:

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
            padding = indice_json["padding"]

            bits = ""
            for byte in bloco_comp:
                bits += f"{byte:08b}"

            if padding:
                bits = bits[:-padding]

            atual = ""
            for b in bits:
                atual += b
                if atual in codigos_inv:
                    f_out.write(codigos_inv[atual])
                    atual = ""

