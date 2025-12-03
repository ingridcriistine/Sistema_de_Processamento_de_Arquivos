import json

from sistema_de_processamento_de_arquivos.descompactar.descompactar import descompactar_bloco

def buscar_substring_compactado(arquivo_entrada, padrao_busca):
    print(f"\n=== BUSCANDO '{padrao_busca}' NO ARQUIVO COMPACTADO")

    tamanho_padrao = len(padrao_busca)
    resultados_globais = []

    with open(arquivo_entrada, "rb") as f_in:

        tamanho_tabela = int.from_bytes(f_in.read(4), "big")
        tabela_json = f_in.read(tamanho_tabela).decode("utf-8")
        tabela_codigos = json.loads(tabela_json)

        offset_indice = int.from_bytes(f_in.read(8), "big")
        f_in.seek(offset_indice)

        tamanho_indice = int.from_bytes(f_in.read(4), "big")
        lista_indices = json.loads(f_in.read(tamanho_indice).decode("utf-8"))

        ultimo_final = ""

        for bloco in lista_indices:
            inicio_original = bloco["orig_start"]
            fim_original    = bloco["orig_end"]
            pos_compactado  = bloco["comp_start"]
            tam_compactado  = bloco["comp_size"]
            bits_padding    = bloco["padding"]

            if fim_original < inicio_original:
                continue

            f_in.seek(pos_compactado)

            tam_real = int.from_bytes(f_in.read(4), "big")
            if tam_real != tam_compactado:
                raise ValueError("Erro no índice: tamanho diferente durante busca.")

            bloco_bytes = f_in.read(tam_compactado)

            texto_bloco = descompactar_bloco(tabela_codigos, bloco_bytes, bits_padding).replace("\n", "")
            ultimo_final = ultimo_final.replace("\n", "")

            janela_busca = ultimo_final + texto_bloco

            pos_local = janela_busca.find(padrao_busca)

            while pos_local != -1:
                if pos_local >= len(ultimo_final):
                    pos_relativo = pos_local - len(ultimo_final)
                    deslocamento_bytes = len(texto_bloco[:pos_relativo].encode("utf-8"))
                    pos_global = inicio_original + deslocamento_bytes
                else:
                    deslocamento_pre = inicio_original - len(ultimo_final.encode("utf-8"))
                    deslocamento_bytes = len(janela_busca[:pos_local].encode("utf-8"))
                    pos_global = deslocamento_pre + deslocamento_bytes

                resultados_globais.append(pos_global)

                pos_local = janela_busca.find(padrao_busca, pos_local + 1)

            # Atualiza resto para capturar fronteira com próximo bloco
            if tamanho_padrao > 1:
                ultimo_final = janela_busca[-(tamanho_padrao - 1):]
            else:
                ultimo_final = ""

    return resultados_globais
