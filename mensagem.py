import database

MENU = 99

def exibir_menu():
    """imprime menu no terminal"""
    colunas = 60
    print("#" * colunas)
    print("{:^60}".format("TAREFAS"))
    print("#" * colunas)
    print("{:^60}".format("digite 99 para voltar para o menu inicial, [CTRL+C] sai do menu"))
    print("#" * colunas)
    
def exibir_tarefas():
    """exibi as tarefas cadastadas"""
    for tarefa in database.get_tarefas():
        concluido = "concluido" if tarefa[2] == 1 else ""
        t = "- [{:>1}] {:<47} {:<10}".format(tarefa[0], tarefa[1], concluido)
        print(t)
        
    print("#" * 60)
    
def mostrar_opcao_add_tarefa():
    texto_nova_tarefa = input("Descreva a Tarefa: ")
    print("add tarefa -> " + str(texto_nova_tarefa))
    if texto_nova_tarefa != str(MENU):
        database.add_tarefa(texto_nova_tarefa)
        
def mostrar_opcao_concluir_tarefa():
    id_tarefa = int(input("Qual tarefa deseja concluir? (digite o id da tarefa): "))
    print("Concluindo a tarefa -> " + str(id_tarefa))
    if id_tarefa != MENU:
        database.concluir_tarefa(id_tarefa)
        
def mostrar_opcao_deletar_tarefa():
    id_tarefa = int(input("Qual tarefa deseja remover? (digite o id da tarefa): "))
    print("Removendo a tarefa -> " + str(id_tarefa))
    if id_tarefa != MENU:
        database.remover_tarefa(id_tarefa)