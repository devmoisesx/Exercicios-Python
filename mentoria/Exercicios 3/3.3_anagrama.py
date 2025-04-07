lista = ["roma", "amor"]
lista2 = ["pedra", "padre"]
lista3 = ["arara", "ana"]
lista4 = ["remo", "toma"]
lista5 = ["treta", "ateRt"]
lista6 = []
lista7 = ["palavra"]
lista8 = ["", "palavra"]
lista9 = ["palavra", ""]
lista10 = ["palavra", " "]
lista11 = [" ", ""]
lista12 = [1, 1]
lista13 = "Abacate"
lista14 = 123
lista15 = ["roma", "amor", "roma"]


def eAnagrama(lista: list):
    # Verifica se é uma lista
    if type(lista) != list:
        return None
    
    # Verifica se a lista possui 2 palavras
    if len(lista) <= 0 or len(lista) <= 1 or len(lista) > 2:
        return None
    
    # Verifica se o item é string
    if type(lista[0]) != str and type(lista[1]) != str:
        return None
    
    # Verifica se a lista possui string vazia
    for w in lista:
        if w == "" or w == " ":
            return None

    # Separa em uma lista letra por letra da palavra e ordena em ordem alfabética e verifica se a lista de letras sao iguais
    if sorted(list(lista[0].lower())) == sorted(list(lista[1].lower())):
        return True
    return False

print(eAnagrama(lista))
print(eAnagrama(lista2))
print(eAnagrama(lista3))
print(eAnagrama(lista4))
print(eAnagrama(lista5))
print(eAnagrama(lista6))
print(eAnagrama(lista7))
print(eAnagrama(lista8))
print(eAnagrama(lista9))
print(eAnagrama(lista10))
print(eAnagrama(lista11))
print(eAnagrama(lista12))
print(eAnagrama(lista13))
print(eAnagrama(lista14))
print(eAnagrama(lista15))
