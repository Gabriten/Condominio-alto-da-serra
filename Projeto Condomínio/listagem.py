from bancodedados import ler_unidades
from calculos import TAXAS, calcular_taxa


def mostrar_tabela(unidades, titulo):
    print(f"\n[{titulo}]")
    print("=" * 121)
    print(f"| {'Apto':<6} | {'Bloco':<5} | {'Nome do Responsável':<25} | {'Idade':<5} | {'Tipo do Apto.':<18} | {'Vagas Ex.':<9} | {'Pet':<3} | {'Taxa Total':<11} | {'Vencimento':<10} |")
    print("-" * 121)
    for u in unidades:
        taxa = calcular_taxa(u)
        nome_tipo = TAXAS[u["Tipo de Unidade"]]["nome"]
        pet_txt = "Sim" if u["Possui Pet"] == 1 else "Não"
        venc = str(u["Dia de Vencimento"])
        if "/" not in venc:
            venc = f" {venc}/11/2026"
        print(f"| {u['Número do Apartamento']:<6} | {u['Bloco']:<5} | {u['Nome do Responsável'][:25]:<25} | {u['Idade']:<5} | {nome_tipo:<18} | {u['Vagas Extras']:<9} | {pet_txt:<3} | R$ {taxa:<7.2f} | {venc:<10} |")
    print("=" * 121)


def listar_geral():
    unidades = ler_unidades()
    if len(unidades) == 0:
        print("\n[LISTAGEM GERAL DE UNIDADES DE CONDOMÍNIO]\nNenhuma unidade cadastrada.")
    else:
        mostrar_tabela(unidades, "LISTAGEM GERAL DE UNIDADES DE CONDOMÍNIO")
    input("\nTecle ENTER para voltar ao menu...\n")


def listar_por_tipo():
    print("\n[LISTAGEM POR TIPO DE IMÓVEL]")
    print("1 - Standard\n2 - Luxo\n3 - Duplex\n4 - Cobertura")
    try:
        tipo_escolhido = int(input("Digite o tipo desejado [1-4]: "))
    except:
        print("Tipo inválido!")
        return

    unidades = ler_unidades()
    filtradas = [u for u in unidades if u["Tipo de Unidade"] == tipo_escolhido]
    if len(filtradas) == 0:
        print(f"\nNenhuma unidade deste tipo encontrada.")
    else:
        mostrar_tabela(filtradas, "LISTAGEM FILTRADA")
    input("\nTecle ENTER para voltar ao menu...\n")


def relatorio_estatistico():
    unidades_lista = ler_unidades()
    total_unidades = len(unidades_lista)
    if total_unidades > 0:
        total_pets = sum(1 for u in unidades_lista if u["Possui Pet"] == 1)
        perc_pets = (total_pets / total_unidades) * 100
    else:
        perc_pets = 0.0
    total_vagas_extras = sum(u["Vagas Extras"] for u in unidades_lista)
    unidades_cob_dup = [u for u in unidades_lista if u["Tipo de Unidade"] in [3, 4]]
    media_cob_dup = sum(calcular_taxa(u) for u in unidades_cob_dup) / len(unidades_cob_dup) if unidades_cob_dup else 0.0
    arrecadacao_total = sum(calcular_taxa(u) for u in unidades_lista)

    print("\n" + "=" * 20 + " RELATÓRIO ESTATÍSTICO " + "=" * 20)
    print(f"• Percentual de unidades com animais de estimação (Pets): {perc_pets:.2f}%")
    print(f"• Quantidade total de vagas de garagem extras alocadas: {total_vagas_extras} vagas")
    print(f"• Média do valor da taxa condominial das Coberturas e Duplex: R$ {media_cob_dup:,.2f}")
    print(f"• Arrecadação total mensal (Taxas + Fundo de Reserva): R$ {arrecadacao_total:,.2f}")
    print("-" * 63)
    input("tecle ENTER para voltar ao menu principal...\n")
