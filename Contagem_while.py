contador = 0
#(variavel) contador recebe 0
numero = -1
#numero recebe -1

while numero != 0:
#enquanto o usuário não digitar 0

    numero = int(input("Digite um número: "))
    # pergunte "digite um numero " e converta para inteiro

    if numero != 0:
    #se numero for diferente de 0
        print ("Tente novamente...")

        contador += 1
        #CONTADOR recebe CONTADOR +1

print(f"Voce digitou: {numero}. Acertou na {contador} tentativa")
#exibe a mensagem de saida, ""
