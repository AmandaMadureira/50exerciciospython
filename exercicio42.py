# Contar quantos números pares existem na lista.
numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite o {i + 1}º número: ")))

contador = 0

for n in numeros:
    if n % 2 == 0:
        contador += 1

print(f"A quantidade de números pares é: {contador}")