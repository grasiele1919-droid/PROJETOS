class Produtos:
    def __init__(self, nome:str, preco:float, qnt: int):
        self.nome = nome
        self.preco = preco
        self.qnt = qnt

    def exibir(self):
        print(f"Produto:{self.nome} | Preço:{self.preco} |Qantidade:{self.qnt}")

produto_1 = Produtos(nome="arroz", preco=7.0, qnt=10) #("arroz", 7.0, 10)
produto_2 = Produtos("feijão", 4.0, 8)

produto_1.exibir()
