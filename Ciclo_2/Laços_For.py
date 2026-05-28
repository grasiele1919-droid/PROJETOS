Produtos= ["caderno", "caneta", "lapis", "borracha", "régua"]
Preços= (30.00, 9.90, 5.90, 3.90, 15.00)
Quantidades= [9,3,3,1,1]
subtotais = []

#ANTES USAVAMOS #preco = preços [0]
#produto = produtos[0]
#print (f"O produto é {Produto}, custa R$ {Preco}.")

for indice, produto in enumerate (Produtos):
    precos = Preços [indice]
    quantidade = Quantidades [indice]
    subtotal = quantidade * precos
    subtotais.append(subtotal)

    #print(f""" Sua compra foi de {quantidade} de {produto}, valor unitario de R$ {precos}.O subtotal foi de R$ {subtotal}.""")
    
    mensagem = f"""
    ________________________________
    Produto: {produto}
    Quantidade: {quantidade}
    Valor unitário: R${precos}
    Sobtotal:R${subtotal}
    ________________________________
    """
    print (mensagem)


total = sum (subtotais)

print (f"Seu pedido total foi de R${total}.")






