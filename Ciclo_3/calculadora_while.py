# 4 opção operações e sair
#pedir 2 numero aposescolha operação
#Calcular e exibir resultado
#tratar a divisão
#exibir aviso p/ opcao invalida
#Repetir o menu até o usuario sair.


while True:
    mensagem = f"""
    ====Calculadora====
    1 - Soma (+)
    2 - Subtração (-)
    3 - Multiplicação (*)
    4 - Divisão (/)
    0 - Sair
    """
    print (mensagem)

    opcao = input("Escolha a opção de operação: ")
    if opcao == "0": break
    if opcao not in ["1","2","3","4"]:
        print ("Opção inválida! Tente novamente...")
        continue

    N1 = int(input("Digite o primeiro numero: "))
    N2 = int(input("Digite o segundo numero: "))

    if opcao == "1": 
        calculo = int(N1 + N2)
        print(f"{N1} + {N2} = {calculo}")
    elif opcao == "2":
        calculo = int(N1 - N2)
        print(f"{N1} - {N2} = {calculo}")
    elif opcao == "3":
        calculo = int(N1 * N2)
        print(f"{N1} * {N2} = {calculo}")
    elif opcao == "4":
        if N2 == 0: print( "Não é possivel dividir")
        else: print(f"{N1} / {N2} = {N1 / N2}")