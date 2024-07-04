import json

# Adiciona um produto
def AddProduto(produtos:list,id:int):
    data = {} # Cada produdo fica em um dicionario.

    data['Id'] = id
    data['Nome'] = str(input('Informe a descrição do produto :')).upper()
   
    while True: #Validação para se informar valor diferente de real
        try:
            data['Quantidade'] = float(input('Informe a quantidade: '))
            break  # Sai do loop se a conversão for aceita
        except ValueError:
            print("Quantidade inválida. Por favor, informe um número válido.")

    while True:
        try:
            data['Preco'] = float(input('Informe o preço: '))
            break # Sai do loop se a conversão for aceita
        except ValueError:
            print("Preço inválido. Por favor, informe um valor válido.")
        
    data['Categoria'] = str(input('Informe a categoria: ')).upper()

    produtos.append(data) # Adiciona o dicionario a lista

    print('\nProduto cadastrado com Sucesso!\n')

    return produtos # Retorna a lista com os dicinarios adicionados.

#Selecionar todos os produtos da lista.
def GetAllProdutos(produtos:list):
    
    if(len(produtos) > 0): #Verifica se a lista não esta vazia.

        for item in produtos: #Imprime cada item dentro da lista.
            print(f"ID: {item['Id']}")
            print(f"NOME: {item['Nome']}")
            print(f"QUANTIDADE: {item['Quantidade']:.2f}".replace('.',','))
            print(f"PREÇO: {item['Preco']:.2f}".replace('.',','))
            print(f"CATEGORIA: {item['Categoria']}")
            print("=======================================\n")       
    else:
        print('Nenhum produto encontrado.')

#Seleciona por categoria
def GetByCategoria(produtos:list):
    if len(produtos) > 0:
        print("Escolha a categoria:\n")
        categorias = set(item['Categoria'] for item in produtos) #Cria um Set que só aceita valor unico para as categorias.

        for categoria in categorias: #mostras as categorias unicas.
            print(f">>> {categoria}")
            
        categoria = input().upper()
        achou = False

        print("\n")

        for item in produtos: #Percorre a lista procurando os itens com a categoria escolhida.
            if item['Categoria'] == categoria:
                print(f"ID: {item['Id']}")
                print(f"NOME: {item['Nome']}")
                print(f"QUANTIDADE: {item['Quantidade']:.2f}".replace('.',','))
                print(f"PREÇO: {item['Preco']:.2f}".replace('.',','))
                print(f"CATEGORIA: {item['Categoria']}")
                print("=======================================\n") 
                achou = True 
        if not achou: #Se caso o usario errar o nome, ele imprime a mensagem.
            print("Categoria não encontrada") 
    else:
        print('Nenhum produto encontrado.')

# Atuliza um produto pela Id.
def UpdateProduto(produtos:list,id:int):
    
    for item in produtos: # Verifica cada item dentro da lista.
        
        if id == item['Id']: # Se o valor do item no campo Id for igual a id passada ele irá editar.
            item['Nome'] = str(input('Informe a descrição do produto :')).upper()
            item['Quantidade'] = float(input('Informe a quantidade: '))
            item['Preco'] = float(input('Informe o preço: '))
            item['Categoria'] = str(input('Informe a categoria: ')).upper()

            return "\nProduto atualizado com sucesso!"
                      
    return '\nProduto não encontrado'

# Deletar um produto.
def DeleteProduto(produtos:list,id:int):
    for item in produtos:
       
        if id == item['Id']: # Verifica se o produto existe para deletar .
            produtos.remove(item)

            return f"Produto {item['Nome']} removido com Sucesso!"      
    return  'Produto não encontrado'   

#Criar Arquivo Json com os produtos.
def SaveJsonFile(produtos:list):  
    if(len(produtos)>0): #verifica se a lista não esta vazia. 
        #Cria o arquivo e salva as informações, o 'w' siginifica write = escrever.
        with open('Produtos.json','w') as file:
            json.dump(produtos,file,indent=4) # Ident = 4  para melhorar a visaulização do json
            return "Arquivo gerado com Sucesso."
                
    return "Nenhum produto para gravar"

#Carregando produtos do arquivo Json.
def LoadProdutos(produtos:list):
    
    try: #Aqui ele tenta ler o arquivo json.
        #Ler o arquivo e passa as informaçoes para a lista, o 'r' siginifica read = ler.
        with open('Produtos.json','r') as file:
            produtos = json.load(file)
            return produtos
    except FileNotFoundError:
        return []
    