# 1

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou o número: {numero}")
        break
    except ValueError:
        print("Erro: Você não digitou um número inteiro válido, Tente novamente.")
        break

# 2
while True:
    try:
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro:"))
        div = numero1/numero2
        print(div)
        break
    except  ZeroDivisionError:
        print('impossivel dividir por zero, tente novamente.')
        break

# 3

def obter_elemento_por_indice(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Erro: O índice fornecido não existe na lista."
minha_lista = ['Maçã', 'Banana', 'Laranja', 'Uva']
meu_indice = 2

resultado = obter_elemento_por_indice(minha_lista, meu_indice)
print(resultado)

indice_invalido = 10
resultado_erro = obter_elemento_por_indice(minha_lista, indice_invalido)
print(resultado_erro)
