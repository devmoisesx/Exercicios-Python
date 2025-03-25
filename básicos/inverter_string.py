print("Programa que inverte uma palavra.")

palavra = input("Me informe uma palavra: ")

print(palavra[::-1])

print("".join(reversed(palavra)))

palavraInvertida = ""
for i in range(len(palavra) -1, -1, -1):
    palavraInvertida += palavra[i]
print(palavraInvertida)