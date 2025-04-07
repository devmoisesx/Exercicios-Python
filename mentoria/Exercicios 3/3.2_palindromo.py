lista = ["mirim", "arara"]
lista2 = ["mirim", "Banana"]
lista3 = []
palavra = "Arara"
frase = "Subi no Onibus"
numero = 1
numero2 = [1, 1]


def ePalindromo(palavra):
    word = ""
    resultados = []
    if type(palavra) != list:
        if not type(palavra) is str:
                return None
        word = "".join(palavra.lower().split())
        if word == word[::-1]:
            resultados.append(True)
    else:
        word = palavra
        # verifica se a lista possui 1 item
        if len(word) <= 0:
            return None
        for w in word:
            if not type(w) is str:
                return None
            if w in w[::-1]:
                resultados.append(True)
            else:
                resultados.append(False)

    return resultados


print(ePalindromo(lista))
print(ePalindromo(lista2))
print(ePalindromo(lista3))
print(ePalindromo(palavra))
print(ePalindromo(frase))
print(ePalindromo(numero))
print(ePalindromo(numero2))
