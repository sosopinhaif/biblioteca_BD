
from ADD_usuario import adicionar_usuario, liste_usuarios 
from ADD_autores import cadastro_autores, liste_autores
from ADD_editoras import cadastro_editora, liste_Editoras
from ADD_livros import cadastrar_livro, listar_livros

while(True):
    print("")
    print("-----MENU-----" )
    print("" )
    print("1-ADICIONAR USUARIO" )
    print("2-LISTAR USUARIO" )
    print("3-CADASTRAR AUTOR")
    print("4-LISTAR AUTORES")
    print("5-CADASTRAR EDITORA")
    print("6-LISTAR EDITORA")
    print("7-CADASTRAR LIVRO")
    print("8-LISTAR LIVROS")
    print("9-CADASTRAR EMPRESTIMO")
    print("10-LISTAR EMPRESTIMOS")
    print("")
    
    opcao = input("qual opção vc escolhe? ")

    if opcao == "1":
        adicionar_usuario()

    elif opcao == "2":
        liste_usuarios()

    elif opcao == "3":
        cadastro_autores()    

    elif opcao == "4": 
        liste_autores() 
  
    elif opcao == "5":
        cadastro_editora()    

    elif opcao == "6": 
        liste_Editoras() 
    
    elif opcao == "7":
        cadastrar_livro()

    elif opcao == "8":
        listar_livros()    