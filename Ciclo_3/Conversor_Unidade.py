def menu_conversor():
    msg = f"""
        ===== Menu =====
        1 - Celsus -> Fahrenheit
        2 - Reais -> Dolar
        3 - Horas -> Minutos
        0 - Sair
        ==============="""
    print (msg)

def temperatura():
    Celsus = int(input ("Digite tempertura Celsus: "))
    print(f"\nTemperatura de {Celsus} graus Celsus em Fahrenheit é {round(Celsus * 1.8 + 32)}.")

def dinheiro():
    reais = float(input ("Digite quantidade de reais: "))
    print(f"\nQuantidade de {reais} reais em dolar é {round(reais /5.0)}.")

def tempo():
    horas = float(input ("Digite as horas: "))
    print(f"\nA hora de {horas} horas em minutos é {horas *60}.")

while True:
    menu_conversor()
    opcao = input ("Digite uma opção: ")

    if opcao == "0":
        break
    elif opcao == "1": temperatura()
    elif opcao == "2": dinheiro()
    elif opcao == "3": tempo ()
    else:
        print("Opção inválida!")

