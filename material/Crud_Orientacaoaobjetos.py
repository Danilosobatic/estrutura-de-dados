class Usuario:
    def __init__(self, id_usuario, nome):
        """Inicializa um novo usuário com id e nome."""
        self.id = id_usuario
        self.nome = nome

    def __str__(self):
        """Representação em string do usuário."""
        return f"ID: {self.id}, Nome: {self.nome}"


class GestaoUsuarios:
    def __init__(self):
        """Inicializa a gestão de usuários com uma lista vazia."""
        self.usuarios = []

    def criar_usuario(self, nome):
        """Cria um novo usuário, atribuindo um ID único."""
        # Determina o ID baseado no número de usuários existentes
        id_usuario = len(self.usuarios) + 1
        
        # Cria o usuário e adiciona à lista de usuários
        usuario = Usuario(id_usuario, nome)
        self.usuarios.append(usuario)
        
        print(f"Usuário {nome} adicionado com sucesso.")

    def ler_usuarios(self):
        """Exibe todos os usuários cadastrados."""
        if not self.usuarios:
            print("Nenhum usuário encontrado.")
        else:
            print("Usuários cadastrados:")
            for usuario in self.usuarios:
                print(usuario)

    def atualizar_usuario(self, id_usuario, novo_nome):
        """Atualiza o nome de um usuário existente."""
        usuario_encontrado = False
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                usuario.nome = novo_nome
                usuario_encontrado = True
                break
        
        if usuario_encontrado:
            print(f"Usuário ID {id_usuario} atualizado para {novo_nome}.")
        else:
            print(f"Usuário com ID {id_usuario} não encontrado.")

    def deletar_usuario(self, id_usuario):
        """Deleta um usuário baseado no ID."""
        usuario_encontrado = False
        for i, usuario in enumerate(self.usuarios):
            if usuario.id == id_usuario:
                self.usuarios.pop(i)
                usuario_encontrado = True
                break
        
        if usuario_encontrado:
            print(f"Usuário ID {id_usuario} deletado com sucesso.")
        else:
            print(f"Usuário com ID {id_usuario} não encontrado.")


# Função que implementa o menu interativo para o usuário
def menu():
    gestao = GestaoUsuarios()  # Instancia a classe de gestão de usuários

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
            gestao.criar_usuario(nome)
        # Operação de leitura de usuários
        elif escolha == '2':
            gestao.ler_usuarios()
        # Operação de atualização de usuário
        elif escolha == '3':
            try:
                id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
                novo_nome = input("Digite o novo nome do usuário: ")
                gestao.atualizar_usuario(id_usuario, novo_nome)
            except ValueError:
                print("Erro: ID inválido.")  # Caso o ID informado não seja um número
        # Operação de deleção de usuário
        elif escolha == '4':
            try:
                id_usuario = int(input("Digite o ID do usuário a ser deletado: "))
                gestao.deletar_usuario(id_usuario)
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
