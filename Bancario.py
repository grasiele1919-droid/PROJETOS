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
        valor = float(input("Digite quanto deseja depositar: R$ "))
        saldo += valor
        print(f"Deposito feito de R$ {valor}.")
        return saldo

def sacar(saldo):
        saque = float(input("Digite o valor que desaja sacar: R$ "))

        if saque <= saldo:
            saldo -= saque
            print(f" Valor sacado de R$ {saque}")
            return saldo
        else:
            print("Saldo insuficiente")
      
def mostrar_saldo(saldo):
      print (F"Saldo total de R$ {saldo}")
      
saldo = 0.0

while True:
    menu_deposito()
    opcao = input("Digite uma opção: ")
        
    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1": saldo = deposito(saldo)
    elif opcao == "2": saldo = sacar (saldo)
    elif opcao == "3": mostrar_saldo(saldo)
    else:
          print("Opção invalida")
