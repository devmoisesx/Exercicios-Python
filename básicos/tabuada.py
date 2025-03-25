print("Programa que exibe a tabuada de um número.")

try:
    num = int(input("Por favor me informe um número inteiro: "))

    for i in range(11):
        print(f"{num} x {i} = {num * i}")
except:
    print("Valor inválido! Por favor digite um valor válido.")