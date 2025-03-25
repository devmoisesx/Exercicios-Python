# Usando Objetos --------------
# lados = {
#     "Superior": 15,
#     "Inferior": 10,
#     "Esquerdo": 20,
#     "Direito": 10
# }

# angulos = {
#     "SuperEsq": 90,
#     "SuperDir": 90,
#     "InferiorEsq": 90,
#     "InferiorDir": 90
# }

# def identifcarQuadrado(lados, angulos):
#     for canto in angulos.values():
#         if canto != 90:
#             return "Não é um quadrado! Pois possui um canto com um angulo diferente de 90 graus."
#     for lado in lados.values():
#         for i in lados.values():
#             if lado != i:
#                 return "Não é um quadrado! Pois possui um lado diferente do outro."
#     return "É um quadrado!"

# print(identifcarQuadrado(lados, angulos))

# Usando listas --------------
lados = [10, 10, 10, 10]
# lados = [15, 10, 10, 10]
# lados = [10, 15, 10, 10]
angulos = [90, 90, 90, 90]
# angulos = [95, 90, 90, 90]
# angulos = [30, 30, 30, 30]

# Usando loops --------------
# def identifcarQuadrado(lados, angulos):
#     for angulo in angulos:
#         if angulo != 90:
#             return "Não é um quadrado! Possui um angulo diferente de 90 graus."

#     for i in range(len(lados) - 1):
#         if lados[i] != lados[i + 1]:
#             return "Não é um quadrado! Não possui todos os lados iguais."
        
#     return "É um quadrado!"

# usando all() --------------
# def identifcarQuadrado(lados, angulos):
#     if not (all(x == lados[0] for x in lados) and all(x == angulos[0] for x in angulos) and angulos[0] == 90):
#         return "Não é um quadrado!"

#     return "É um quadrado!"

# Usando set() --------------
def identifcarQuadrado(lados, angulos):
    if not len(set(lados)) == 1:
        return "Não é um quadrado! Possui um lado com tamanho diferente dos demais."

    if not (len(set(angulos)) == 1 and angulos[0] == 90):
        return "Não é um quadrado! Possui um angulo diferente de 90 graus."

    # forma reduzida:
    # if not (len(set(lados)) == 1 and len(set(angulos)) == 1 and angulos[0] == 90):
    #     return "Não é um quadrado!"

    return "É um quadrado!"

print(identifcarQuadrado(lados, angulos))
