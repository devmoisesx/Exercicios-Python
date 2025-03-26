palavra = "Abacate"
vogais = ["a", "e", "i", "o", "u"]
count = 0

for i in list(palavra.lower()):
    for j in vogais:
        if j == i:
            count += 1

print(count)