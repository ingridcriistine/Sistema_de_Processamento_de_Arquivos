import argparse
import os
from .compactar.compactador import compactar
from .buscar_simples.boyer_moore_simples import buscar_simples
from .descompactar.descompactar import descompactar
# from .buscar_compactado.compressed_search import buscar_compactado

def main():
    parser = argparse.ArgumentParser(prog="meu_programa")
    subparsers = parser.add_subparsers(dest="comando")
    
    # --- Compactar ---
    p_compactar = subparsers.add_parser("compactar", help="Compacta um arquivo usando Huffman")
    p_compactar.add_argument("arquivo_original")
    p_compactar.add_argument("arquivo_compactado")
    
    # --- Descompactar ---
    p_descompactar = subparsers.add_parser("descompactar", help="Descompacta um arquivo .huff")
    p_descompactar.add_argument("arquivo_compactado")
    p_descompactar.add_argument("arquivo_descompactado")

    # --- Buscar simples ---
    p_simples = subparsers.add_parser("buscar_simples", help="Busca substring em arquivo original")
    p_simples.add_argument("arquivo_original")
    p_simples.add_argument("substring")
    
    # --- Buscar compactado (se fizer depois) ---
    # p_comp = subparsers.add_parser("buscar_compactado", help="Busca em arquivos compactados")
    # p_comp.add_argument("arquivo_compactado")
    # p_comp.add_argument("substring")

    args = parser.parse_args()
    
    if args.comando == "compactar":
        pasta_comp = "arquivos/compactados" 
        saida = os.path.join(pasta_comp, args.arquivo_compactado)
        compactar(args.arquivo_original, saida)

    elif args.comando == "descompactar":
        pasta_desc = "arquivos/descompactados"
        saida = os.path.join(pasta_desc, args.arquivo_descompactado)
        descompactar(args.arquivo_compactado, saida)


    elif args.comando == "buscar_simples":
        buscar_simples(args.arquivo_original, args.substring)

    else:
        parser.print_help()
