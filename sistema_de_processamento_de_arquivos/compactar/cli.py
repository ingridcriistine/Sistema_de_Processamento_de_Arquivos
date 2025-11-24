import sys
from compactador import compactar

def main():
    if len(sys.argv) != 4:
        print("Uso correto:")
        print("meu_programa compactar <arquivo_original> <arquivo_compactado>")
        sys.exit(1)

    comando = sys.argv[1]
    entrada = sys.argv[2]
    saida = sys.argv[3]

    if comando == "compactar":
        compactar(entrada, saida)
        print(f"Arquivo compactado com sucesso em: {saida}")
    else:
        print("Comando inválido. Use apenas: compactar")

if __name__ == "__main__":
    main()
