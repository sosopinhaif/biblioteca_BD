import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor() 

def adicionar_usuario():
    name = input("nome de usuario: ")
    
    cursor.execute("INSERT INTO usuarios(nome) VALUES(?)", (name,))

    conn.commit()
    print("ADD com sucesso!!!")

def liste_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    if not usuarios:
        print("nenhum user foi encontrado!;(")
        return 
    for usuario in usuarios:
        print(f"ID: {usuario[0]} | nome: {usuario[1]}")
