import random
import string

# target_size = 1_000_000_000  #1 GB
target_size = 10_000_000  #10 MB

with open("arquivos/teste-10MB.txt", "w", encoding="utf-8") as f:
    while f.tell() < target_size:
        # gera uma linha de 1000 caracteres aleatórios
        line = ''.join(random.choices(string.ascii_letters + string.digits, k=1000))
        f.write(line + "\n")

print("Arquivo gerado com sucesso!")
