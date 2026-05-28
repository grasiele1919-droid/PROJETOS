nomes = ["Daniel", "Ana", "João", "Maria"]
notas = [7,9,10,5.9]
frequencias = [80, 50, 90, 49,]

#para cada
for posicao_nome, nome in enumerate(nomes):
    nota = notas[posicao_nome]
    frequencia = frequencias[posicao_nome]

    if nota >= 7 and frequencia >=75:
        print (f"{nome} passou")

    elif nota <7 and frequencia <75:
        print(f"{nome} reprovado")
    
    else:
        print(f"{nome} reprovado")




