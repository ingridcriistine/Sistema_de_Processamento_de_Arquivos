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
        self.codigos = codigos  # map char -> bitstring
        self.block_size = block_size

    def _comprimir_bloco_para_bytes(self, texto_bloco):
        buffer_bits = ""
        out = bytearray()
        for ch in texto_bloco:
            buffer_bits += self.codigos[ch]
            while len(buffer_bits) >= 8:
                byte = int(buffer_bits[:8], 2)
                out.append(byte)
                buffer_bits = buffer_bits[8:]
        padding = 0
        if buffer_bits:
            padding = 8 - len(buffer_bits)
            buffer_bits = buffer_bits.ljust(8, "0")
            out.append(int(buffer_bits, 2))
        return bytes(out), padding

    def comprimir_para_blocos(self, saida):
        tabela_json = json.dumps(self.codigos).encode("utf-8")
        tam_tabela = len(tabela_json)

        index_entries = []

        current_orig_pos_bytes = 0

        with open(self.caminho, "r", encoding="utf-8") as f_in, open(saida, "wb") as f_out:
            f_out.write(tam_tabela.to_bytes(4, "big"))
            f_out.write(tabela_json)

            index_offset_pos = f_out.tell()
            f_out.write((0).to_bytes(8, "big"))

            while True:
                bloco = f_in.read(self.block_size) 
                if not bloco:
                    break

                bloco_comp_bytes, padding = self._comprimir_bloco_para_bytes(bloco)

                comp_start = f_out.tell()

                comp_size = len(bloco_comp_bytes)

                f_out.write(comp_size.to_bytes(4, "big"))
                if comp_size:
                    f_out.write(bloco_comp_bytes)

                bloco_original_bytes = bloco.encode("utf-8")
                orig_start = current_orig_pos_bytes
                orig_end = current_orig_pos_bytes + len(bloco_original_bytes) - 1 if len(bloco_original_bytes) > 0 else current_orig_pos_bytes - 1

                entry = {
                    "orig_start": orig_start,
                    "orig_end": orig_end,
                    "comp_start": comp_start,
                    "comp_size": comp_size,
                    "padding": padding
                }
                index_entries.append(entry)

                current_orig_pos_bytes += len(bloco_original_bytes)

            index_start = f_out.tell()
            index_json = json.dumps(index_entries).encode("utf-8")
            index_size = len(index_json)
            f_out.write(index_size.to_bytes(4, "big"))
            f_out.write(index_json)

            f_out.seek(index_offset_pos)
            f_out.write(index_start.to_bytes(8, "big"))
