# 1


numeros = 1 
while numeros <= 1000:
    print(numeros)
    numeros = numeros + 1


# 2

nomes = []
contador = 0

while contador <= 10:
    nome = input(f'digite seu nome aqui{contador + 1}')
    nomes.append(nome)
    contador += 1


print('\n--- pessoas cadastradas ---')
for n in range (10):
    nome = input ('nome')
    print(nome)