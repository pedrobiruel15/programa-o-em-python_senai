# 1

def verificar_par_ou_impar(num1, num2):
    def par_ou_impar(n):
        return "Par" if n % 2 == 0 else "Ímpar"
        
    resultado1 = par_ou_impar(num1)
    resultado2 = par_ou_impar(num2)

    return f"O primeiro número ({num1}) é {resultado1} e o segundo ({num2}) é {resultado2}."
print(verificar_par_ou_impar(9, 12))

# 2

def multiplicar_numeros(n1, n2, n3):
    resultado = n1 * n2 * n3
    return resultado

resultado_final = multiplicar_numeros(19, 20, 3)
print(f'o resultado é: {resultado_final}')

# 3

def elevado(num1):
    resultado = num1 ** 2
    return resultado

resultado_final = elevado(10)
print(f'o resultado é: {resultado_final}')

# 4

def idade():
    idadeus = int(input('qual é a sua idade?'))
    if idadeus <18:
        print('idade não suficiente')
    else:
        print('idade suficiente')
idade()
    
# 5

def aniversario():
     anoquenasceu = int(input('qual o ano que nasceu?'))
     anoatual =  int(input('qual o ano atual?'))
     print(anoatual - anoquenasceu)
    
aniversario()
