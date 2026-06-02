def	exibi_menu():
	print("-----Menu-----")
	print("1 - Primeira opção")
	print("0 - Sair")

while True:
	#mostra o menu
	exibi_menu()
#entrada do usuario
	opção = input("Escolha: ")
	#saida
	if opção =="0":
	    break
	elif opção =="1":
		print("primeira_opcao()")
	else:
		print("Opção Invalida!")
