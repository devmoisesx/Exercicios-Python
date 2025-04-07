# lista = ["mirim", "arara"]
lista = ["mirim", "Banana"]
# lista = []

def ePalindromo(lista):
    resultados = []
    if len(lista) <= 0:
        return False
    for w in lista:
        if w in w[::-1]:
            resultados.append(True)
        else:
            resultados.append(False)

        # Outro jeito de fazer:
        # reverso = ""
        # print(w)
        # for l in w[::-1]:
        #     reverso += l
        # print(reverso)
        # if w == reverso:
        #     resultados.append(True)
        # else:
        #     resultados.append(False)

    return resultados

print(ePalindromo(lista))