# Ler uma frase e contar quantas letras ela tem.

frase = input("Digite uma frase: ")

contador = 0

for char in frase:
    if char.isalpha():
        contador +=1

print(f"A frase tem {contador} letras")