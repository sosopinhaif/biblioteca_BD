
from ADD_usuario import adicionar_usuario, liste_usuarios

while(True):
    print("" \
    "-----MENU-----" \
    "" \
    "1-ADICIONAR USUARIO" \
    "2-LISTAR USUARIO" \
    "")

    opcao = input("qual opção vc escolhe? ")

    if opcao == "1":
        adicionar_usuario()

    elif opcao == "2":
        liste_usuarios()
