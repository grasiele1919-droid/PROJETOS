""" opção operações e sair
#pedir 2 numero aposescolha operação
#Calcular e exibir resultado
#tratar a divisão
#exibir aviso p/ opcao invalida
#Repetir o menu até o usuario sair."""

while True:
    mensagem = f"""
    ====Calculadora====
    1 - Soma (+)
    2 - Subtração (-)
    3 - Multiplicação (x)
    4 - Divisão (/)
    0 - Sair
    """
    print (mensagem)

    opcao = input("Escolha a opção de operação: ")
    if opcao == "0": 
        break #quebra o codigo PARA

    if opcao not in ["1","2","3","4"]:  #not in - não deixa o usuario digitar texto diferente do que definido
        print ("Opção inválida! Tente novamente...")
        continue    #continue - Segue o fluxo

    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    if opcao == "1": 
        calculo = int(n1 + n2)
        print(f"{n1} + {n2} = {calculo}")
    elif opcao == "2":
        calculo = int(n1 - n2)
        print(f"{n1} - {n2} = {calculo}")
    elif opcao == "3":
        calculo = int(n1 * n2)
        print(f"{n1} x {n2} = {calculo}")
    elif opcao == "4":
        if n2 == 0: print("Não é possivel dividir")
        else: print(f"{n1} / {n2} = {round(n1 / n2,2)}")