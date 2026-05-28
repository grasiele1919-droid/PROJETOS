#recebe lista de numeros
numeros =[1,3,5,6,40]

#total da soma dos numeros
total = sum(numeros)

#quantida de elementos da lista
tamanho_lista = len(numeros)

#Se qunatidade for maior que 4
if len(numeros) >= 4:
    print(total)

#Senão
else:
    print("Insira mais elementos")


#resultado da soma
print (f"Soma total dos numeros é {total}")

