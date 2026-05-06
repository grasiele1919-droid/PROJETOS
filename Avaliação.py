Avaliação = int(input("Digite a nota do aluno:"))

if Avaliação <= 5:
    print("Reprovado")

elif Avaliação > 5 and Avaliação <= 7:
    print ("Recuperação")

elif Avaliação > 7 and Avaliação <= 10:
    print("Parabêns, superou as expectativas")

else:
    print("Não coresponde a nota de 0 a 10")