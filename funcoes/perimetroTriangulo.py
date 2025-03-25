lados = [10, 25, 20]

def perimetroTriangulo(lados):
    perimetro = 0
    for lado in lados:
        perimetro += lado
    return perimetro

print(perimetroTriangulo(lados))