from .lendo_arquivo import PrimeiraLeituraStreaming
from .lendo_arquivo import SegundaLeituraStreaming
from .arvore import construir_arvore_huffman
from .codigos import gerar_codigos


def compactar(entrada, saida):
    print("\n=== INICIANDO COMPACTAÇÃO ===")

    leitor1 = PrimeiraLeituraStreaming(entrada)
    leitor1.processar()

    print("Frequências obtidas:")
    for ch, freq in leitor1.freq.items():
        exibe = repr(ch)
        print(f"  {exibe}: {freq}")

    root = construir_arvore_huffman(leitor1.freq)

    codigos = gerar_codigos(root)

    print("\nCódigos de Huffman gerados:")
    for char, code in codigos.items():
        if char == "\n":
            print("\\n:", code)
        elif char == " ":
            print("' ':", code)
        else:
            print(f"{char}: {code}")

    leitor2 = SegundaLeituraStreaming(entrada, codigos)
    leitor2.comprimir_para_blocos(saida)

    print("\nArquivo compactado com sucesso!")
    print(f"Saída: {saida}")
