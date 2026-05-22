#FOR =Sabe quando termina, tem contatdor automatico. Usados em listas contagens fixas

# #ENTRADA
# #produtos recebe
produtos=["arroz", "feijão","farinha","macarrão", "oleo"]
#recebe Preços
preços = [5.9, 9.0, 4.59, 7.99, 6.90]

#PROCESSAMENTO
#for exige que exista variavel e um fim

#para cada PRODUTO em PRODUTOS:                   (INICIO,FIM, PASSO) OU ([],PASSO)
#para cada POSIÇÃO(variavel 1) de PRODUTO(variavel 2) EM PRODUTOS ENUMERADOS:
for posição_produto, produto in enumerate(produtos):
 #SE o valor da posição do preços é menos que 10:
    if preços[posição_produto] < 10:
        #preço atualizado recebe o valor da posição de preços
        preço_atualizado = round(preços[posição_produto] * 1.10,2)
    
        mensagem = f"""
        _________________________________________
        Produto: {produto}
        Preço:R${preços[posição_produto]}
        Reajuste com + 10%: R$ {preço_atualizado}
        """
        print (mensagem)


    #FIM
    #exibe produto, preços [posição] + 10% reajuste
    #print(f"Produto: {produto}, custa R$ {preços[posição_produto]}, com mais 10% de reajuste ficará R$ {preço_atualizado}.")

#ENUMERATE - Consegue inumerar a posição o item na lista

