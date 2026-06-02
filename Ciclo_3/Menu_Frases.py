def exibe_menu():
    print (f"\n =========")
    print (f"---MENU---")
    print ("1 Saudação")
    print ("2 Sobre")
    print ("3 Ajuda")
    print ("0 Sair")
    print ("==========")

def saudacao (): # não precisa colocar variavel dentro dos parenteses.
    nome = input ("Digite seu nome:")
    print(f"Bem Vindo ao curso, {nome}!")
def sobre():
    print(f"Curso Python")
def ajuda ():
    print(f"Procure a coordenador do curso.")


while True:
    exibe_menu()
    opcao = input("Digite a opção escolhida: ")

    if opcao == "1": saudacao()
    elif opcao == "2": sobre()
    elif opcao == "3": ajuda()
    elif opcao == "0": 
        break
    else:
        print("Opção inválida!")
