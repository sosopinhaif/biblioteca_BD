import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()

for linhas in resultados:
    print(f"id: {linhas[0]} | nome:{linhas[1]} ")

cursor.execute("SELECT * FROM autores")
cursor.execute("SELECT * FROM editoras")

conn.close()
