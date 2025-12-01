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
    def __init__(self, caminho, codigos, block_size=4096):
        self.caminho = caminho
        self.codigos = codigos
        self.block_size = block_size

    def comprimir_para_blocos(self, saida):

        tabela_json = json.dumps(self.codigos).encode("utf-8")
        tamanho_tabela = len(tabela_json)

        with open(saida, "wb") as f_out:

            f_out.write(tamanho_tabela.to_bytes(4, "big"))
            f_out.write(tabela_json)
            
            with open(self.caminho, "r", encoding="utf-8") as f_in:

                global_pos = 0  
                while True:
                    bloco = f_in.read(self.block_size)
                    if not bloco:
                        break

                    buffer_bits = ""
                    bloco_bytes = bytearray()

                    for ch in bloco:
                        buffer_bits += self.codigos[ch]

                        while len(buffer_bits) >= 8:
                            byte = int(buffer_bits[:8], 2)
                            bloco_bytes.append(byte)
                            buffer_bits = buffer_bits[8:]

                    padding = 0
                    if buffer_bits:
                        padding = 8 - len(buffer_bits)
                        buffer_bits = buffer_bits.ljust(8, "0")
                        bloco_bytes.append(int(buffer_bits, 2))

                    bloco_size = len(bloco_bytes)

                    f_out.write(bloco_size.to_bytes(4, "big"))

                    f_out.write(bytes(bloco_bytes))

                    indice = {
                        "start_global": global_pos,
                        "end_global": global_pos + len(bloco) - 1,
                        "padding": padding
                    }

                    indice_json = json.dumps(indice).encode("utf-8")
                    indice_size = len(indice_json)

                    f_out.write(indice_size.to_bytes(4, "big"))

                    f_out.write(indice_json)

                    global_pos += len(bloco)