print("== LOGIN / LOGOUT ==")
pilha_login = []

def mostrar_usuario(usuario):
    print(f"Usuário logado: {usuario['nome']} | Email: {usuario['email']}")

while True:
    acao = input("Digite 'login', 'logout' ou 'sair': ").lower()
    if acao == 'login':
        nome = input("Digite o nome de usuário: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")
        usuario = {"nome": nome, "email": email, "senha": senha}
        pilha_login.append(usuario)
        print("Login realizado com sucesso.\n")
    elif acao == 'logout':
        if pilha_login:
            saiu = pilha_login.pop()
            print(f"{saiu['nome']} fez logout.\n")
        else:
            print("Nenhum usuário logado.\n")
    elif acao == 'sair':
        break
    else:
        print("Comando inválido.\n")
