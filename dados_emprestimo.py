import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela livros
conn.execute("DROP TABLE IF EXISTS emprestimos")

#cria a tabela emprestimos
sql_create = """
    CREATE TABLE emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER REFERENCES usuarios(id),
        data DATE DEFAULT CURRENT_DATE)
"""
conn.execute(sql_create)

#insere registro na tabela
sql_insert = """
    INSERT INTO emprestimos (usuario_id) VALUES (1)
"""

conn.execute(sql_insert)
conn.commit()
