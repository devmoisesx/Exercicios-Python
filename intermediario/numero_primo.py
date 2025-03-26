num = int(input("Informe um número: "))

def verificarPrimo(num):
    if num < 2:
        return False    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        
print(verificarPrimo(num))