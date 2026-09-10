import sqlite3
from datetime import datetime

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela livros
conn.execute("DROP TABLE IF EXISTS emprestimos_livros")

#cria a tabela emprestimos
sql_create = """
    CREATE TABLE emprestimos_livros (emprestimo_id INTEGER REFERENCES emprestimos(id),
        livro_id INTEGER REFERENCES livros(id),
        data_devolucao DATE,
        PRIMARY KEY (emprestimo_id, livro_id))
    """
conn.execute(sql_create)

#insere registro na tabela
sql_insert = """
    INSERT INTO emprestimos_livros (emprestimo_id, livro_id, data_devolucao) VALUES (?, ?, ?)
"""

#gerando uma data
data_string = "12/09/2026"
objeto_data = datetime.strptime(data_string, "%d/%m/%Y")
conn.execute(sql_insert, (1, 1, objeto_data.isoformat()))
conn.commit()