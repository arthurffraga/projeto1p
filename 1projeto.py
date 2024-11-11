def menu():
    #while(True):
    print("""Seja bem vindo(a)!
Digite a opção desejada:
1 - Cadastrar cliente
2 - Clientes
3 - Cadastrar produto
4 - Estoque
5 - Cadastrar venda
6 - Relatorio de vendas       
        """)
    opcao = input().lower()
    if (opcao == "1" or opcao == "cadastrar cliente" or opcao == "cadastrar"):
        menu2()
    elif(opcao == "2" or opcao == "clientes"):
        menu3()
    elif(opcao == "3" or opcao == "cadastrar produto"):
        menu4()
    elif(opcao == "4" or opcao == "estoque"):
        menu5()
    elif(opcao == "5" or opcao == "cadastrar venda"):
        menu6()
    elif(opcao == "" or opcao == "sair"):
        print("você saiu")
            #break


def menu2():
    while(True):
        print("Digite o nome do cliente:")
        nome = (input().capitalize()) #deixa a primeira letra em maiusculo
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
        if (cpfVerificado and (idade >= 18) and (type(nome) == str)):
            print("Cadastro concluido")
            with open('projeto//clientes.txt', "a")as arquivo:
                arquivo.write(f"Nome: {nome}, CPf: {cpf}, Idade: {idade}\n")
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
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            menu()
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
       
def menu4():
    while(True):
        print("Digite o produto:")
        produto = str(input().lower())
        print("Digite o preço:")
        precoProduto = float(input())
        print("Digite a quantidade do produto:")
        qtdProduto = int(input())
        with open('projeto//estoque.txt', "a") as arquivo:
            arquivo.write(f"{produto} {precoProduto} {qtdProduto}\n")
        print("Produto cadastrado")
        print("")
        print("""Deseja voltar para o menu?
1- Sim
2- Não""")
        while(True):
            voltar = input().lower()
            if (voltar == "1" or voltar == "sim"):
                menu()
            elif(voltar == "2" or voltar == "não" or voltar == "nao"):
                print("Você saiu!")
                break
            else:
                print("Digite uma opção:")
       

def menu5():
    print("")
    print("Estoque:")
    with open('projeto//estoque.txt', "r") as arquivo:
        listaProduto = arquivo.readlines()
        for linhas in listaProduto:
            print(linhas, end= "")
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            menu()
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
       
def menu6():
    with open('projeto//estoque.txt', "r") as arquivo:
        listaProdutos= arquivo.readlines()
        for linhas in listaProdutos:
            print(linhas, end="")
    listaStr = ""
    for i in listaProdutos:
        listaStr += i
    listaDividida = listaStr.split()
    print(listaDividida)
    print("Qual produto foi vendido?")
    produto = input().lower()
    posicaoProduto = listaDividida.index(produto)
    posicaoEstoque = posicaoProduto + 2
    qtdEstoque = listaDividida[posicaoEstoque]
    print("Quantos foram vendidos?")
    vendidos = int(input())
    listaDividida.pop(posicaoEstoque)
    listaDividida.insert(posicaoEstoque, str(int(qtdEstoque) - vendidos))
    print(listaDividida)
    arquivoNovo = ""
    acumulador = 1
    for linha in listaDividida:
        arquivoNovo += linha
        arquivoNovo += " "
        if(acumulador % 3 == 0):
            arquivoNovo += "\n"
        acumulador += 1
    print(arquivoNovo)
    #with open('projeto//estoque.txt', "w") as novoEstoque:
        #novoEstoque.write(arquivoNovo)
menu()