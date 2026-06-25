
senha_correta = "professor123"
tentativas = 3
acesso_permitido = False


while tentativas > 0:
    senha_digitada = input("Digite a senha de acesso: ")
    
    if senha_digitada == senha_correta:
        print("\nAcesso concedido!")
        acesso_permitido = True
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta. Você ainda tem {tentativas} tentativa(s).")
        else:
            print("\nConta bloqueada! Senha incorreta inserida 3 vezes.")


if acesso_permitido:

    dados_aluno = {"nome": "", "notas": []}
    
    dados_aluno["nome"] = input("\nDigite o nome do aluno: ")

    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota do aluno: "))
        dados_aluno["notas"].append(nota)
        
 
    soma = sum(dados_aluno["notas"])
    quantidade = len(dados_aluno["notas"])
    media = soma / quantidade
    
    print("\n" + "="*30)
    print("      RELATÓRIO FINAL      ")
    print("="*30)
    print(f"Aluno: {dados_aluno['nome']}")
    print(f"Notas: {dados_aluno['notas']}")
    print(f"Média Final: {media:.2f}")
    print("="*30)

input('Digite enter para sair')
