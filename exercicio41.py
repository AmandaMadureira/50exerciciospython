# Calcular a média dos valores de uma lista.

numeros = []

for i in range(5):
    numeros.append(float(input(f"Digite o {i + 1}º número: ")))
    
media = sum (numeros) / len (numeros)

print(f"A média entre os números digitados é igual a {media:.2f}")