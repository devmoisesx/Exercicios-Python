print("Programa para calcular um fatorial.")

num = int(input("Me informe um número inteiro: "))
fatorial = []
calculo = 1

for i in range(num, 0, -1):
    fatorial.append(i)

for j in range(len(fatorial), 0, -1):
    fat = int(j)
    calculo *= fat

valorFatorial = ''
for n in fatorial:
    valorFatorial += str(n) + ', '
valorFatorial = valorFatorial[:-2]

print(f"{num}! = {valorFatorial} = {calculo}")