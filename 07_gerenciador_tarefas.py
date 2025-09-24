def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open("tarefas.txt", "w") as f:
        f.write("\n".join(tarefas))

tarefas = carregar_tarefas()

while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
    elif opcao == "2":
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    elif opcao == "3":
        num = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas.pop(num)
            salvar_tarefas(tarefas)
        else:
            print("Tarefa inválida.")
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
