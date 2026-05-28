produtos = ["óleo 5W40", "Carburador", "pneu ARO 20"]
precos_produtos = (75.00, 500.00, 799.90)

servicos = ["lavação", "troca óleo", "troca pneus" ]
precos_servicos = (150.00, 249.90, 599.99)

compra = input("Você deseja ver nossos produtos ou servicos? ")

if compra == "produtos":
    for codigo, produto in enumerate(produtos):
        preco_produto = round(precos_produtos[codigo],2)
        mesagem1 = f"""
CODIGO do produto: {codigo}
Produto: {produto}
Preço do produto: R${preco_produto}
________________________
"""
        print(mesagem1)

elif compra == "servicos":
    for codigo, servico in enumerate(servicos):
        preco_servico = round(precos_servicos[codigo],2)
        mesagem_2 = f"""
CODIGO servico: {codigo}
Serviço: {servico}
Preço do servico: R${preco_servico} 
________________________
"""
        print(mesagem_2)
else:
    print("Opção invalida...")
    exit()

codigo = int(input(f"Digite o codigo do {compra} que deseja: "))

