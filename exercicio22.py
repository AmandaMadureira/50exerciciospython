# Ler duas notas e calcular a média. Informar se o aluno foi aprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print("Aluno aprovado!")

else:
    print("Aluno reprovado")

print(f"A sua média foi {media:.2f}")