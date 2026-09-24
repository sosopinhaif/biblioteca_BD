import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

def cadastrar_autor():
    nome = input("Digite o nome do autor: ")

    cursor.execute(
        "INSERT INTO autores (nome) VALUES (?)",
        (nome,)
    )

    conn.commit()

    print("Autor cadastrado com sucesso!")


def listar_autores():
    cursor.execute("SELECT * FROM autores")

    autores = cursor.fetchall()

    if not autores:
        print("Nenhum autor cadastrado.")
        return

    for autor in autores:
        print(f"ID: {autor[0]} | Nome: {autor[1]}")

def cadastrar_livro():

    titulo = input("Digite o título: ")
    autor_id = int(input("Digite o ID do autor: "))
    editora_id = int(input("Digite o ID da editora: "))
    ano = int(input("Digite o ano de publicação: "))
    edicao = int(input("Digite a edição: "))

    disponivel = int(input("Disponível? (1 - Sim / 0 - Não): "))

    cursor.execute("""
        INSERT INTO livros
        (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        titulo,
        autor_id,
        editora_id,
        ano,
        edicao,
        disponivel
    ))

    conn.commit()

    print("Livro cadastrado com sucesso!")
def listar_livros():

    cursor.execute("""
        SELECT 
            livros.id,
            livros.titulo,
            autores.nome,
            editoras.nome,
            livros.ano_publicacao,
            livros.edicao,
            livros.disponivel
        FROM livros
        JOIN autores
            ON livros.autor_id = autores.id
        JOIN editoras
            ON livros.editora_id = editoras.id
    """)

    livros = cursor.fetchall()

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:

        disponibilidade = "Sim" if livro[6] == 1 else "Não"

        print(
            f"\nID: {livro[0]}"
            f"\nTítulo: {livro[1]}"
            f"\nAutor: {livro[2]}"
            f"\nEditora: {livro[3]}"
            f"\nAno: {livro[4]}"
            f"\nEdição: {livro[5]}"
            f"\nDisponível: {disponibilidade}"
        )