def menu():
    #while(True):
    print("""Seja bem vindo(a)!
Digite a opção desejada:
1 - Cadastrar cliente
2 - Clientes
3 - Pedidos
4 - Busca
5 - Sair       
        """)
    opcao = input().lower()
    if (opcao == "1" or opcao == "cadastrar cliente" or opcao == "cadastrar"):
        menu2()
    elif(opcao == "2" or opcao == "clientes"):
        menu3()
    elif(opcao == "5" or opcao == "sair"):
        print("você saiu")
            #break


def menu2():
    while(True):
        print("Digite o nome do cliente:")
        nome = str(input().capitalize()) #deixa a primeira letra em maiusculo
        print("Digite o CPF")
        cpf = (input())
        cpfN = "0123456789"
        cpfCorreto = ""
        for i in cpf:
            if i in cpfN:
                cpfCorreto += i    
        print("Digite a idade:")
        idade = int(input())
        cpfVerificado = len(cpfCorreto) == 11
        if (cpfVerificado and idade >= 18 and nome == str):
            print("Cadastro concluido")
            with open('projeto//clientes.txt', "a")as arquivo:
                arquivo.write(f"{nome}, {cpf}, {idade}\n")
            break
        elif(len(cpfCorreto) <11 and idade < 18):
            print("O CPF está incompleto e é menor de idade")
        elif (len(cpfCorreto) <11):
            print("O cpf está incompleto")
        elif(idade < 18):
            print("É menor de idade")
        elif(nome != str):
            print("Digite um nome")


        print("""1 - Continuar
2 - Voltar
""")
        while(True):
            op = input().lower()
            if (op == "2" or op == "voltar"):
                menu()
            elif(op == "1" or op== "continuar"):
                break
            else:
                print("Digite uma opção")


    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    voltar = input().lower()
    if (voltar == "1" or voltar == "sim"):
        menu()
    elif(voltar == "2" or voltar == "não"):
        print("Você saiu!")

def menu3():
    print("Clientes cadastrados:")
    print("")
    with open('projeto//clientes.txt', "r") as arquivo:
        linha = arquivo.readlines()
        for linhas in linha:
            print(linhas, end = "")
        print("")
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    voltar = input().lower()
    if (voltar == "1" or voltar == "sim"):
        menu()
    elif(voltar == "2" or voltar == "não"):
        print("Você saiu!")
        

menu()