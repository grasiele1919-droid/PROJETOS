class Alunos:
    def __init__(self, nome, nota:float):
        self.nome = nome
        self.nota = nota

    def exibir(self):
        print(f"Nome:{self.nome} | Nota:{self.nota}")

    def situacao(self):
        if self.nota >= 6:
            print("Aprovado")
        else:
            print("Reprovado")
        

aluno_1 = Alunos("Ana", 8.5)
aluno_2 = Alunos("Bruno", 6)


aluno_1.exibir()
aluno_1.situacao()
aluno_2.exibir()
aluno_2.situacao()


