# Mostrar o menor número de uma lista.

numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite o {i +1}º número: ")))

menor = min(numeros)

print(f"O menor número é {menor}")