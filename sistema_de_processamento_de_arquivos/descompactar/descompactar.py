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
    bits = "".join(f"{byte:08b}" for byte in compressed_bytes)
    if padding:
        bits = bits[:-padding]
    atual = ""
    out_chars = []
    for b in bits:
        atual += b
        if atual in codigos_inv:
            out_chars.append(codigos_inv[atual])
            atual = ""
    return "".join(out_chars).replace("\n", "")



def descompactar(entrada, saida):
    print("\n=== INICIANDO DESCOMPACTAÇÃO INDEXADA ===")
    with open(entrada, "rb") as f_in, open(saida, "w", encoding="utf-8") as f_out:
        tam_tabela = int.from_bytes(f_in.read(4), "big")
        tabela_json = f_in.read(tam_tabela).decode("utf-8")
        codigos = json.loads(tabela_json)

        index_offset = int.from_bytes(f_in.read(8), "big")
        f_in.seek(index_offset)

        index_size = int.from_bytes(f_in.read(4), "big")
        index_entries = json.loads(f_in.read(index_size).decode("utf-8"))

        for entry in index_entries:
            comp_start = entry["comp_start"]
            comp_size  = entry["comp_size"]
            padding    = entry["padding"]

            f_in.seek(comp_start)
            actual_comp_size = int.from_bytes(f_in.read(4), "big")
            if actual_comp_size != comp_size:
                raise ValueError("comp_size mismatch")
            bloco_comp = f_in.read(comp_size)
            texto = descompactar_bloco(codigos, bloco_comp, padding)
            f_out.write(texto)

    print("Descompactação concluída.")