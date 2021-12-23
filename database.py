import sqlite3

#conecta ao banco de dados "todo-data"
conn = sqlite3.connect("todo-data.db")

def criar_tabela():
    """cria a tabela 'tarefas'  caso ela não exista"""
    cursor = conn.cursor()
    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS tarefas (
            id_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
            tarefa TEXT,
            concluido BOOLEAN DEFAULT 0
        )
    """
    )
    
def add_tarefa(tarefa):
    """add nova tarefa"""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (tarefa) VALUES ('{}')".format(tarefa))
    conn.commit()
    
def remover_tarefa(id_tarefa):
    """remove uma tarefa da tabela"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id_tarefa = {}".format(id_tarefa))
    conn.commit()

def concluir_tarefa(id_tarefa):
    """marce tarefa como concluida"""
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluido = 1 WHERE id_tarefa = {}".format(id_tarefa))
    conn.commit()

def get_tarefas():
    """retorna a lista de tarefas cadastradas"""
    cursor = conn.cursor()
    return cursor.execute("SELECT id_tarefa, tarefa, concluido FROM tarefas")
    