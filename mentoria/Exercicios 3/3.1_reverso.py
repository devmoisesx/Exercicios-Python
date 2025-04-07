palavra = "rua"

def reverterPalavra(palavra):
    reverso = ""
    for w in palavra[::-1]:
        reverso += w
    return reverso

print(reverterPalavra(palavra))