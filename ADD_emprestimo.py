import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

def cadastro_emprestimo():

    usuario_id = int(input("Digite o ID do usuário: "))

    cursor.execute(
        "INSERT INTO emprestimos (usuario_id) VALUES (?)",
        (usuario_id,)
    )

    conn.commit()

    print("Empréstimo cadastrado com sucesso! ;p")
def listar_emprestimos():

    cursor.execute("""
        SELECT 
            emprestimos.id,
            usuarios.nome,
            emprestimos.data
        FROM emprestimos
        JOIN usuarios
            ON emprestimos.usuario_id = usuarios.id
    """)

    emprestimos = cursor.fetchall()

    if not emprestimos:
        print("Nenhum empréstimo cadastrado.")
        return

    for emprestimo in emprestimos:
        print(
            f"ID: {emprestimo[0]} | "
            f"Usuário: {emprestimo[1]} | "
            f"Data: {emprestimo[2]}"
        )
