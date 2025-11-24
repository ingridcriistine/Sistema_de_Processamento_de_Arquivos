def buildHuffmanCodes(root, code, codes):
    if root is None:
        return
    
    if root.char is not None:
        codes[root.char] = code
        return

    buildHuffmanCodes(root.left,  code + "0", codes)
    buildHuffmanCodes(root.right, code + "1", codes)


def gerar_codigos(root):
    codigos = {}
    buildHuffmanCodes(root, "", codigos)
    return codigos

    