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

class SegundaLeituraStreaming:
    def __init__(self, caminho, codigos, block_size=4096):
        self.caminho = caminho
        self.codigos = codigos
        self.block_size = block_size

    def comprimir_para_binario(self, saida):
        buffer_bits = ""

        with open(self.caminho, "r", encoding="utf-8") as f_in, \
             open(saida, "wb") as f_out:

            while True:
                chunk = f_in.read(self.block_size)
                if not chunk:
                    break

                for ch in chunk:
                    buffer_bits += self.codigos[ch]

                    while len(buffer_bits) >= 8:
                        byte = buffer_bits[:8]
                        buffer_bits = buffer_bits[8:]
                        f_out.write(int(byte, 2).to_bytes(1, byteorder="big"))

            # padding final
            if buffer_bits:
                buffer_bits = buffer_bits.ljust(8, "0")
                f_out.write(int(buffer_bits, 2).to_bytes(1, byteorder="big"))


