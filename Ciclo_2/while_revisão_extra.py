import time
tanque = int(input("Digite quantidade de agua atual no tanque: "))
tempo_escoamento = 5
tempo_total_escoamento = 0

print("Tanque atual: ")

while tanque >0:
    print("Escoando 25 litros...")
    tanque = tanque -25
    tempo_total_escoamento = tempo_escoamento + tempo_escoamento

    print ("Tanque atual:", tanque )
print(f"Tempo total que levou para escoar os {tanque} litros foi de {tempo_total_escoamento}.")
