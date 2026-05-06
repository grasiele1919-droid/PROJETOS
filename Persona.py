Pessoa = int(input("Digite a idade da pessoa:"))

if Pessoa <=10:
    print("Criança")

elif Pessoa < 10 and Pessoa >= 18:
    print("Adolecente")

elif Pessoa < 18 and Pessoa >=60:
    print("Adulto")

else:
    print("Idoso")