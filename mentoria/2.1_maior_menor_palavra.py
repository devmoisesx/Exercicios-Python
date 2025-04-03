lista = ["abc", "abcde", "ab", "abcdefg", "a", "a", "a", "ab", "ab", "abc"]
# lista = ["abc", "abcde", "ab", "abcdefg", "a", "a", "a", "ab", "ab", "abc", 2, 5]
palavra = ""


def maiorPalavra(lista):
       palavra = lista[0]
       for i in range(len(lista)):
            tamanho = 0
            for j in lista[i]:
                    tamanho += 1
            if tamanho > len(palavra):
                palavra = lista[i]
       return palavra

def maiorMenorPalavra(lista):
        for palavra in lista:
                if not type(palavra) is str:
                       return "Valor inválido! Apenas texto é permitido."
        maiorPalavra = maiorPalavra(lista)
        menorPalavra = ""
            # print(tamanho)
        return print(f"A maior palavra é: {maiorPalavra}, e a menor palavra é: {menorPalavra}")



print(maiorMenorPalavra(lista))