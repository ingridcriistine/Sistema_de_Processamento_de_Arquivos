def buscar_simples(arquivo_original, pat, block_size=4096):
    print(f"Buscando '{pat}' em {arquivo_original}" )
    
    m = len(pat)
    if m == 0:
        print("Padrão vazio")
        return []
    
    bad_char = bad_character_rule(pat)
    good_suffix = good_suffix_rule(pat)
    
    combinacoes = []
    offset = 0             
    sobra = ""
    
    with open(arquivo_original, "r", encoding="utf-8") as arquivo:
        while True:
            bloco = arquivo.read(block_size)
            if not bloco:
                break
        
            texto = sobra + bloco
            matches = boyer_moore_chunk(texto, pat, bad_char, good_suffix)
            
            for pos in matches:
                if pos >= len(sobra):
                    # Posição em caracteres dentro do bloco atual
                    pos_char = pos - len(sobra)
                    
                    # Convertemos o trecho até a posição para bytes
                    bytes_antes = texto[:pos].encode("utf-8")
                    pos_byte = len(bytes_antes)
                    
                    # combinacoes.append(offset + pos - len(sobra)) #posição inicial da combinação
                    combinacoes.append(offset + pos_byte) #qtd de bytes ate a posição inicial
            
            sobra = texto[-(m-1):] if m > 1 else ""
            # offset += len(bloco)
            offset += len(bloco.encode("utf-8"))
        
    print("Ocorrências encontradas (offsets em bytes):", combinacoes)
    return combinacoes
        
def boyer_moore_chunk(txt, pat, bad_char, good_suffix):
    m = len(pat)
    n = len(txt)
    posicaoAtual = 0
    res = []
    
    while posicaoAtual <= n-m:
        j = m-1
        
        while j >= 0 and pat[j] == txt[posicaoAtual+j]:
            j-=1
        
        #achou a combinação completa
        if j < 0:
            res.append(posicaoAtual)
            posicaoAtual += good_suffix[0]
        else:
            mismatch_char = txt[posicaoAtual+j]
            bad_char_skip = j - bad_char.get(mismatch_char, -1)
            good_suffix_skip = good_suffix[j]
            
            skip = max(1, bad_char_skip, good_suffix_skip) #escolhe o maior pulo
            posicaoAtual += skip
    
    return res
    
def bad_character_rule(pat):
    tabela = {}
    
    for i, char in enumerate(pat):
        tabela[char] = i
        
    return tabela
    
def good_suffix_rule(pat):
    m = len(pat)
    tabela = [0] * (m+1)
    border_positions = [0] * (m+1)
    
    i = m
    j = m+1
    border_positions[i] = j
    
    while i > 0:
        while j<=m and pat[i-1] != pat[j-1]:
            if tabela[j-1] == 0:
                tabela[j-1] = j-i
            j = border_positions[j]
        i -= 1
        j -= 1
        
        border_positions[i] = j
        
    #preenche valores que faltaram
    j = border_positions[0]
    for i in range(m):
        if tabela[i] == 0:
            tabela[i] = j
    
    return tabela