# Ler 5 números e mostrar a soma deles.

soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

print(f"A soma dos cinco números é {soma}")