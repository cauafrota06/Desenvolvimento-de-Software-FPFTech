class Tarefa:
    def __init__(self, id, categoria, descricao, urgencia, diasRestantes):
        self.id = id
        self.categoria = categoria
        self.descricao = descricao
        self.urgencia = urgencia
        self.diasRestantes = diasRestantes
        self.status = "Pendente"

class GerenciadorTarefas:
    def __init__(self):

        self.lista_tarefas = []

    def adicionar_tarefa(self):
        tarefa_id = len(self.lista_tarefas) + 1
        categoria = input('Categoria: ')
        descricao = input('Descrição: ')
        urgencia = input('Urgência (Moderado, Importante, Crítico): ')
        dias_restantes = input('Dias restantes: ')

        nova_tarefa = Tarefa(tarefa_id, categoria, descricao, urgencia, dias_restantes)
        self.lista_tarefas.append(nova_tarefa)

        print(f"Tarefa '{descricao}' criada com sucesso!")

    def alterar_status(self):
        self.listar_tarefas()

        if not self.lista_tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        id_busca = int(input("Digite o ID da tarefa que deseja atualizar o status: "))

        for tarefa in self.lista_tarefas:
            if tarefa.id == id_busca:
                tarefa.status = input("Novo status: ")

                print(f"Tarefa {id_busca} atualizada!")
                return

        print("Tarefa não encontrada.")

    def listar_tarefas(self):
        if not self.lista_tarefas:
            print("A lista está vazia.")
        else:
            print("\n--- LISTA DE TAREFAS ---")
            for t in self.lista_tarefas:
                print(f"ID: {t.id} | [{t.status}] {t.descricao} (Urgência: {t.urgencia})")

    def deletar_tarefa(self):
        self.listar_tarefas()
        if not self.lista_tarefas:
            return

        try:
            id_para_deletar = int(input("Digite o ID da tarefa que deseja deletar: "))

            tarefa_encontrada = None

            for tarefa in self.lista_tarefas:
                if tarefa.id == id_para_deletar:
                    tarefa_encontrada = tarefa
                    break
            if tarefa_encontrada:
                self.lista_tarefas.remove(tarefa_encontrada)
                print(f"Tarefa {id_para_deletar} deletada com sucesso!")
            else:

                print(f"Erro: Não existe tarefa com o ID {id_para_deletar}.")

        except ValueError:
            print("Erro: Por favor, digite um número inteiro correspondente ao ID.")

    def menu(self):

        while True:
            print('\n1 - Criar Tarefa')
            print('2 - Alterar Status')
            print('3 - Listar Tarefas')
            print('4 - Deletar Tarefa')
            print('0 - Sair')

            opcao = int(input('Opção: '))

            if opcao == 1:
                self.adicionar_tarefa()

            elif opcao == 2:
                self.alterar_status()

            elif opcao == 3:
                self.listar_tarefas()

            elif opcao == 4:
                self.deletar_tarefa()

            elif opcao == 0:
                print("Saindo...........")
                break

gerenciador = GerenciadorTarefas()
gerenciador.menu()