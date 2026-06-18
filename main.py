

print ('E-comerce X')

produtos = ['', '1 - HD','2 - monitor',' 3 - teclado']

valores = [0,500.0,5000.0,250.0,14000.0]

print(f'''
{produtos[1]} R$ {valores[1]}
{produtos[2]} R$ {valores[2]}
{produtos[3]} R$ {valores[3]}


   ''')

carrinho = []
total = []



produto_1 = int(input('produto: '))
produto_2 = int(input('produto: '))
produto_3 = int(input('produto: '))


carrinho.extend([produto_1, produto_2, produto_3,])
total.extend([valores[produto_1], valores[produto_2], valores[produto_3]])
print('***' * 20)
print('R$', sum(total))
print('produtos:', carrinho)
print('Obrigado Volte Sempre!')