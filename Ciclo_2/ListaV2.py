Produtos= ["caderno", "caneta", "lapis", "borracha", "régua"]
Preços= (30.00, 9.99, 5.90, 3.99, 15.00)

print("Lista completa de produtos: ", Produtos)
print("Primeiro produto da lista: ", Produtos[0]) 
print("Último produto da lista: ", Produtos[-1])
print("Quantidade de produtos na lista: ", len(Produtos))

print(f"O produto {Produtos[0]}, custa R${Preços[0]}.")

#para remover:
Produtos.remove (Produtos[-1])
Preços.remove (Preços[-1])


# para somar o preço de todos os produtos:
total= sum(Preços)
print(f"O total deu R$ {total}.")


# logica condicional IF/else para desconto:
if total <100:
    exit()

else:
    desconto= 0.95
    c= total * desconto
    print(f"O total agora com descontoé de R${total}.")