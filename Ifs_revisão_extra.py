velocidade = int(input("Digite a velocidade do carro:"))

if velocidade >0 and velocidade <=60:
    print("Andando dentro do limite.")
elif velocidade >60 and velocidade <=80:
    print("acima da velocidade, multa leve")
elif velocidade >80:
    print("acima da velocidade, multa gravissima")
elif velocidade == 0:
    print("Veiculo parado.")
else:
    print("Numero digitado invalido")