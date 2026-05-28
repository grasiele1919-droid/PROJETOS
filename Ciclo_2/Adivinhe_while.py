import random
numero_secreto = random.randint(1,10)
palpite = 0
tentativas = 0
#precisa colocar 0 para não corre o risco de dar erro e finalizar o codigo sem chegar


while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (1 a 10): "))

    if palpite != numero_secreto:
        print("Errou! Tente novamente.")
        
    tentativas = tentativas +1

print (f"Parabêns! Acertou na {tentativas} tentativa.")    