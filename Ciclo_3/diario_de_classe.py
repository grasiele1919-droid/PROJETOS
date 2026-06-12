''' alunis ficam em uma lista de objetos.
Um menu while true permite lançar notas a um aluno ja cadatsrado -  e cada nova nota recalcula a media dele'''


class Aluno:
    def __init__(self, nome, notas=[]):
        self.nome = nome
        self.notas = notas


    def exibir(self):
        print(f"Aluno:{self.nome}")
        if self.notas:
            for ordem_nota, nota in enumerate(self.notas,1):
                print(f"Nota n n{ordem_nota}: {nota}")

    def situacao(self):
        #somar self.nota e fazer o calculao da media e por fim dizer se esta aprovado ou reprovado
        nota = len(notas)


        if self.nota >= 6:
            print("Aprovado")
        else:
            print("Reprovado")

def exibir_menu():
    msg = (f"""
    +++++++++++++++++++
    1 - Cadastrar Aluno
    2 - Lançar notas
    3 - Ver situação
    4 - Listar Alunos
    0 - Sair
    """)
    print(msg)

def cadastrar_aluno():
    nome = input("Digite nome do Aluno: ")
    aluno = Aluno(nome)
    alunos.append(aluno)
    print(f"Cadastrando Aluno {nome} com sucesso...")

def cadastrar_nota():
    indice = int(input("Digite o código do aluno: "))
    aluno  =alunos[indice]
    nota = float(input("Digite a nota para ser lançado:"))
    aluno.notas.append(nota)

    
    nota = input("Digite nota do Aluno: ")
    notas = Aluno(nota)
    nota.append(notas)

    nota = input("Digite nota do aluno: ")
    print("Cadastrando Nota...")
        

alunos=[]
