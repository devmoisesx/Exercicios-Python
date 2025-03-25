lados = [10, 10, 10, 10]
lados = [3, 3, 3, 3]
# lados = [55, 55, 55, 55]
# lados = [12, 10, 10, 10]

def perimetroQuadrilatero(lados):
    for i in range(len(lados) - 1):
        if lados[i] != lados[i + 1]:
            return "Não é um quadrado!"
    lado = lados[0]
    perimetro = lado * 4
    return perimetro

print(perimetroQuadrilatero(lados))