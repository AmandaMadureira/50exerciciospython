# Criar uma lista com 5 números e mostrar todos.

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Os números digitados foram: ")

for num in numeros:
    print(num)
