"""
Sistema de Biblioteca Pessoal
Crie um programa para gerenciar uma pequena biblioteca pessoal utilizando os conceitos básicos de Orientação a Objetos.

Objetivo
Permitir que o usuário cadastre livros e visualize os livros cadastrados."""

class Livros():
    def __init__(self, titulo, autor, ano_de_publicacao:int):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao

    def exibir(self):
        print(f"Titulo:{self.titulo} | Autor:{self.autor} | Ano de Publicação: {self.ano_de_publicacao}")

def exibir_menu():
    msg = (f"""
    +++++++++++++++++++
    1 - Cadastrar Livro
    2 - Listar livro
    0 - Sair
    """)
    print(msg)

def cadastrar_livro():
    print("Cadastrando Livro...")
    titulo = input("Digite Titulo do livro: ")
    autor = input("Digite autor do livro: ")
    ano = int(input("Digite ano de publicação: "))
    livro = Livros(titulo, autor, ano)
    livros.append(livro)

def exibir_lista():
    if not livros:
        print("Não há livros cadastrados")
        return
    for livro in livros:
        print("_______________________")
        livro.exibir()    
        
livros = []
while True:
    exibir_menu()
    opcao = input("Digite uma opção: ")

    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1": cadastrar_livro()
    elif opcao == "2": exibir_lista()
    else:
        print("Opção invalida!")
    



