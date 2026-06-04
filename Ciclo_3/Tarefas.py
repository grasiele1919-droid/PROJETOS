""" Caderno de tarefas - as tarefas ficam em uma lista. Cada opção chama uma função que recebe essa
lista como parametro para adionar, listar e remover.
1 adcionar (pede um texto e adiona a lista)
2 listar (mostra as tarefas niumeradas)
3 remover (remove pela posição informada)
0 sair (encerra o programa)
"""

def menu_tarefas():
        msg = f"""
    ++++ Menu de tarefas ++++
    1 - Adicionar uma tarefa
    2 - Listar as tarefas
    3 - Remover tarefa
    0 - Sair
    +++++++++++++++++++++++++
    """
        print(msg)

def adicionar(tarefas):
    tarefa = input("Adicione a tarefa:")
    tarefas.append(tarefa)
    print("Adicionando tarefa...")

def listar(tarefas):
    if not tarefas:
        print("Não há tarefas para exibir")
    else:
        for posicao, tarefa in enumerate(tarefas, start = 1): #Start é para comecar apartir do numero que colocar depois.
            print(f"{posicao} - {tarefa}")

def remover(tarefas):
    if not tarefas:
        print("Não há tarefas para remover: ")
    else:
        tarefa = int(input("Digite o número da tarefa que desaja remover"))
        if tarefa >0 and tarefa <= len(tarefas):
            tarefa.pop (tarefa - 1) #pop - remove e salva o item removido ex:lista_removida = tarefa.pop(tarefa)
            print("Tarefa Removida!")
   
tarefas = []

while True:
   menu_tarefas()
   opcao = input("Digite a opção desejada: ")

   if opcao == "0":
    print("saindo...")
    break
   elif opcao =="1": adicionar(tarefas)
   elif opcao =="2": listar(tarefas)
   elif opcao =="3": remover(tarefas)
   




