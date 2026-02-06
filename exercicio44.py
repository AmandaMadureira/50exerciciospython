# Mostrar os nomes em ordem alfabética.

nomes = []

for i in range(5):
    nomes.append(input(f"Digite o {i + 1}º nome: "))

nomes.sort()

print("Nomes na ordem alfabética: ")

for nome in nomes:
    print(nome)