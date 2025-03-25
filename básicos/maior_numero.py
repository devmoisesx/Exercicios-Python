print("Programa para saber se um número é maior que outro.\n")

try:
    num1 = float(input("Me informe o primeiro número: "))
    num2 = float(input("Me informe o segundo número: "))   
    maiorNumero = 0
    menorNumero = 0

    if num1 > num2:
        maiorNumero = num1
        menorNumero = num2
    else:
        maiorNumero = num2
        menorNumero = num1

    print(f"O número {maiorNumero} é maior que número {menorNumero}")
except:
    print("Valor inválido! Digite um valor númerico.")

