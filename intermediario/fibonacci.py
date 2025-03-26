termos = int(input("Quantos termos você quer mostrar? "))

termo1 = 0
termo2 = 1
count = 3

print(f"{termo1} -> {termo2}", end='')

while count <= termos:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    count += 1
    print(f" -> {termo3}", end='')
    