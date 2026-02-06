# Contar quantas vogais existem em uma frase.

frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
contador = 0

for char in frase:
    if char in vogais:
        contador +=1

print(f"A frase {frase} tem {contador} vogais")