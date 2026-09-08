import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("CREATE TABLE emprestimo (id INTERGER PRIMARY KEY AUTOINCREMENT," \
              )