class Produtos:
    def __init__(self, nome:str, preco:float, qnt: int):
        self.nome = nome
        self.preco = preco
        self.qnt = qnt

    def exibir(self):
        print(f"Produto:{self.nome} | Preço:{self.preco} |Quantidade:{self.qnt}")

def exibir_menu():
    print("____________________")
    print("1 - Cadastro de produtos")
    print("2 - Exibir produtos")
    print("0 - Sair")
    print("____________________")

def cadastrar_produtos():
    print("\n CADASTRANDO PRODUTO...")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qnt = int(input("Digite o quantidade do produto: "))
    produto = Produtos(nome,preco, qnt)
    produtos.append(produto)

def exibir_produtos():
    if not produtos:
        print("Não há produtos cadastrados")
        return
    for produto in produtos:
        print("---------------------------")
        produto.exibir()

produtos = []
while True:
    exibir_menu()
    opcao = input("Escolha a opção: ")

    if opcao == "0":
        break
    elif opcao =="1":cadastrar_produtos()
    elif opcao =="2": exibir_produtos()
    else:
        print("Opção invalida!")

