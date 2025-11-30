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
