import util.funcoes as fd

opcao = '0'
produtos = []
id:int = 0

while True:
    print('== Bem Vindo ao Sistema de Controle de Estoque ==\n')

    print('_MENU_\n')

    print('1-Adicionar Produto')
    print('2-Visualisar Produtos')
    print('3-Atualizar Produto')
    print('4-Remover Produto')
    print('5-Salvar e Carregar Produto')
    print("6-Sair do Programa\n")

    opcao = str(input('Escolha uma das opções: \n'))
    print("\n")

    if opcao == '1':
        id += 1
        produtos = fd.AddProduto(produtos,id)

    elif opcao == '2':
        escolha = input("Deseja ver 'Todos' ou por 'Categoria' ? T/C: ").strip().lower()
        if escolha == "t":
            fd.GetAllProdutos(produtos)
        else:
            fd.GetByCategoria(produtos)

    elif opcao == '3':
        prod_Id = int(input("Informe a Id do produto: "))
        resultado = fd.UpdateProduto(produtos,prod_Id)
        print(resultado)

    elif opcao == '4':
        prod_Id = int(input("Informe a Id do produto: "))
        resultado = fd.DeleteProduto(produtos,prod_Id)
        print(resultado)

    elif opcao == '5':
        resultado = fd.SaveJsonFile(produtos)
        print("\n",resultado)

        if len(produtos) == 0:
            produtos = fd.LoadProdutos(produtos)
            # Verifiva o valor maximo no campo Id na lista carregada, e atribui à varivel 'id' para continuar o sequencial do produto.
            #Se caso estiver vazia ele atribui o valor defaut que é 0.
            id = max([produto["Id"] for produto in produtos], default=0)
            print("Produtos carregados com sucesso!\n")
        else:
            print("\nPara carregar produtos a lista de produtos tem que esta vazia!") 

    elif opcao == '6':
        print("Saindo do programa.")
        break

    else:
        print("\nOpção invalida!\n")
    
    continuar = input("\nDeseja retornar ao menu principal? (s/n): ").strip().lower()
    if continuar != "s":
        print("Saindo do programa.")
        break
        