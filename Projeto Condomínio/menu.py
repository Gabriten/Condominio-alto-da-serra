import time
from cadastro import cad_uni, editar_unidade, remover_unidade
from listagem import listar_geral, listar_por_tipo, relatorio_estatistico


def exibir_menu():
    print("=" * 88)
    print("CONDOMÍNIO ALTO DA SERRA - SHELL CLI")
    print("=" * 88)
    print("1 - Cadastrar Unidade/Morador")
    print("2 - Editar Unidade")
    print("3 - Remover Unidade")
    print("4 - Listagem Geral de Unidades")
    print("5 - Listagem por Tipo de Imóvel")
    print("6 - Relatório Estatístico do Condomínio")
    print("0 - Sair")
    print("-" * 88)


def main():
    while True:
        exibir_menu()
        opcao = input("Opção desejada [0-6]: ").strip()
        if opcao == '1':
            cad_uni()
        elif opcao == '2':
            editar_unidade()
        elif opcao == '3':
            remover_unidade()
        elif opcao == '4':
            listar_geral()
        elif opcao == '5':
            listar_por_tipo()
        elif opcao == '6':
            relatorio_estatistico()
        elif opcao == '0':
            print("\nSaindo do sistema. Até logo!")
            time.sleep(1)
            break
        else:
            print("\nOpção inválida!\n")


main()
