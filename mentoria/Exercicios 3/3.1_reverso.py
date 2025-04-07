palavra = "rua"
palavra2 = 2

def reverterPalavra(palavra):
    if not type(palavra) is str:
        return None
    reverso = ""
    for w in palavra[::-1]:
        reverso += w
    return reverso

print(reverterPalavra(palavra))
print(reverterPalavra(palavra2))