Usuario_correto = "admin"
senha_correto = "1234"
#armazenamneto do dado correto

usuario = input("Usuario: " )
senha = int(input("senha: "))
#entrada dos dados

if usuario == Usuario_correto and senha_correto:
    #igual ==
    print ("Acesso liberado")

else:
    print("Usuario ou senha incorretos")





