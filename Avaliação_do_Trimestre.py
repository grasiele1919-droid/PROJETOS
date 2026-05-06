print ("Digite as notas dos 3 trimestre")
Nota1= float(input("nota 1: "))
Nota2= float(input("nota 2: "))
Nota3= float(input("nota 3: "))

Total = Nota1 + Nota2 + Nota3
Média = Total / 3

if Média <= 5:
    print("Reprovado, sua média é: ", Média)

elif Média > 5 and Média <= 7:
    print ("Recuperação, sua média é: ", Média)

elif Média > 7 and Média <= 10:
    print("Aprovado, sua média é: ", Média)

else:
    print("Não coresponde a nota de 0 a 10")