#WHILE =  enquanto ______ (for vedadeiro segue em repetição)( condições variaveis)
#entrada

#usuario_correto recebe "admin"
usuario_correto = "admin"
#senha_correto recebe "1234"
senha_correta = "1234"

#usuario recebe " "
usuario = ""
senha = ""

#ENQUANTO usuario é diferente de usuario_correto ou senha é diferente de senha_correta:
while usuario != usuario_correto or senha != senha_correta:
    #entrada "Digite o usuario: "
    usuario = input("Digite o usuario: ")
    #senha "Digite a senha: "
    senha = input("Digite o senha: ")

    #SE usuario é diferente de usuario_correto ou senha é diferente de senha_correta:
    if usuario != usuario_correto or senha != senha_correta:
        print("Usuario ou senha invalido, tente novamente...")

    else:
        print("Acesso Liberado...")
