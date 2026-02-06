# Mostrar o maior número de uma lista.

numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite o {i + 1}º número: ")))

maior = max(numeros)

print(f"O maior número da lista é {maior}")