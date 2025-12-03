import json

class PrimeiraLeituraStreaming:
    def __init__(self, caminho, block_size=4096):
        self.caminho = caminho
        self.block_size = block_size
        self.freq = {}

    def processar(self):
        with open(self.caminho, "r", encoding="utf-8") as f:
            while True:
                chunk = f.read(self.block_size)
                if not chunk:
                    break

                for ch in chunk:
                    if ch not in self.freq:
                        self.freq[ch] = 0
                    self.freq[ch] += 1

# class SegundaLeituraStreaming:
#     def __init__(self, caminho, codigos, block_size=4096):
#         self.caminho = caminho
#         self.codigos = codigos
#         self.block_size = block_size

#     def comprimir_para_binario(self, saida):
#         buffer_bits = ""

#         tabela_json = json.dumps(self.codigos).encode("utf-8")
#         tamanho = len(tabela_json)

#         with open(saida, "wb") as f_out:

#             f_out.write(tamanho.to_bytes(4, "big"))

#             f_out.write(tabela_json)

#             f_out.write(b"\x00")
#             pos_padding = f_out.tell() - 1  

#             with open(self.caminho, "r", encoding="utf-8") as f_in:
#                 while True:
#                     chunk = f_in.read(self.block_size)
#                     if not chunk:
#                         break

#                     for ch in chunk:
#                         buffer_bits += self.codigos[ch]

#                         while len(buffer_bits) >= 8:
#                             byte = int(buffer_bits[:8], 2)
#                             buffer_bits = buffer_bits[8:]
#                             f_out.write(byte.to_bytes(1, "big"))

#             padding = 0
#             if buffer_bits:
#                 padding = 8 - len(buffer_bits)
#                 buffer_bits = buffer_bits.ljust(8, "0")
#                 f_out.write(int(buffer_bits, 2).to_bytes(1, "big"))

#             f_out.seek(pos_padding)
#             f_out.write(bytes([padding]))

class SegundaLeituraStreaming:
    def __init__(self, caminho_arquivo, tabela_codigos, tamanho_bloco=4096):
        self.caminho_arquivo = caminho_arquivo
        self.codigos = tabela_codigos      # mapa: caractere → sequência de bits
        self.tamanho_bloco = tamanho_bloco

    def _comprimir_bloco(self, bloco_texto):
        bits_acumulados = ""
        bytes_compactados = bytearray()

        for caractere in bloco_texto:
            bits_acumulados += self.codigos[caractere]

            # Cada vez que tivermos 8 bits, convertemos para byte
            while len(bits_acumulados) >= 8:
                byte = int(bits_acumulados[:8], 2)
                bytes_compactados.append(byte)
                bits_acumulados = bits_acumulados[8:]

        padding = 0
        if bits_acumulados:
            padding = 8 - len(bits_acumulados)
            bits_acumulados = bits_acumulados.ljust(8, "0")
            bytes_compactados.append(int(bits_acumulados, 2))

        return bytes(bytes_compactados), padding

    # Compacta o arquivo inteiro em blocos + cria índice
    def comprimir_para_blocos(self, caminho_saida):

        tabela_json = json.dumps(self.codigos).encode("utf-8")
        tamanho_tabela = len(tabela_json)

        indice = []                     
        posicao_atual_original = 0    

        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo_in, \
             open(caminho_saida, "wb") as arquivo_out:

            arquivo_out.write(tamanho_tabela.to_bytes(4, "big"))
            arquivo_out.write(tabela_json)

            # Reservamos 8 bytes para escrever + tarde a posição do índice
            pos_offset_indice = arquivo_out.tell()
            arquivo_out.write((0).to_bytes(8, "big"))

            while True:
                bloco = arquivo_in.read(self.tamanho_bloco)
                if not bloco:
                    break

                bloco_compactado, padding = self._comprimir_bloco(bloco)
                tamanho_compactado = len(bloco_compactado)

                inicio_compactado = arquivo_out.tell()

                arquivo_out.write(tamanho_compactado.to_bytes(4, "big"))
                arquivo_out.write(bloco_compactado)

                # Calcula tamanho real do bloco original em bytes
                bloco_original_bytes = bloco.encode("utf-8")
                inicio_original = posicao_atual_original
                fim_original = posicao_atual_original + len(bloco_original_bytes) - 1

                indice.append({
                    "orig_start": inicio_original,
                    "orig_end": fim_original,
                    "comp_start": inicio_compactado,
                    "comp_size": tamanho_compactado,
                    "padding": padding
                })

                posicao_atual_original += len(bloco_original_bytes)

            # Escrever o índice no final do arquivo
            inicio_indice = arquivo_out.tell()
            indice_json = json.dumps(indice).encode("utf-8")
            tamanho_indice = len(indice_json)

            arquivo_out.write(tamanho_indice.to_bytes(4, "big"))
            arquivo_out.write(indice_json)

            # Atualiza no início a posição onde o índice começa
            arquivo_out.seek(pos_offset_indice)
            arquivo_out.write(inicio_indice.to_bytes(8, "big"))
