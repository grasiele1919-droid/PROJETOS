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
def deposito():
        valor = float(input("Digite quanto deseja depositar: R$ "))
        saldo_total = saldo + valor
        print(f"Deposito feito de R$ {valor}.")
        
def sacar():
      

saldo = 0.0

while True:
    menu_deposito()
    deposito = input("Digite uma opção: ")
        
    if deposito == "0":
        print("Saindo...")
        break
    elif deposito == "1": deposito()