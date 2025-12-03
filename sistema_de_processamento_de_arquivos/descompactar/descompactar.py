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

def descompactar_bloco(tabela_codigos, bloco_comprimido, bits_de_padding):
    tabela_invertida = {codigo: char for char, codigo in tabela_codigos.items()}

    bits = "".join(f"{byte:08b}" for byte in bloco_comprimido)

    if bits_de_padding:
        bits = bits[:-bits_de_padding]

    buffer_bits = ""
    resultado_chars = []

    for bit in bits:
        buffer_bits += bit
        if buffer_bits in tabela_invertida:
            resultado_chars.append(tabela_invertida[buffer_bits])
            buffer_bits = ""

    return "".join(resultado_chars)


def descompactar(arquivo_entrada, arquivo_saida):
    print("\n=== INICIANDO DESCOMPACTAÇÃO INDEXADA ===")

    with open(arquivo_entrada, "rb") as f_in, open(arquivo_saida, "w", encoding="utf-8") as f_out:

        tamanho_tabela = int.from_bytes(f_in.read(4), "big")
        tabela_json = f_in.read(tamanho_tabela).decode("utf-8")
        tabela_codigos = json.loads(tabela_json)

        offset_indice = int.from_bytes(f_in.read(8), "big")
        f_in.seek(offset_indice)

        tamanho_indice = int.from_bytes(f_in.read(4), "big")
        lista_indices = json.loads(f_in.read(tamanho_indice).decode("utf-8"))

        for info_bloco in lista_indices:
            pos_compactado = info_bloco["comp_start"]
            tam_compactado = info_bloco["comp_size"]
            bits_padding   = info_bloco["padding"]

            # Vai até o bloco
            f_in.seek(pos_compactado)

            # Lê o tamanho declarado e confere
            tam_real_lido = int.from_bytes(f_in.read(4), "big")
            if tam_real_lido != tam_compactado:
                raise ValueError("Erro: tam_compactado diferente do armazenado.")

            bytes_bloco = f_in.read(tam_compactado)

            texto = descompactar_bloco(tabela_codigos, bytes_bloco, bits_padding)

            f_out.write(texto)

    print("Descompactação concluída.")
