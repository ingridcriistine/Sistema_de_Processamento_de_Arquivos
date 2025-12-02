import json

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
    return "".join(out_chars)


def buscar_substring_compactado(entrada, padrao):
    print(f"\n=== BUSCANDO '{padrao}' NO ARQUIVO COMPACTADO (INDEXADO) ===")
    m_chars = len(padrao) 
    resultados = []

    with open(entrada, "rb") as f_in:
        tam_tabela = int.from_bytes(f_in.read(4), "big")
        tabela_json = f_in.read(tam_tabela).decode("utf-8")
        codigos = json.loads(tabela_json)

        index_offset = int.from_bytes(f_in.read(8), "big")
        f_in.seek(index_offset)
        index_size = int.from_bytes(f_in.read(4), "big")
        index_entries = json.loads(f_in.read(index_size).decode("utf-8"))

        ultimo_final = "" 

        for entry in index_entries:
            orig_start = entry["orig_start"]  
            orig_end   = entry["orig_end"]
            comp_start = entry["comp_start"]
            comp_size  = entry["comp_size"]
            padding    = entry["padding"]

            if orig_end < orig_start:
                continue

            f_in.seek(comp_start)
            actual_comp_size = int.from_bytes(f_in.read(4), "big")
            if actual_comp_size != comp_size:
                raise ValueError("comp_size mismatch during search")
            bloco_comp = f_in.read(comp_size)

            texto = descompactar_bloco(codigos, bloco_comp, padding).replace("\n", "")
            ultimo_final = ultimo_final.replace("\n", "")
            janela = (ultimo_final + texto)


            pos = janela.find(padrao)
            while pos != -1:
               
                if pos >= len(ultimo_final):
                    dentro = pos - len(ultimo_final)
                    byte_offset = len(texto[:dentro].encode("utf-8"))
                    pos_global = orig_start + byte_offset
                else:
                    ajuste_prev = orig_start - len(ultimo_final.encode("utf-8"))
                    byte_offset = len(janela[:pos].encode("utf-8"))
                    pos_global = ajuste_prev + byte_offset

                resultados.append(pos_global)
                                
                pos = janela.find(padrao, pos + 1)

            if m_chars > 1:
                ultimo_final = (ultimo_final + texto)[- (m_chars - 1):] if (m_chars - 1) > 0 else ""
            else:
                ultimo_final = ""

    return resultados
