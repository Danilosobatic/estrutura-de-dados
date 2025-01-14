import os

# Função para criar um usuário
def criar_usuario(nome):
    try:
        # Abre o arquivo 'usuarios.txt' no modo de leitura ('r') para verificar os IDs existentes.
        with open('usuarios.txt', 'r') as f:
            usuarios = f.readlines()
            
            if usuarios:
                # Pega o maior ID do arquivo e adiciona 1.
                ultimo_id = max([int(line.split(',')[0]) for line in usuarios])
                id_usuario = ultimo_id + 1
            else:
                id_usuario = 1  # Se o arquivo estiver vazio, começa com o ID 1
    except FileNotFoundError:
        # Caso o arquivo não exista, cria o arquivo com o ID inicial como 1.
        id_usuario = 1

    # Agora, abre o arquivo em modo de adição ('a') e escreve o novo usuário.
    with open('usuarios.txt', 'a') as f:
        f.write(f'{id_usuario},{nome}\n')
    
    # Exibe uma mensagem informando que o usuário foi adicionado com sucesso.
    print(f"Usuário {nome} adicionado com sucesso.")

# Função para ler todos os usuários
def ler_usuarios():
    try:
        # Abre o arquivo 'usuarios.txt' no modo de leitura ('r')
        with open('usuarios.txt', 'r') as f:
            usuarios = f.readlines()
        
        if not usuarios:
            print("Nenhum usuário encontrado.")
        else:
            print("Usuários cadastrados:")
            for usuario in usuarios:
                id_usuario, nome = usuario.strip().split(',')
                print(f"ID: {id_usuario}, Nome: {nome}")
    
    except FileNotFoundError:
        print("Erro: O arquivo 'usuarios.txt' não foi encontrado.")

# Função para atualizar um usuário
def atualizar_usuario(id_usuario, novo_nome):
    try:
        with open('usuarios.txt', 'r') as f:
            usuarios = f.readlines()
        
        usuario_encontrado = False
        for i, usuario in enumerate(usuarios):
            id_arquivo, nome = usuario.strip().split(',')
            if id_arquivo == str(id_usuario):
                usuarios[i] = f'{id_usuario},{novo_nome}\n'
                usuario_encontrado = True
                break
        
        if usuario_encontrado:
            # Escreve as mudanças de volta no arquivo
            with open('usuarios.txt', 'w') as f:
                f.writelines(usuarios)
            print(f"Usuário ID {id_usuario} atualizado para {novo_nome}.")
        else:
            print(f"Usuário com ID {id_usuario} não encontrado.")
    
    except FileNotFoundError:
        print("Erro: O arquivo 'usuarios.txt' não foi encontrado.")

# Função para deletar um usuário
def deletar_usuario(id_usuario):
    try:
        with open('usuarios.txt', 'r') as f:
            usuarios = f.readlines()
        
        usuario_encontrado = False
        for i, usuario in enumerate(usuarios):
            id_arquivo, nome = usuario.strip().split(',')
            if id_arquivo == str(id_usuario):
                usuarios.pop(i)
                usuario_encontrado = True
                break
        
        if usuario_encontrado:
            # Escreve as mudanças de volta no arquivo
            with open('usuarios.txt', 'w') as f:
                f.writelines(usuarios)
            print(f"Usuário ID {id_usuario} deletado com sucesso.")
        else:
            print(f"Usuário com ID {id_usuario} não encontrado.")
    
    except FileNotFoundError:
        print("Erro: O arquivo 'usuarios.txt' não foi encontrado.")

# Menu interativo para o CRUD de usuários
def menu():
    while True:
        print("\nEscolha uma operação:")
        print("1. Criar usuário")
        print("2. Ler usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        
        escolha = input("Digite o número da operação: ")

        if escolha == '1':
            nome = input("Digite o nome do usuário: ")
            criar_usuario(nome)
        elif escolha == '2':
            ler_usuarios()
        elif escolha == '3':
            try:
                id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
                novo_nome = input("Digite o novo nome do usuário: ")
                atualizar_usuario(id_usuario, novo_nome)
            except ValueError:
                print("Erro: ID inválido.")
        elif escolha == '4':
            try:
                id_usuario = int(input("Digite o ID do usuário a ser deletado: "))
                deletar_usuario(id_usuario)
            except ValueError:
                print("Erro: ID inválido.")
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
