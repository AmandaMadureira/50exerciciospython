# Ler vários números até o usuário digitar 0.

while True:
    numero = float(input("Digite um número (digite 0 se quiser sair): "))
    
    if numero == 0:
        break
    print(f"Você digitou {numero}")

print("Programa encerrado")