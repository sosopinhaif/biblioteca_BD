import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

def cadastro_autores():
    name = input("qual autor vc deseja cadastrar? ")

    cursor.execute("INSERT INTO autores(nome) VALUES(?)", (name,))

    conn.commit()

    print("autor cadastrado com sucesso!!:p")

def liste_autores():
    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()
    if not autores:
        print("nenhum autor foi encontrado!;(")
        return 
    for autor in autores:
        print(f"ID: {autor[0]} | nome: {autor[1]}")      