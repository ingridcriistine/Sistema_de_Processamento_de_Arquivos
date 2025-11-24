from .lendo_arquivo import PrimeiraLeituraStreaming
from .lendo_arquivo import SegundaLeituraStreaming
from .arvore import construir_arvore_huffman
from .codigos import gerar_codigos

def compactar(entrada, saida):
    leitor1 = PrimeiraLeituraStreaming(entrada)
    leitor1.processar()

    root = construir_arvore_huffman(leitor1.freq)
    codigos = gerar_codigos(root)

    print("Códigos de Huffman gerados:")
    for char, code in codigos.items():
        if char == "\n":
            print("\\n:", code)
        elif char == " ":
            print("' ':", code)
        else:
            print(f"{char}: {code}")


    leitor2 = SegundaLeituraStreaming(entrada, codigos)
    leitor2.comprimir_para_binario(saida)

    print("Arquivo compactado com sucesso!")

