# Sistema_de_Processamento_de_Arquivos
Projeto final da disciplina Estrutura de Dados II - UFPR

## Descrição
Breve explicação sobre o objetivo do projeto, contexto e motivação.

## Como executar
Passo a passo para rodar o projeto:
1. Pré-requisitos: possuir Python na versão 3.13.3 instalado.
2. Comandos para instalação.
3. Comando para executar o código principal.
- Etapa 1: `sistema_de_processamento_de_arquivos compactar <arquivo_original> <arquivo_compactado>`
- Etapa 2: `sistema_de_processamento_de_arquivos compactar arquivos/<arquivo_original> "<substring>"`

## Estrutura

```
├── arquivos/                                       # Arquivos de teste  
├── sistema_de_processamento_de_arquivos/           # Pasta com o código-fonte principal  
    ├── buscar_compactado/                          # Pasta com as funções da etapa 3  
    ├── buscar_simples/                             # Pasta com as funções da etapa 2  
        └── boyer_moore_simples.py                  # Funções gerais de busca de substring em arquivos grandes  
    ├── compactar/                                  # Pasta com as funções da etapa 1  
    ├── __main__.py                                 #   
    └── cli.py                                      #   
├── .gitignore                                      # Arquivo gitignore  
└── AI_USAGE_LOG.md                                 # Relatório do uso de IA generativa  
├── gerador_arquivos.py                             # Gera arquivos de texto para teste  
└── README.md                                       # Este documento    
```

## Etapas do Projeto

### Etapa 1 | Compressão de Arquivos Grandes 
- Implementar a funcionalidade de compressão de um arquivo de texto. O algoritmo deve processar o arquivo de entrada garantindo baixo uso de memória.
- Comando: `sistema_de_processamento_de_arquivos compactar <arquivo_original> <arquivo_compactado>`
- Algoritmo utilizado: Huffman.

### Etapa 2 | Busca de Substring em Arquivo Grande
- Objetivo: Implementar uma busca por substring em um arquivo de texto original (não comprimido) que pode ser maior que a memória RAM disponível.
- Comando: `sistema_de_processamento_de_arquivos compactar arquivos/<arquivo_original> "<substring>"`
- Saída: A lista de posições (offsets em bytes) onde a substring foi encontrada.
- Algoritmo utilizado: Boyer-Moore.

### Etapa 3 | Busca de Substring em Arquivo Comprimido
- Objetivo: Integrar e evoluir as etapas anteriores para permitir a busca por substring diretamente no arquivo gerado pela Etapa 1, sem descompressão total.

## Autores

- Ingrid Cristine Rocha
- Milena Calegari Dourado

## Referências

ETAPA 1
- []()

ETAPA 2
- [Boyer Moore Algorithm | Good Suffix heuristic](https://www.geeksforgeeks.org/dsa/boyer-moore-algorithm-good-suffix-heuristic/)
- [Boyer Moore Algorithm in Python](https://www.geeksforgeeks.org/dsa/boyer-moore-algorithm-in-python/)
- [Aula 13: Strings - Busca de Substrings](https://youtu.be/TuAJG9nZ-gY?si=5yomCnUxbuV1Dorj)
- [ADS1: Practical: Implementing Boyer-Moore](https://youtu.be/CT1lQN73UMs?si=SNuxzzx_WLX6Q_uo)
- [ADS1: Preprocessing](https://youtu.be/HGVQi5xX44M?si=l3nrk8MD1LyrnxzN)
- [ADS1: Boyer-Moore basics](https://youtu.be/4Xyhb72LCX4?si=8fisJb5VXY8qzbbv)

ETAPA 3
- []()
