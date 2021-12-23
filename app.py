import database
import mensagem 

def main():
    NOVA_TAREFA = 1
    CONCLUIR_TAREFA = 2
    REMOVER_TAREFA = 3
    
    while True:
        mensagem.exibir_menu()
        mensagem.exibir_tarefas()
        
        try:
            opcao = int(input(" O que deseja fazer? 1 -> Add Nova Tarefa, 2 -> Concluir Tarefa, 3 -> Remover Tarefa => "))
            
            if opcao == NOVA_TAREFA:
                mensagem.mostrar_opcao_add_tarefa()
                
            elif opcao == CONCLUIR_TAREFA:
                mensagem.mostrar_opcao_concluir_tarefa()
                
            elif opcao == REMOVER_TAREFA:
                mensagem.mostrar_opcao_deletar_tarefa()
                
            else:
                print("Opção não reconhecida, informe uma opção valida")
            
        except ValueError as e:
            print("Opção não reconhecida, informe uma opção valida")
        
        

if __name__ == "__main__":
    database.criar_tabela()
    main()  