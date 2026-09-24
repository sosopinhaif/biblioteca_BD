import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

def cadastro_editora():
    name = input("qual é a editora? ")

    cursor.execute("INSERT INTO editora(nome) VALUES(?)", (name,))

    conn.commit()

    print("editora cadastrada com sucesso!!;p")

def liste_Editoras():
    cursor.execute("SELECT * FROM editora")
    editoras = cursor.fetchall()
    if not editoras:
        print("nenhuma editora foi encontrada!;(")
        return 
    for editora in editoras:
        print(f"ID: {editora[0]} | nome: {editora[1]}")      