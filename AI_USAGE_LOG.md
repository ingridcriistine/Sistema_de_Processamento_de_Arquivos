# Relatório de Uso de Inteligência Artificial Generativa

Este documento registra todas as interações significativas com ferramentas de IA generativa (como Gemini, ChatGPT, Copilot, etc.) durante o desenvolvimento deste projeto. O objetivo é promover o uso ético e transparente da IA como ferramenta de apoio, e não como substituta para a compreensão dos conceitos fundamentais.

## Política de Uso
O uso de IA foi permitido para as seguintes finalidades:
- Geração de ideias e brainstorming de algoritmos.
- Explicação de conceitos complexos.
- Geração de código boilerplate (ex: estrutura de classes, leitura de arquivos).
- Sugestões de refatoração e otimização de código.
- Debugging e identificação de causas de erros.
- Geração de casos de teste.

É proibido submeter código gerado por IA sem compreendê-lo completamente e sem adaptá-lo ao projeto. Todo trecho de código influenciado pela IA deve ser referenciado neste log.

---

## Registro de Interações

### Interação 1

- **Data:** 16/11/2025
- **Etapa do Projeto:** 0 - Definições iniciais
- **Ferramenta de IA Utilizada:** ChatGPT
- **Objetivo da Consulta:** Estávamos em dúvida sobre qual seria a linguagem de programação mais adequada para o desafio proposto.

- **Prompt(s) Utilizado(s):**
  1. "Qual o nível de dificuldade de utilizar a linguagem C para compactar um arquivo de texto grande e, posteriormente, realizar buscas por
substrings diretamente no arquivo compactado, de forma eficiente e sem a necessidade de descompressão total. Todos os recursos serão implementados do zero, sem funções prontas da própria linguagem."
  2. "Qual seria a linguagem mais indicada para realizar o desafio de forma mais simples e eficiente?"

- **Resumo da Resposta da IA:**
  A IA explicou que o nível de dificuldade da utilização da linguagem C para o projeto seria muito alto, principalmente devido a implementação sem bibliotecas externas. Seria necessário lidar com restrição de memória e arquivos enormes, assim como possuir domínio de vários assuntos avançados em C.
  Ao perguntar sobre outras linguagens, indicou Python e Java como as melhores opções para o projeto, assim como destacou que com Python seria muito mais simples e produtivo.

- **Análise e Aplicação:**
  A resposta da IA esclareceu alguns pontos fortes e fracos das linguagens e ajudou a escolher a mais adequada para a elaboração do projeto (Python).


### Interação 2

- **Data:** 21/11/2025
- **Etapa do Projeto:** Compressão
- **Ferramenta de IA Utilizada:** ChatGPT
- **Objetivo da Consulta:** Queríamos saber como funcionava a questão da leitura de arquivos e o consumo da memória RAM, afim de pensar em uma opção estável.
- **Prompt(s) Utilizado(s):** 
1. "Como funciona a leitura de arquivos e o consumo da memória ram?"
2. Como que eu dimensiono o quanto que memória ram devo utilizar dependendo do arquivo??
- **Resumo da Resposta da IA:**
 Foi apresentado diferentes tipos de leitura de arquivo e como cada um se comporta com o uso da memória RAM. Apresentou também pontos que fazem pesar mais esse consumo de memória como buffers grandes e uso de split. Além disso, mostrou que o uso da RAM não é dimensionado pelo tamanho do arquivo e sim pelo tamanho do buffer que eu uso, enfatizando que não se deve utilizar o tamanho do buffer do mesmo tamanho do arquivo.
- **Análise e Aplicação:** 
  Disso foi retirado uma ideia de como diminuir a quantidade de consumo da memória RAM ao ler um arquivo.
- **Referência no Código:** ...

---
