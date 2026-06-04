import math

def calcular_media(notas:list) -> float:
    media = sum(notas) / len(notas) # SUM vai somar as notas e LEN vai contar o numero de notas
    return math.ceil (media) # RETURN - devolve o resultado

contador = 1
notas = []

while True:
    nota = float(input(f"Digite a nota {contador} ou -1 para Sair: "))
    notas.append(notas)

    print(" Nota foi registrada!")
    if nota == "-1":
        break

media = calcular_media (notas )
print(f" A media foi de, {media}.")

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")