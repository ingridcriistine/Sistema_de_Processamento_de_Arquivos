import json

def buscar_substring(txt, pat):
    m = len(pat)
    res = []
    for i in range(len(txt) - m + 1):
        if txt[i:i+m] == pat:
            res.append(i)
    return res


def buscar_compactado(arq, substring):
    resultados = []
    m = len(substring)

    with open(arq, "rb") as f:

        tam_idx = int.from_bytes(f.read(4), "big")
        idx_json = f.read(tam_idx).decode("utf-8")
        indice = json.loads(idx_json)

        padding_global = f.read(1)[0]

        base_offset = 4 + tam_idx + 1

        sufixo_anterior = ""

        for bloco in indice:

            comp_offset  = bloco["comp_offset"]
            comp_size    = bloco["comp_size"]
            orig_offset  = bloco["orig_offset"]
            codigos      = bloco["codigos"]
            padding      = bloco["padding"]   

            f.seek(base_offset + comp_offset)
            compressed = f.read(comp_size)

            dados = descompactar_bloco(codigos, compressed, padding)

            for pos in buscar_substring(dados, substring):
                resultados.append(orig_offset + pos)

            if len(sufixo_anterior) > 0:

                janela = sufixo_anterior + dados
                posicoes = buscar_substring(janela, substring)

                for p in posicoes:
                    if p < len(sufixo_anterior):
                        offset_real = orig_offset - len(sufixo_anterior) + p
                        resultados.append(offset_real)

            if len(dados) >= m-1:
                sufixo_anterior = dados[-(m-1):]
            else:
                sufixo_anterior = dados

    return resultados
