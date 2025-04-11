import uuid
from itertools import permutations
import time

lista = ["andar", "nadar"]


def verificarPalavra(p1: str, p2: str):
    if type(p1) != str or type(p2) != str:
        return print(None)

    if p1 == "" or p2 == "":
        return print(None)

    if p1 == " " or p2 == " ":
        return print(None)
    
    if len(p1) != len(p2):
        return print(False)
    
    # result = eAnagrama(p1, p2)
    # return result

    return eAnagrama(p1, p2)

def eAnagrama(p1: str, p2:str):
    if sorted(p1.lower()) != sorted(p2.lower()):
        return False
    return True

quantidade = 10000000

inicio = time.time()
for i in range(quantidade):
    verificarPalavra(lista[0], lista[1])
fim = time.time()

print(f"Tempo de execução: {fim - inicio:.4f} segundos")

# print(lista)
# print(lista[0].lower())
# print(lista[1].lower())
# print(lista[0].lower())
# print(lista[1][::-1].lower())
# print(lista[0][::-1].lower())
# print(lista[1].lower())
# print(sorted(lista[0]))
# print(sorted(lista[1]))

# def eAnagrama(lista: list):
# # Verifica se é uma lista
# if type(lista) != list:
#     return None

# # Verifica se a lista possui 2 palavras
# if len(lista) <= 0 or len(lista) <= 1 or len(lista) > 2:
#     return None

# # Verifica se o item é string
# if type(lista[0]) != str and type(lista[1]) != str:
#     return None

# # Verifica se a lista possui string vazia
# for w in lista:
#     if w == "" or w == " ":
#         return None

# Separa em uma lista letra por letra da palavra e ordena em ordem alfabética e verifica se a lista de letras sao iguais
# if sorted(list(lista[0].lower())) == sorted(list(lista[1].lower())):
#     return True
# return False


# def eAnagrama(lista: list):
#     # Verifica se é uma lista
#     if type(lista) != list:
#         return None

#     # Verifica se a lista possui 2 palavras
#     if len(lista) <= 0 or len(lista) <= 1 or len(lista) > 2:
#         return None

#     # Verifica se o item é string
#     if type(lista[0]) != str and type(lista[1]) != str:
#         return None

#     # Verifica se a lista possui string vazia
#     for w in lista:
#         if w == "" or w == " ":
#             return None

# #     if sorted(list(lista[0].lower())) == sorted(list(lista[1].lower())):
#         # return print(lista[0].lower(), ''.join(reversed(lista[1].lower())))
#         return print(sorted(lista[0][::1].lower()), sorted(lista[0][::1].lower()))
#     return False

# palavra1 = sorted(p1.lower())
    # palavra2 = sorted(p2.lower())

    # if palavra1 == palavra2:
    #     return True
    # return False
    # - 4.8 segundos rodando com 10 milhoes

    # if sorted(lista[0].lower()) == sorted(lista[1].lower()):
    #     # return print(True)
    #     return True
    # return False
    # - 6 segundos rodando com 10 milhoes

    # if p1.sort().lower() == p2.sort().lower():
    #     return print(True)
    #     # return True
    # return False
    # - 6 segundos rodando com 10 milhoes

    # if sorted(list(lista[0].lower())) == sorted(list(lista[1].lower())):
    #     return True
    # return False
    # - 7 segundos rodando com 10 milhoes

    # if sorted(lista[0][::-1].lower()) == sorted(lista[1][::-1].lower()):
    #     return True
    # return False
    # - 8 segundos rodando com 10 milhoes

    # lista1 = list(lista[0])
    # lista2 = list(lista[1])

    # lista1.sort()
    # lista2.sort()

    # count = 0
    # igual = True
    # while count < len(lista[0]) and igual:
    #     if lista1[count] == lista2[count]:
    #         count += 1
    #     else:
    #         igual = False
    # return igual
    # - 6.7 segundos rodando com 10 milhoes

    # if lista[0].lower() == lista[1].lower() or lista[0].lower() == lista[1][::-1].lower() or lista[0][::-1].lower() == lista[1].lower():
    #     # return print(True)
    #     return True
    # return False

# print(eAnagrama(lista))
# print(eAnagrama(lista2))
# print(eAnagrama(lista3))
# print(eAnagrama(lista4))
# print(eAnagrama(lista5))

# print(eAnagrama(lista6))
# print(eAnagrama(lista7))
# print(eAnagrama(lista8))
# print(eAnagrama(lista9))
# print(eAnagrama(lista10))
# print(eAnagrama(lista11))
# print(eAnagrama(lista12))
# print(eAnagrama(lista13))
# print(eAnagrama(lista14))
# print(eAnagrama(lista15))
