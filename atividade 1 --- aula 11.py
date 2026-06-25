# 1

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou o número: {numero}")
        break
    except ValueError:
        print("Erro: Você não digitou um número inteiro válido. Tente novamente.")

# 2
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou o número: {numero}")
        break