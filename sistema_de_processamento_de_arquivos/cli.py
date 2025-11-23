import argparse
from .compactar.compactador import compactar
from .buscar_simples.boyer_moore_simples import buscar_simples
from .buscar_simples.boyer_moore_simples import b
# from .buscar_compactado.compressed_search import buscar_compactado

def main():
    parser = argparse.ArgumentParser(prog="meu_programa")
    subparsers = parser.add_subparsers(dest="comando")
    
    p_compactar = subparsers.add_parser("compactar", help="Compacta um arquivo")
    p_compactar.add_argument("arquivo_original")
    p_compactar.add_argument("arquivo_compactado")
    
    p_simples = subparsers.add_parser("buscar_simples", help="Busca substring em arquivo original")
    p_simples.add_argument("arquivo_original")
    p_simples.add_argument("substring")
    
    p_comp = subparsers.add_parser("buscar_compactado", help="Busca em arquivos compactados")
    p_comp.add_argument("arquivo_compactado")
    p_comp.add_argument("substring")

    args = parser.parse_args()
    
    if args.comando == "compactar":
        compactar(args.arquivo_original, args.arquivo_compactado)

    elif args.comando == "buscar_simples":
        buscar_simples(args.arquivo_original, args.substring)

    # elif args.comando == "buscar_compactado":
    #     buscar_compactado(args.arquivo_compactado, args.substring)

    else:
        parser.print_help()

    if __name__ == "__main__":
        main()