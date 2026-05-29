"""
def  calcular_media (notas)
calcula a media de uma lista de notas
:param notas: lista de numeros(ex.[7,8,9])
:return: retono 
"""

def somar(n1,n2):   #defina soma(n1,n2):
    total=  n1 + n2     #total recebe n1 + n2
    print(f"{n1} + {n2} = {total}")

def subtrair(n1,n2):
    total=  n1 - n2
    print(f"{n1} - {n2} = {total}")     

def multiplicar(n1,n2):
    print(f"{n1} * {n2} = {n1*n2}")      

def divisão(n1,n2):
    if n2 == 0: print("Não é possivel dividir")
    else: 
        print(f"{n1} / {n2} = {n1 /n2}")      


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
        break #querbra o codigo PARA

    if opcao not in ["1","2","3","4"]:  #not in - não deixa o usuario digitar texto diferente do que definido
        print ("Opção inválida! Tente novamente...")
        continue    #continue - Segue o fluxo

    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    if opcao == "1": somar(n1,n2)
    elif opcao == "2": subtrair(n1,n2)       
    elif opcao == "3": multiplicar(n1,n2)
    elif opcao == "4": divisão(n1,n2)