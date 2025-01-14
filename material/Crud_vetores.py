# Lista para armazenar os usuários
usuarios = []

# Função para criar um usuário
def criar_usuario(nome):
    # Determina o ID do novo usuário com base no tamanho da lista de usuários
    id_usuario = len(usuarios) + 1
    
    # Cria um dicionário representando o usuário e adiciona à lista
    usuario = {'id': id_usuario, 'nome': nome}
    usuarios.append(usuario)
    
    # Exibe uma mensagem informando que o usuário foi adicionado com sucesso.
    print(f"Usuário {nome} adicionado com sucesso.")

# Função para ler todos os usuários
def ler_usuarios():
    # Verifica se a lista de usuários está vazia
    if not usuarios:
        print("Nenhum usuário encontrado.")  # Caso não haja usuários, exibe mensagem
    else:
        # Caso existam usuários, imprime todos os dados
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}")

# Função para atualizar um usuário
def atualizar_usuario(id_usuario, novo_nome):
    # Flag para verificar se o usuário foi encontrado
    usuario_encontrado = False
    # Percorre todos os usuários procurando pelo ID
    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            usuario['nome'] = novo_nome  # Atualiza o nome do usuário
            usuario_encontrado = True  # Marca como encontrado
            break  # Interrompe o loop após encontrar o usuário
    
    # Se o usuário foi encontrado, exibe mensagem de sucesso
    if usuario_encontrado:
        print(f"Usuário ID {id_usuario} atualizado para {novo_nome}.")
    else:
        print(f"Usuário com ID {id_usuario} não encontrado.")  # Caso o ID não seja encontrado

# Função para deletar um usuário
def deletar_usuario(id_usuario):
    # Flag para verificar se o usuário foi encontrado
    usuario_encontrado = False
    # Percorre todos os usuários procurando pelo ID
    for i, usuario in enumerate(usuarios):
        if usuario['id'] == id_usuario:
            usuarios.pop(i)  # Remove o usuário da lista
            usuario_encontrado = True  # Marca como encontrado
            break  # Interrompe o loop após encontrar o usuário
    
    # Se o usuário foi encontrado, exibe mensagem de sucesso
    if usuario_encontrado:
        print(f"Usuário ID {id_usuario} deletado com sucesso.")
    else:
        print(f"Usuário com ID {id_usuario} não encontrado.")  # Caso o ID não seja encontrado

# Menu interativo para o CRUD de usuários
def menu():
    while True:
        # Exibe as opções de operação
        print("\nEscolha uma operação:")
        print("1. Criar usuário")
        print("2. Ler usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        
        # Lê a escolha do usuário
        escolha = input("Digite o número da operação: ")

        # Operação de criação de usuário
        if escolha == '1':
            nome = input("Digite o nome do usuário: ")
            criar_usuario(nome)
        # Operação de leitura de usuários
        elif escolha == '2':
            ler_usuarios()
        # Operação de atualização de usuário
        elif escolha == '3':
            try:
                id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
                novo_nome = input("Digite o novo nome do usuário: ")
                atualizar_usuario(id_usuario, novo_nome)
            except ValueError:
                print("Erro: ID inválido.")  # Caso o ID informado não seja um número
        # Operação de deleção de usuário
        elif escolha == '4':
            try:
                id_usuario = int(input("Digite o ID do usuário a ser deletado: "))
                deletar_usuario(id_usuario)
            except ValueError:
                print("Erro: ID inválido.")  # Caso o ID informado não seja um número
        # Operação para sair do programa
        elif escolha == '5':
            print("Saindo do programa...")
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")  # Caso o usuário digite uma opção inválida

# Executa o menu quando o script for rodado
if __name__ == "__main__":
    menu()
