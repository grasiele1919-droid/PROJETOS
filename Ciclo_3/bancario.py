def menu_deposito():
        msg = f"""
    ++++ Menu de Deposito ++++
    1 - Depositar
    2 - Sacar
    3 - Ver saldo
    0 - Sair
    +++++++++++++++++++++++++ 
    """
        print(msg)

def deposito(saldo):
        valor = float(input("Digite valor que deseja depositar: R$ "))
        saldo += valor #(saldo = saldo + valor)
        print(f"Depósito de R$ {valor} realizado.")
        return saldo

def sacar(saldo):
        saque = float(input("Digite o valor que deseja sacar: R$ "))
        if saque > saldo:
            print("Saldo insuficiente")
            return saldo #devolve o saldo atualizado para o escopo global.
        saldo -= saque
        print(f" Valor sacado é de R$ {saque}.")
        return saldo          
      
def mostrar_saldo(saldo):
      print (F"Saldo total de R$ {saldo}")
      
saldo = 0.0

while True:
    menu_deposito()
    opcao = input("Digite uma opção: ")
        
    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1": saldo = deposito(saldo) #return no saldo ela vai atualizar do local para a variavel global
    elif opcao == "2": saldo = sacar (saldo)
    elif opcao == "3": mostrar_saldo(saldo)
    else:
          print("Opção invalida")