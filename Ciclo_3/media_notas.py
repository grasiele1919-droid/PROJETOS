import math

def calcular_media(notas:list)-> float:
    media = sum(notas) / len(notas)
    return media

contador = 1
notas = []
while True:
    nota = float(input(f"Digite a nota{contador} ou 'sair' para sair: "))
    notas.append(notas)
    print(" Nota foi registrada!")
    if nota == "sair":
        break

calcular_media
