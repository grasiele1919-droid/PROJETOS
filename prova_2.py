# loja automativa venda de produtos e serviços 
# usario quer produtos ou serviços?
# lista de serviços e lista de produtos com preços
# exibe final usuario escolhe o quer comprar.


#lista de produtos
#lista de preço produtos
#lista serviços
#lista de serviços
#recebe do usuario produto ou serviço
#exibe a lista de venda
#recebe do usuario item de compra
#exibe para usuario o item de compra com preço

produtos = ["óleo", "peças", "pneu"]
precos_produtos = (75.00, 500.00, 799.90)
servicos = ["lavação", "troca óleo", "troca pneus" ]
precos_servicos = (150.00, 249.90, 599,99)

compra = input("Você deseja ver nossos Produtos ou Serviços? ")

if produtos == "produtos":
    for posicao_produto, produto in enumerate(produtos):
        produto = produtos [posicao_produto]
        preco_produto = precos_produtos[posicao_produto]

    mesagem1 = f"""
________________________
Produto:{produto}
Posição produto: {posicao_produto}
Preço do produto:{preco_produto} 
"""
    print(mesagem1)

else:
    print("Opcao invalida, tente novamente...")

if servicos == "servicos":
    for posicao_servico,servico in enumerate(servicos):
        servico = servico[posicao_servico]
        preco_servico = precos_servicos[posicao_servico]

    mesagem2 = f"""
________________________
Serviço:{servico}
Posição produto: {posicao_servico}
Preço do produto:{preco_produto} 
"""
    print(mesagem2)

else:
    print("Opcao invalida, tente novamente...")




 



