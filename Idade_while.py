idade = -1
tentativas = -1

while idade <0 or idade > 120:
    idade = int(input("Digite a idade válida (0 a 120): "))

    if idade <0 or idade > 120:
        print("Errou! Idade invalida, tente novamente.")

tentativas = tentativas +1

print (f"Obrigada! A idade digitada digitada é {idade}. Acertou na {tentativas} tentativa.")     
