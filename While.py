while True:
    mensagem: (f"""
Menu:
1 - ver situação 1
2 - ver situação 2
3 - Sair
""")
    print (mensagem)

    opcao = input ("escolha uma opção: ")
    if opcao == "1":
        print("Tente novamente...")

    elif opcao == "2":
        print("Errou, tente novamente...")

    elif opcao == "3":
        print ("Saindo do sistema...")
        break

    else: 
        print ("Opção invalida. tente novamente")