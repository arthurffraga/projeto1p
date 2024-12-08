def menu():
    while(True):
        print("""Seja bem vindo(a) ao Geladíssimo
Digite a opção desejada:
1 - Clientes
2 - Estoque
3 - Vendas
4 - Sair""")
        opcao = input().lower()

        if (opcao == "1" or opcao == "clientes") :
            return(menuClientes())
        elif(opcao == "2" or opcao == "estoque"):
            return(menuEstoque())
        elif(opcao == "3" or opcao == "vendas"):
            return(menuVendas())
        elif(opcao == "4" or opcao == "sair"):
            print("Você saiu")
            break
        else:
            print("Digite uma opção")

def menuClientes():
    while(True):
        print("""Digite uma das opções:
1 - Cadastrar cliente
2 - Lista de clientes
3 - Voltar ao menu principal
4 - Atualizar
5 - Excluir
6 - Sair """)
        opcao = input().lower()
        if (opcao == "1" or opcao == "cadastrar cliente"):
            return(cadastrarCliente())
        elif(opcao == "2" or opcao == "lista de clientes"):
            return(listaClientes())
        elif(opcao == "3" or opcao == "voltar ao menu principal" or opcao == "voltar"):
            return(menu())      
        elif(opcao == "4" or opcao == "atualizar"):
            return(atualizarClientes())
        elif(opcao == "5" or opcao == "excluir"):
            return(excluirCliente())  
        elif(opcao == "6" or opcao == "sair"):
            print("Você saiu!")
            break
        else:
            print("Digite uma das opções")
def menuEstoque():
    while(True):
        print("""Digite uma das opções:
1 - Cadastrar produto
2 - Estoque
3 - Voltar ao menu principal
4 - Atualizar
5 - Excluir
6 - Sair """)
        opcao = input().lower()
        if (opcao == "1" or opcao == "cadastrar produto"):
            return(cadastrarProduto())
        elif(opcao == "2" or opcao == "estoque"):
            return(estoque())
        elif(opcao == "3" or opcao == "voltar ao menu principal" or opcao == "voltar"):
            return(menu())
        elif(opcao == "4" or opcao == "atualizar"):
            return(atualizarEstoque())
        elif(opcao == "5" or opcao == "excluir"):
            return(excluirProduto())
        elif(opcao == "6" or opcao == "sair"):
            print("Você saiu!")
            break
        else:
            print("Digite uma das opções")    

def menuVendas():
    while(True):
        print("""Digite uma das opções:
1 - Cadastrar venda
2 - Relatorio de vendas
3 - Voltar ao menu principal
4 - Atualizar
5 - Excluir
6 - Relatorio do total de vendas
7 - Sair """)
        opcao = input().lower()
        if (opcao == "1" or opcao == "cadastrar venda"):
            return(cadastrarVenda())
        elif(opcao == "2" or opcao == "relatorio de vendas"):
            return(relatorioVendas())
        elif(opcao == "3" or opcao == "voltar ao menu principal" or opcao == "voltar"):
            return(menu())
        elif(opcao == "4" or opcao == "atualizar"):
            return(atualizarVendas())
        elif(opcao == "5" or opcao == "excluir"):
            return(excluirVenda())
        elif(opcao == "6"):
            return(relatorioVendasTotal())            
        elif(opcao == "7" or opcao == "sair"):
            print("Você saiu!")
            break
        else:
            print("Digite uma das opções")   

def atualizarClientes():
    while(True):
        with open('projeto//clientes.txt', "r") as arquivo:
            listaClientes= arquivo.readlines()
            for linhas in listaClientes:
                print(linhas, end="")
        listaStr = ""
        for i in listaClientes:
            listaStr += i
        listaDividida = listaStr.split()
        print("Quem você deseja atualizar?")
        cliente = input().capitalize()
        print("""O que você deseja atualizar?
1 - Nome
2 - Cpf
3 - Idade""")
        atualizacao = input().lower()
        if (atualizacao == "nome" or atualizacao == "1"):
            print("Digite o novo nome:")
            novoNome = input().capitalize()
            posicaoCliente = listaDividida.index(cliente)
            listaDividida.pop(posicaoCliente)
            listaDividida.insert(posicaoCliente, novoNome)
            print(listaDividida)
            arquivoNovo = ""
            acumulador = 1
            for linha in listaDividida:
                arquivoNovo += linha
                arquivoNovo += " "
                if(acumulador % 3 == 0):
                    arquivoNovo += "\n"
                acumulador += 1
            print("Cliente atualizado")
            with open('projeto//clientes.txt', "w")as arquivoCliente:
                arquivoCliente.write(arquivoNovo)
            break
        elif (atualizacao == "cpf" or atualizacao == "2"):
            print("Digite o novo cpf:")
            novoCpf = input().capitalize()
            posicaoCliente = listaDividida.index(cliente)
            posicaoCpf = posicaoCliente + 1
            listaDividida.pop(posicaoCpf)
            listaDividida.insert(posicaoCpf, novoCpf)
            print(listaDividida)
            arquivoNovo = ""
            acumulador = 1
            for linha in listaDividida:
                arquivoNovo += linha
                arquivoNovo += " "
                if(acumulador % 3 == 0):
                    arquivoNovo += "\n"
                acumulador += 1
            print("Cliente atualizado")
            with open('projeto//clientes.txt', "w")as arquivoCliente:
                arquivoCliente.write(arquivoNovo)
            break
        elif (atualizacao == "idade" or atualizacao == "3"):
            print("Digite a nova idade:")
            novaIdade = int(input())
            posicaoCliente = listaDividida.index(cliente)
            posicaoIdade = posicaoCliente + 2
            listaDividida.pop(posicaoIdade)
            listaDividida.insert(posicaoIdade, str(novaIdade))
            print(listaDividida)
            arquivoNovo = ""
            acumulador = 1
            for linha in listaDividida:
                arquivoNovo += linha
                arquivoNovo += " "
                if(acumulador % 3 == 0):
                    arquivoNovo += "\n"
                acumulador += 1
            print("Cliente atualizado")
            with open('projeto//clientes.txt', "w")as arquivoCliente:
                arquivoCliente.write(arquivoNovo)
            break
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuClientes())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
    return

def excluirCliente():
    while(True):
        with open('projeto//clientes.txt', "r") as arquivo:
            listaClientes= arquivo.readlines()
            for linhas in listaClientes:
                print(linhas, end="")
        listaStr = ""
        for i in listaClientes:
            listaStr += i
        listaDividida = listaStr.split()
        print("Quem você deseja excluir?")
        cliente = input().capitalize()
        posicaoCliente = listaDividida.index(cliente)
        for i in range(3):
            listaDividida.pop(posicaoCliente)
        arquivoNovo = ""
        acumulador = 1
        for linha in listaDividida:
            arquivoNovo += linha
            arquivoNovo += " "
            if(acumulador % 3 == 0):
                arquivoNovo += "\n"
            acumulador += 1
        print("Cliente excluído")
        with open('projeto//clientes.txt', "w") as arquivoClientes:
            arquivoClientes.write(arquivoNovo)
        break
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuClientes())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")    
def excluirProduto():
    while(True):
        with open('projeto//estoque.txt', "r") as arquivo:
            listaEstoque= arquivo.readlines()
            for linhas in listaEstoque:
                print(linhas, end="")
        listaStr = ""
        for i in listaEstoque:
            listaStr += i
        listaDividida = listaStr.split()
        print("O que você deseja excluir?")
        produto = input().lower()
        posicaoEstoque = listaDividida.index(produto)
        for i in range(3):
            listaDividida.pop(posicaoEstoque)
        arquivoNovo = ""
        acumulador = 1
        for linha in listaDividida:
            arquivoNovo += linha
            arquivoNovo += " "
            if(acumulador % 3 == 0):
                arquivoNovo += "\n"
            acumulador += 1
        print("Excluído!")
        with open('projeto//estoque.txt', "w") as arquivoClientes:
            arquivoClientes.write(arquivoNovo)
        break
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuEstoque())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")  
def excluirVenda():
    while(True):
        with open('projeto//vendas.txt', "r") as arquivo:
            listaVendas= arquivo.readlines()
            for linhas in listaVendas:
                print(linhas, end="")
        print("")
        print("Qual linha você deseja excluir?")
        produto = int(input())
        itemVendas = produto - 1
        itemRemovido = listaVendas[itemVendas]
        listaVendas.pop(itemVendas)
        print("Excluído!")
        listaStr = " ".join(listaVendas)
        with open('projeto//vendas.txt', "w") as arquivo2:
            arquivo2.write(listaStr)
        with open('projeto//estoque.txt', "r") as rEstoque:
            estoque = rEstoque.readlines()
        listaStr = ""
        for i in estoque:
            listaStr += i
        listaDividida2 = listaStr.split()
        listaItemR = itemRemovido.split()
        produto = listaItemR[1]
        indiceProduto = listaDividida2.index(produto)
        indiceEstoque = indiceProduto + 2
        valorEstoque = listaDividida2[indiceEstoque]
        valorVendido = listaItemR[3]
        valorFinal = str(int(valorEstoque) + int(valorVendido))
        listaDividida2[indiceEstoque] = valorFinal
        arquivoNovo2 = ""
        acumulador2 = 1
        for linha2 in listaDividida2:
            arquivoNovo2 += linha2
            arquivoNovo2 += " "
            if(acumulador2 % 3 == 0):
                arquivoNovo2 += "\n"
            acumulador2 += 1
        with open('projeto//estoque.txt', "w") as novoEstoque:
            novoEstoque.write(arquivoNovo2)
        break
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuVendas())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
    return           
def atualizarEstoque():
    while(True):
        with open('projeto//estoque.txt', "r") as arquivo:
            listaClientes= arquivo.readlines()
            for linhas in listaClientes:
                print(linhas, end="")
        listaStr = ""
        for i in listaClientes:
            listaStr += i
        listaDividida = listaStr.split()
        print("Qual produto você deseja atualizar?")
        produto = input().lower()
        print("""O que você deseja atualizar?
1 - Sabor
2 - Preço
3 - Quantidade""")
        atualizacao = input().lower()
        if (atualizacao == "sabor" or atualizacao == "1"):
            print("Digite o novo sabor:")
            novoSabor= input().lower()
            posicaoSabor = listaDividida.index(produto)
            listaDividida.pop(posicaoSabor)
            listaDividida.insert(posicaoSabor, novoSabor)
            arquivoNovo = ""
            acumulador = 1
            for linha in listaDividida:
                arquivoNovo += linha
                arquivoNovo += " "
                if(acumulador % 3 == 0):
                    arquivoNovo += "\n"
                acumulador += 1
            print("Item atualizado!")
            with open('projeto//estoque.txt', "w")as arquivoCliente:
                arquivoCliente.write(arquivoNovo)
            break
        elif(atualizacao == "2" or atualizacao == "preco") :
            print("Digite o novo preço:")
            novoPreco = input().lower()
            posicaoSabor = listaDividida.index(produto)
            posicaoPreco = posicaoSabor + 1
            listaDividida.pop(posicaoPreco)
            listaDividida.insert(posicaoPreco, novoPreco)
            arquivoNovo = ""
            acumulador = 1
            for linha in listaDividida:
                arquivoNovo += linha
                arquivoNovo += " "
                if(acumulador % 3 == 0):
                    arquivoNovo += "\n"
                acumulador += 1
            print("Item atualizado!")
            with open('projeto//estoque.txt', "w")as arquivoCliente:
                arquivoCliente.write(arquivoNovo)
            break
        elif (atualizacao =="3" or atualizacao == "quantidade"):
            print("Digite a nova quantidade:")
            novaQtd = int(input())
            posicaoSabor = listaDividida.index(produto)
            posicaoQtd = posicaoSabor + 2
            listaDividida.pop(posicaoQtd)
            listaDividida.insert(posicaoQtd, str(novaQtd))
            arquivoNovo = ""
            acumulador = 1
            for linha in listaDividida:
                arquivoNovo += linha
                arquivoNovo += " "
                if(acumulador % 3 == 0):
                    arquivoNovo += "\n"
                acumulador += 1
            print("Item atualizado!")
            with open('projeto//estoque.txt', "w")as arquivoCliente:
                arquivoCliente.write(arquivoNovo)
            break
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuEstoque())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
    return
def atualizarVendas():
    while(True):
        with open('projeto//vendas.txt', "r") as arquivo:
            listaVendas= arquivo.readlines()
            for linhas in listaVendas:
                print(linhas, end="")
        print("")
        print("Qual linha você deseja atualizar?")
        produto = int(input())
        itemVendas = listaVendas[produto - 1]
        print("""O que você deseja atualizar?
1 - Produto
2 - Vendidos""")
        listaDividida = itemVendas.split()
        opcao = input().lower()
        if (opcao == "produto" or opcao == "1"):
            print("Digite o novo produto:")
            novaQtd= input().lower()
            antigoProduto = listaDividida[1]
            listaDividida.pop(1)
            listaDividida.insert(1, novaQtd)
            listaNova = ""
            acumulador = 1
            for linha in listaDividida:
                listaNova += linha
                listaNova += " "
                if(acumulador == 10):
                    listaNova += "\n"
                acumulador += 1
            listaVendas.pop(produto - 1)
            listaVendas.insert(produto - 1, listaNova)
            arquivoNovo = "".join(listaVendas)
            print("Venda atualizada!")
            with open('projeto//vendas.txt', "w")as arquivoCliente:
                arquivoCliente.write(arquivoNovo)
            with open('projeto//estoque.txt', "r") as rEstoque:
                estoque = rEstoque.readlines()
            listaStr = ""
            for i in estoque:
                listaStr += i
            qtdInicial = listaDividida[3]
            listaDividida2 = listaStr.split()
            posicaoProduto2 = listaDividida2.index(antigoProduto)
            posicaoEstoqueInicial = posicaoProduto2 + 2
            valorEstoque = listaDividida2 [posicaoEstoqueInicial]
            valorNovo = str((int(valorEstoque) + int(qtdInicial)))
            listaDividida2[posicaoEstoqueInicial] = valorNovo
            posicaoProduto3 = listaDividida2.index(novaQtd)
            posicaoEstoqueInicial3 = posicaoProduto3 + 2
            valorEstoque3 = listaDividida2 [posicaoEstoqueInicial3]
            valorNovo3 = str((int(valorEstoque3) - int(qtdInicial)))
            listaDividida2[posicaoEstoqueInicial3] = valorNovo3         
            arquivoNovo2 = ""
            acumulador2 = 1
            for linha2 in listaDividida2:
                arquivoNovo2 += linha2
                arquivoNovo2 += " "
                if(acumulador2 % 3 == 0):
                    arquivoNovo2 += "\n"
                acumulador2 += 1
            with open('projeto//estoque.txt', "w") as novoEstoque:
                novoEstoque.write(arquivoNovo2)
            break
        elif(opcao == "2" or opcao == "vendidos"):
            print("Digite quantos foram vendidos:")
            produto1 = listaDividida[1]
            novaQtd= int(input())
            preco = listaDividida[5]
            qtdInicial = listaDividida[3]
            listaDividida.pop(3)
            listaDividida.insert(3, str(novaQtd))
            listaDividida.pop(8)
            listaDividida.insert(8, str(novaQtd * float(preco)))            
            listaNova = ""
            acumulador = 1
            for linha in listaDividida:
                listaNova += linha
                listaNova += " "
                if(acumulador == 10):
                    listaNova += "\n"
                acumulador += 1
            listaVendas.pop(produto - 1)
            listaVendas.insert(produto - 1, str(listaNova))
            arquivoNovo = "".join(listaVendas)
            print("Venda atualizada!")
            with open('projeto//vendas.txt', "w")as arquivoCliente:
                arquivoCliente.write(arquivoNovo)
            #fazer com que ele tire do estoque a diferença na atualização
            with open('projeto//estoque.txt', "r") as rEstoque:
                estoque = rEstoque.readlines()
            listaStr = ""
            for i in estoque:
                listaStr += i
            listaDividida2 = listaStr.split()
            posicaoProduto2 = listaDividida2.index(produto1)
            posicaoEstoqueInicial = posicaoProduto2 + 2
            valorEstoque = listaDividida2 [posicaoEstoqueInicial]
            valorFinal = str((int(valorEstoque) + int(qtdInicial)) - novaQtd)
            listaDividida2[posicaoEstoqueInicial] = valorFinal
            arquivoNovo2 = ""
            acumulador2 = 1
            for linha2 in listaDividida2:
                arquivoNovo2 += linha2
                arquivoNovo2 += " "
                if(acumulador2 % 3 == 0):
                    arquivoNovo2 += "\n"
                acumulador2 += 1
            with open('projeto//estoque.txt', "w") as novoEstoque:
                novoEstoque.write(arquivoNovo2)
            break
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuVendas())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
    return           
def cadastrarCliente():
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
        if (cpfVerificado and (idade >= 18) and (nome.isalpha()) == True):
            print("Cadastro concluido")
            with open('projeto//clientes.txt', "a")as arquivo:
                arquivo.write(f"{nome} {cpf} {idade}\n")
            break
        elif(len(cpfCorreto) <11 and idade < 18):
            print("O CPF está incompleto e é menor de idade")
        elif (len(cpfCorreto) <11):
            print("O cpf está incompleto")
        elif(idade < 18):
            print("É menor de idade")
        elif(nome.isalpha() != True):
            print("Digite um nome")

        print("""1 - Continuar
2 - Voltar
""")
        while(True):
            op = input().lower()
            if (op == "2" or op == "voltar"):
                return(menuClientes())
            elif(op == "1" or op== "continuar"):
                break
            else:
                print("Digite uma opção")
        
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuClientes())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção")
    return

def listaClientes():
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
            return(menuClientes())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
    return
       
def cadastrarProduto():
    while(True):
        print("Digite o produto:")
        produto = str(input().lower())
        print("Digite o preço:")
        precoProduto = float(input())
        print("Digite a quantidade do produto:")
        qtdProduto = int(input())
        if (qtdProduto > 10 and precoProduto > 0):
            with open('projeto//estoque.txt', "a") as arquivo:
                arquivo.write(f"{produto} {precoProduto} {qtdProduto}\n")
                print("Produto cadastrado")
                break
        else:
            print("O produto não pode ser cadastrado ")
        print("")
        print("""1 - Continuar
2 - Voltar
""")
        while(True):
            op = input().lower()
            if (op == "2" or op == "voltar"):
                return(menuEstoque())
            elif(op == "1" or op== "continuar"):
                break
            else:
                print("Digite uma opção")

    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuEstoque())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
    return
       
def relatorioVendasTotal():
    with open('projeto//vendas.txt', "r") as arquivoVendas:
        listaVendas = arquivoVendas.readlines()
    listaStr = ""
    for i in listaVendas:
        listaStr += i
    listaDividida = listaStr.split()
    acumulador = 1
    valorTotal = 0
    for j in listaDividida:
        acumulador += 1
        if (acumulador % 10 == 0):
            valorTotal += float(j)
    print("")
    print(f"O valor total das vendas foi: {valorTotal} reais")
    print("")
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuVendas())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
    return
def estoque():
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
            return(menuEstoque())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção:")
    return
       
def cadastrarVenda():
    while(True):
        with open('projeto//estoque.txt', "r") as arquivo:
            listaProdutos= arquivo.readlines()
            for linhas in listaProdutos:
                print(linhas, end="")
        listaStr = ""
        for i in listaProdutos:
            listaStr += i
        listaDividida = listaStr.split()
        print("Qual produto foi vendido?")
        produto = input().lower()
        if (produto in listaDividida):
            posicaoProduto = listaDividida.index(produto)
            posicaoEstoque = posicaoProduto + 2
            qtdEstoque = listaDividida[posicaoEstoque]
            posicaoValor = posicaoProduto + 1
            precoProduto = listaDividida[posicaoValor]
            if (int(qtdEstoque) <= 0):
                print("O produto acabou")
            elif(int(qtdEstoque) > 0):
                print("Quantos foram vendidos?")
                vendidos = int(input())
                listaDividida.pop(posicaoEstoque)
                listaDividida.insert(posicaoEstoque, str(int(qtdEstoque) - vendidos))
                arquivoNovo = ""
                acumulador = 1
                for linha in listaDividida:
                    arquivoNovo += linha
                    arquivoNovo += " "
                    if(acumulador % 3 == 0):
                        arquivoNovo += "\n"
                    acumulador += 1
                print("Venda cadastrada")
                with open('projeto//estoque.txt', "w") as novoEstoque:
                    novoEstoque.write(arquivoNovo)
                with open('projeto//vendas.txt', "a") as vendas:
                    vendas.write(f"Produto: {produto} ,Vendidos: {vendidos} ,Valor: {precoProduto} ,Valor total: {float(precoProduto) * vendidos} reais\n")
                break
        else:
            print("o produto não está cadastrado")
        print("""Deseja cadastrar outra venda?
1 - sim          
2 - não""")
        while(True):
            opcao = input().lower()
            if (opcao == "sim" or opcao == "1"):
                break
            elif(opcao == "2" or opcao == "não" or opcao == "nao"):
                return(menuVendas())
            else:
                print("Digite uma opção")
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuVendas())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção")
    return   
def relatorioVendas():
    print("Relatório de vendas:")
    with open('projeto//vendas.txt', "r") as vendas:
        linha = vendas.readlines()
        for linhas in linha:
            print(linhas, end = "")
    print("""Deseja voltar para o menu?
1- Sim
2- Não""")
    while(True):
        voltar = input().lower()
        if (voltar == "1" or voltar == "sim"):
            return(menuVendas())
        elif(voltar == "2" or voltar == "não" or voltar == "nao"):
            print("Você saiu!")
            break
        else:
            print("Digite uma opção")
    return

with open('projeto//clientes.txt', "r") as arquivoClientes:
    listaDeClientes = arquivoClientes.readlines()
with open('projeto//estoque.txt', "r") as arquivoEstoque:
    listaDeClientes = arquivoEstoque.readlines()
with open('projeto//vendas.txt', "r") as arquivoVendas:
    listaDeClientes = arquivoVendas.readlines()
menu()
