#ENTRADA
# #produos recebe
produtos=["arroz", "feijão","farinha","macarrão", "oleo"]
#recebe Preços
preços = [5.9, 9.0, 4.59, 7.99, 6.90]

#PROCESSAMENTO
#for exige que exista variavel e um fim

#para cada PRODUTO em PRODUTOS:                   (INICIO,FIM, PASSO) OU ([],PASSO)
#para cada POSIÇÃO(variavel 1) de PRODUTO(variavel 2) EM PRODUTOS ENUMERADOS:
for posição_produto, produto in enumerate(produtos):

    #FIM
    #exibe produto, preços [posição]
    print(f"Produto: {produto}, custa R$ {preços[posição_produto]}.")

#ENUMERATE - Consegue inumerar a posição o item na lista

