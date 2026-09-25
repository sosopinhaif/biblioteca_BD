import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

def add_cadastro_de_livro():
    emprestimo_cadastro= int(input("qual o id do seu emprestimo? "))
    livro_cadastro= int(input("digite o id do seu livro agora: "))

    cursor.execute("INSERT INTO emprestimos_livros(emprestimo_id , livro_id) VALUES(?,?)",
                   (emprestimo_cadastro,
                    livro_cadastro,))
    
    conn.commit()
    print("seu livro esta cadastrado no emprestimo! :D")