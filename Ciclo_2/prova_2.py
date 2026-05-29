"""
loja automativa venda de produtos e serviços 
usario quer produtos ou serviços?
lista de serviços e lista de produtos com preços
exibe final usuario escolhe o quer comprar.
"""

"""
lista de produtos
lista de preço produtos
lista serviços
lista de serviços
recebe do usuario produto ou serviço
exibe a lista de venda
recebe do usuario item de compr
desconto de 10% pedidos acima R$300
exibe para usuario o item de compra com preço"""

produtos = ["óleo 5W40", "Carburador", "pneu ARO 20"]
precos_produtos = (75.00, 500.00, 799.90)

servicos = ["lavação", "troca óleo", "troca pneus" ]
precos_servicos = (150.00, 249.90, 599.99)

compra = input("Você deseja ver nossos produtos ou servicos? ")
if compra == "produtos":
    for posicao_produto, produto in enumerate(produtos):
        preco_produto = round(precos_produtos[posicao_produto],2)

        mesagem1 = f"""
CODIGO do produto: {posicao_produto}
Produto: {produto}
Preço do produto: R${preco_produto}
________________________
"""
        print(mesagem1)

    pedido = int(input("Digite o codigo do produto que deseja: "))
    produto_escolhido = produtos[pedido]
    preço_produto_escolhido = precos_produtos[pedido]
    if preço_produto_escolhido >=300:
        desconto1 = round(precos_produtos[pedido] - (precos_produtos[pedido] * 0.1), 2)

        mensagem_produto = f"""
________________________
CUPOM FISCAL
Produto: {produto_escolhido}
Preço: R$ {preço_produto_escolhido}
Pedido acima de R$300.00, desconto de 10%
Total pedido: R$ {desconto1}
________________________
"""
        print(mensagem_produto)
    else:
        mensagem_produto2 = f"""
________________________
CUPOM FISCAL
Produto: {produto_escolhido}
Total pedido: R$ {preço_produto_escolhido}
________________________
"""
        print(mensagem_produto2)

elif compra == "servicos":
    for posicao_servico,servico in enumerate(servicos):
        preco_servico = round(precos_servicos[posicao_servico],2)

        mesagem_2 = f"""
CODIGO servico: {posicao_servico}
Serviço: {servico}
Preço do servico: R${preco_servico} 
________________________
"""
        print(mesagem_2)

    pedido1 = int(input("Digite o codigo do serviço que deseja: "))
    servico_escolhido = servicos[pedido1]
    preco_servico_escolhido = precos_servicos[pedido1]
    
    if preco_servico_escolhido >=300:
        desconto2 = round(precos_servicos[pedido1]-(precos_servicos[pedido1] * 0.1), 2)

        mensagem_servico1 = f"""
________________________
CUPOM FISCAL
Serviço: {servico_escolhido}
Preço: R${preco_servico_escolhido}
Pedido acima de R$300.00, desconto de 10%
Total pedido: R$ {desconto2}
________________________
"""
        print(mensagem_servico1)
    else:
        mensagem_servico2 = f"""
________________________
CUPOM FISCAL
Serviço: {servico_escolhido}
Total pedido: R${preco_servico_escolhido}
________________________
"""
        print(mensagem_servico2)

else:
    print("Opcao invalida, tente novamente...")
    exit()