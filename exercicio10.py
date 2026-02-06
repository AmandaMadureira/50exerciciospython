# Leia um número e mostre sua tabuada (1 a 10)

num = int(input("Digite um número: "))

print(f"Tabuada de {num}")
for i in range (1,11):
    print(f"{num} x {i} = {num * i}")