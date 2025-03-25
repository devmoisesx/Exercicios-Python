try:
    num1 = int(input("Me informe um número para saber se é par ou ímpar: "))
    result = num1 % 2
    if result == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except:
    print("Valor digitado inválido.")

