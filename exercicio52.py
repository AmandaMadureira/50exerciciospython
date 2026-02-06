# Verificar se uma palavra é um palíndromo.

palavra = input("Digite uma palavra: ").lower()

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")