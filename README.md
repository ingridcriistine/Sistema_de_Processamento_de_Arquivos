# Sistema_de_Processamento_de_Arquivos
Projeto final da disciplina Estrutura de Dados II - UFPR

## Descrição
- Objetivo geral: Projetar e implementar uma ferramenta de linha de comando (CLI) para compressão e busca de substrings em arquivos de texto, com foco no processamento de dados que excedem a memória RAM disponível. O projeto visa aplicar conceitos de algoritmos, manipulação de arquivos em baixo nível e gerenciamento de memória.
- Descrição Geral: O projeto visa o desenvolvimento de uma aplicação modular que será construída em três etapas progressivas. A aplicação final deverá ser capaz de compactar um arquivo de texto grande e, posteriormente, realizar buscas por substrings diretamente no arquivo compactado, de forma eficiente e sem a necessidade de descompressão total.

## Como executar
Passo a passo para rodar o projeto:
1. Pré-requisitos: possuir Python na versão 3.13.3 instalado.
2.  Comando para executar o código principal.
- Etapa 1: `sistema_de_processamento_de_arquivos compactar arquivos/<arquivo_original> <arquivo_compactado>`
- Etapa 1: `sistema_de_processamento_de_arquivos descompactar arquivos/compactados/<arquivo_compactado> <arquivo_descompactado>`
- Etapa 2: `sistema_de_processamento_de_arquivos buscar_simples arquivos/<arquivo_original> "<substring>"`
- Etapa 3: `sistema_de_processamento_de_arquivos buscar_compactado arquivos/<arquivo_compactado> "<substring>"`

## Estrutura

```
├── arquivos/                                       # Arquivos de teste  
├── sistema_de_processamento_de_arquivos/           # Pasta com o código-fonte principal  
    ├── buscar_compactado/                          # Pasta com as funções da etapa 3
        └── boyer_moore_compactado.py               # Funções gerais de busca de substring em arquivos compactados
    ├── buscar_simples/                             # Pasta com as funções da etapa 2  
        └── boyer_moore_simples.py                  # Funções gerais de busca de substring em arquivos grandes  
    ├── compactar/                                  # Pasta com as funções da etapa 1 - compactar
        ├── arvore.py                               #   
        ├── codigos.py                              #   
        ├── compactador.py                          # Função geral de compactação de arquivos
        ├── fila_prioridade.py                      #   
        ├── lendo_arquivo.py                        #   
        └── node.py                                 #
    ├── descompactar/                               # Pasta com as funções da etapa 1 - descompactar
        └── descompactar.py                         # Função geral de descompactação de arquivos
    ├── __main__.py                                 #   
    └── cli.py                                      # Arquivo principal do programa que ser executado no terminal
├── .gitignore                                      # Arquivo gitignore  
├── AI_USAGE_LOG.md                                 # Relatório do uso de IA generativa  
├── gerador_arquivos.py                             # Gera arquivos de texto para teste  
└── README.md                                       # Este documento    
```

## Etapas do Projeto

### Etapa 1 | Compressão de Arquivos Grandes 
- Objetivo: Implementar a funcionalidade de compressão de um arquivo de texto. O algoritmo deve processar o arquivo de entrada garantindo baixo uso de memória.
- Comandos: 
    `sistema_de_processamento_de_arquivos compactar <arquivo_original> <arquivo_compactado>`
    `sistema_de_processamento_de_arquivos descompactar arquivos/compactados/<arquivo_compactado> <arquivo_descompactado>`
- Algoritmo utilizado: Huffman.
- Sobre a implementação: 

### Etapa 2 | Busca de Substring em Arquivo Grande
- Objetivo: Implementar uma busca por substring em um arquivo de texto original (não comprimido) que pode ser maior que a memória RAM disponível.
- Comando: `sistema_de_processamento_de_arquivos buscar_simples arquivos/<arquivo_original> "<substring>"`
- Saída: A lista de posições (offsets em bytes) onde a substring foi encontrada.
- Algoritmo utilizado: Boyer-Moore.
- Sobre a implementação: O algoritmo escolhido foi o Boyer-Moore, devido a sua alta velocidade de busca e ocupação de espaço reduzida. As funções foram implementadas com base nas referências listadas ao final d0 arquivo, e a dificuldade de implementação foi de nível médio, levando em consideração que havia muito conteúdo para auxiliar e explicar o processo. Ao lidar com os blocos de conteúdos para o processamento de arquivos maiores que a memória RAM disponível, assim como o problema de fronteiras, o nível de dificuldade aumentou e a adaptação das funções gerou alguns problemas.

### Etapa 3 | Busca de Substring em Arquivo Comprimido
- Objetivo: Integrar e evoluir as etapas anteriores para permitir a busca por substring diretamente no arquivo gerado pela Etapa 1, sem descompressão total.
- Comando: `sistema_de_processamento_de_arquivos buscar_compactado arquivos/<arquivo_compactado> "<substring>"`
- Algoritmo pensado: Boyer-Moore.
- Sobre a implementação: A solução pensada para isso consiste em modificar o formato de saída da Etapa 1, dividindo o arquivo original em blocos independentes de compressão e criando um índice que registre, para cada bloco, sua posição no arquivo compactado e a faixa de bytes correspondente no arquivo original. Durante a busca, apenas o índice é carregado em memória, e o programa passa a descompactar seletivamente apenas os blocos relevantes, aplicando o algoritmo de busca em cada um deles. Quando necessário, também deve verificar ocorrências que cruzam a fronteira entre dois blocos, combinando o final de um bloco com o início do próximo - como já implementado na Etapa 2. Embora tenhamos compreendido a arquitetura necessária, a implementação exigiria muitas alterações no compressor e no descompressor desenvolvidos na Etapa 1, o que acabou ultrapassando o tempo disponível. Por isso, não foi possível concluir completamente a etapa, mas a lógica e o desenho da solução foram estudados e compreendidos.
  
## Autores

- Ingrid Cristine Rocha
- Milena Calegari Dourado

## Referências

ETAPA 1
- [Entendendo o algoritmo de Huffman | Compressão | Árvore binária](https://youtu.be/4hHZdTfWZtQ?si=DYzVMvTkR2qSPCA4)
- [Huffman Coding - Python Implementation and Demo](https://youtu.be/JCOph23TQTY?si=0RuYMkOfdrHB9_L_)
- [Text File Compression And Decompression Using Huffman Coding](https://www.geeksforgeeks.org/dsa/text-file-compression-and-decompression-using-huffman-coding/)


ETAPA 2
- [Boyer Moore Algorithm | Good Suffix heuristic](https://www.geeksforgeeks.org/dsa/boyer-moore-algorithm-good-suffix-heuristic/)
- [Boyer Moore Algorithm in Python](https://www.geeksforgeeks.org/dsa/boyer-moore-algorithm-in-python/)
- [Aula 13: Strings - Busca de Substrings](https://youtu.be/TuAJG9nZ-gY?si=5yomCnUxbuV1Dorj)
- [ADS1: Practical: Implementing Boyer-Moore](https://youtu.be/CT1lQN73UMs?si=SNuxzzx_WLX6Q_uo)
- [ADS1: Preprocessing](https://youtu.be/HGVQi5xX44M?si=l3nrk8MD1LyrnxzN)
- [ADS1: Boyer-Moore basics](https://youtu.be/4Xyhb72LCX4?si=8fisJb5VXY8qzbbv)

ETAPA 3
- [Search and Retrieval of Compressed Text](https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S0065245804630063?utm_source=chatgpt.com)
- [Is there a compression format that allows decompression at any point in the file?](https://stackoverflow.com/questions/41896388/is-there-a-compression-format-that-allows-decompression-at-any-point-in-the-file?utm_source=chatgpt.com)
