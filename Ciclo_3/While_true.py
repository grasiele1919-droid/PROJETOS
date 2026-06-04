def	exibir_menu():
	print("-----Menu-----")
	print("1 - Primeira opção")
	print("0 - Sair")

while True:
	#mostra o menu
	exibir_menu()
#entrada do usuario
	opcao = input("Escolha: ")
	#saida
	if opcao =="0":
		print("saindo do programa")
		break
	elif opcao =="1":
		print("primeira_opcao()")
	else:
		print("Opção Invalida!")
