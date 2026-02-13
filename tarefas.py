import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

tarefas = carregar_tarefas()

while True:
    print("\nTarefas:")
    for i, t in enumerate(tarefas, 1):
        print(f"{i}. {t}")
    print("\n1 - Adicionar | 2 - Remover | 3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ").strip()
        if tarefa:
            tarefas.append(tarefa)
            salvar_tarefas(tarefas)
    elif opcao == "2":
        try:
            idx = int(input("Número da tarefa: ")) - 1
            if 0 <= idx < len(tarefa):
                tarefas.pop(idx)
                salvar_tarefas(tarefas)
        except ValueError:
            print("Entrada inválida.")
    elif opcao == "3":
        break
    else:
        print("Opção inválida.")
