# Ler a temperatura e dizer se está frio, agradável ou quente.

temp = int(input("Digite a temperatura atual: "))

if (temp > 25):
    print("O clima está quente")
elif (temp < 18):
    print("O clima está frio")
else:
    print("O clima está agradável")