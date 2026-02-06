# Contar quantos números o usuário digitou.

contador = 0

while True:
    numero = float(input("Digite um número (digite 0 para sair): "))
    if numero == 0:
        break
    contador +=1

print(f"Você digitou {contador} números")
    