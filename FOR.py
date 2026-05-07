Frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

Fruta_favorita = input("Qual é a sua fruta favorita? ")

#SE a fruta favorita NÃO ESTA na lsita frutas
if Fruta_favorita not in frutas:
    print ("Sua fruta favorita não esta na lista!")
    print("Adicionando...")
    frutas.append(Fruta_favorita)

    #exit é para parar encerrar o programa, ou seja, não executa mais nada depois disso
    exit()

#PARA cada posiçao (indice) e fruta NA lista numerada
for posicao, fruta in enumerate(frutas):
    # faça isso:
    #SE a fruta dessa interação é igual a fruta favorida

    if fruta == Fruta_favorita
    # Salva numa nova variavel a posição dessa iteração
    
    posicao_fruta_favorita = posicao

    #Quebra o for (faz ele parar)
    break

#saida do algoritmo(print)

print(f"Minha fruta favorita está na posição indice {posicao_fruta_favorita}")