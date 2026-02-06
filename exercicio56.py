# Verificar se uma palavra começa com uma letra específica.

palavra = input("Digite uma palavra: ").lower()
letra = input("Digite uma letra: ").lower()

if palavra.startswith(letra):
    print(f"A palavra começa com a letra {letra}")
else:
    print(f"A palavra não começa com a letra {letra}")