def buscar_simples(arquivo_original, pat):
    print(f"Buscando '{pat}' em {arquivo_original}" )
    
    with open(arquivo_original, "r", encoding="utf-8") as arquivo:
        txt = arquivo.read()
        
    posicoes = boyer_moore(txt, pat)
    print("Ocorrências encontradas:", posicoes)
        
def boyer_moore(txt, pat):
    m = len(pat)
    n = len(txt)
    
    if m == 0:
        return []
    
    bad_char = bad_character_rule(pat)
    good_suffix = good_suffix_rule(pat)
    
    combinacoes = []
    posicaoAtual = 0
    
    while posicaoAtual <= n-m:
        j = m-1
        
        while j >= 0 and pat[j] == txt[posicaoAtual+j]:
            j-=1
        
        #achou a combinação completa
        if j < 0:
            combinacoes.append(posicaoAtual)
            posicaoAtual += good_suffix[0]
        else:
            mismatch_char = txt[posicaoAtual+j]
            ultima_posicao = bad_char.get(mismatch_char, -1)
            bad_char_skip = j-ultima_posicao
            
            good_suffix_skip = good_suffix[j]
            
            skip = max(1, bad_char_skip, good_suffix_skip) #escolhe o maior pulo
            posicaoAtual += skip
    
    return combinacoes
    
def bad_character_rule(pat):
    tabela = {}
    
    for i, char in enumerate(pat):
        tabela[char] = i
        
    return tabela
    
def good_suffix_rule(pat):
    m = len(pat)
    tabela = [0] * m
    border_positions = [0] * (m+1)
    
    i = m
    j = m+1
    border_positions[i] = j
    
    while i > 0:
        while j<=m and pat[i-1] != pat[j-1]:
            if tabela[j] == 0:
                tabela[j] = j-1
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