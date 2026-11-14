#Parte do cadastro
#Gabriel

import time
import re
import json
import os

ARQUIVO = "condominio.txt"


# Funções para persistência em arquivo TXT (formato JSON)
def carregar_dados():
    # Se o arquivo não existir, retorna um dicionário vazio
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def salvar_dados():
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(unidades, f, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso no arquivo!")
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo: {e}")


#Validador de CPF
def validar_cpf(cpf):

    cpf = cpf.strip().replace(".", "").replace("-", "")

    # Verifica se possui 11 dígitos
    if not cpf.isdigit() or len(cpf) != 11:
        return False

    # Verifica se todos os números são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula os dois dígitos verificadores
    for tamanho in (9, 10):

        soma = 0

        for i in range(tamanho):
            soma += int(cpf[i]) * (tamanho + 1 - i)

        resto = (soma * 10) % 11

        digito = 0 if resto == 10 else resto

        if digito != int(cpf[tamanho]):
            return False

    return True

# Validador de nome

def validar_nome(nome):
  repetidos = re.compile(r"(\w)\1{2,}")
  if repetidos.search(nome):
    return False
  return True

#  == Cadastro de Morador ==

# Carrega os dados salvos previamente (retorna {} caso o arquivo não exista)
unidades = carregar_dados()

    #Cadastro de nova unidade

def cad_uni():

    numAp = input("Número do apartamento: ")
    while not numAp.isdigit() or len(numAp) > 4:
      print("Insira números válidos!")
      numAp = input("Número do apartamento: ")
    while int(numAp) < 0:
      print("Insira um número diferente de Zero: ")
      numAp = input("Número do apartamento: ")


    bloc = input("Bloco do apartamento(A,B,C): ").strip().upper()
    while bloc not in ["A", "B", "C"]:
      print("Insira somente os blocos permitidos: A, B ou C!")
      bloc = input("Bloco do apartamento(A,B,C): ").strip().upper()

    while (numAp + bloc) in unidades:
      print("Essa unidade já está cadastrada!\nInsira outra unidade!")
      numAp = input("Número do apartamento: ")
      bloc = input("Bloco do apartamento(ex.: A,B,C): ").strip().upper()


    while True:
      nome = input("Nome do responsável pelo imóvel: ").strip()
      if not nome.replace(" ", "").isalpha():
        print("Nome inválido! Por favor insira somente letras.")
        continue
      if len(nome) > 80:
        print("Por favor insira somente as letras necessárias!")
        continue

      nome = nome.lower()
      if not validar_nome(nome):
        print("Nome inválido! Evite usar mais de duas letras repetidas em sequência.")
        continue

      nome = nome.title()
      break

#CPF
    while True:
      cpf = input("Digite seu CPF: ").strip()

      while any(unidade["Cpf"] == cpf for unidade in unidades.values()):
        print("Este CPF já foi cadastrado à uma unidade!")
        cpf = input("Digite seu CPF: ").strip()

      if validar_cpf(cpf):
          print("CPF válido!")
          break
      else:
          print("CPF inválido! Tente novamente.")


    sexo = input("Sexo do responsável(1 - Feminino, 2 - Para masculino): ")
    while sexo not in ["1","2"]:
      print("Insira um dado válido!")
      sexo = input("Sexo do responsável(1 - Feminino, 2 - Para masculino): ")
    sexo = int(sexo)


    idade = input("Idade do responsável: ")
    while not idade.isdigit() or int(idade) < 18 or int(idade) > 120:
        print("Insira uma idade válida!")
        idade = input("Idade do responsável (Entre 18 e 120): ")
    idade = int(idade)


    print("Tipos de Apartamento:\n1- Standard (R$ 350)\n2- Luxo (R$ 500)\n3- Duplex (R$ 700)\n4- Cobertura (R$ 900)")
    tipoAp = input("Insira seu tipo do apartamento: ")
    while tipoAp not in ["1","2","3","4"]:
      print("Insira um valor válido!")
      tipoAp = input("Insira seu tipo do apartamento: ")
    tipoAp = int(tipoAp)


    vagas = input("Número de vagas extras de garagem: ")
    while not vagas.isdigit():
      print("Insira somente números por favor!")
      vagas = input("Número de vagas extras de garagem: ")
    while int(vagas) > 5:
      print("Você pediu por vagas demais!")
      vagas = input("Número de vagas extras (Máximo de 5): ")
    vagas = int(vagas)


    pet = input("Possui pet (1 - Sim, 0 - Não): ")
    while not pet.isdigit() or pet not in ["0", "1"]:
      print("Insira um valor válido!")
      pet = input("Possui pet (1 - sim, 0 - Não): ")
    pet = int(pet)


    sindico = input("Exerce a função de Síndico (1 - Sim, 0 - Não): ")
    while not sindico.isdigit() or sindico not in ["0", "1"]:
      print("Insira um valor válido!")
      sindico = input("Exerce a função de Síndico (1 - Sim, 0 - Não): ")
    sindico = int(sindico)

    vencimento = input("Data de vencimento da taxa Condominial (Entre os dias 1 e 28): ")
    while not vencimento.isdigit() or int(vencimento) < 1 or int(vencimento) > 28:
        print("Insira uma data válida!")
        vencimento = input("Data de vencimento da taxa Condominial (Entre os dias 1 e 28): ")

    vencimento = int(vencimento)


    #Tabela de Taxa Base Condominial e Vagas Extras

    extra_standart = 50 * vagas
    standart = 350

    extra_luxo = 70 * vagas
    luxo = 500

    extra_duplex = 90 * vagas
    duplex = 700

    extra_cober = 120 * vagas
    cobertura = 900

    taxa_extra = 0

    if tipoAp == 1:
      taxa = standart
      taxa_extra = extra_standart
    elif tipoAp == 2:
      taxa = luxo
      taxa_extra = extra_luxo
    elif tipoAp == 3:
      taxa = duplex
      taxa_extra = extra_duplex
    elif tipoAp == 4:
      taxa = cobertura
      taxa_extra = extra_cober


    #Regras de Negócio, Acréscimos e Descontos

# Fundo Reserva

    reserva = (taxa * 5)/100

# Desconto vagas extras
    if vagas > 2:
      desc_vagas = taxa_extra - ((taxa_extra * 20)/100)
    else:
      desc_vagas = taxa_extra

# Isenção Síndico

    if sindico == 1:
      taxa = 0

# Idoso
    if idade >= 65:
      taxa = taxa - ((taxa * 15)/100)

# Taxa Pet
    if pet == 1:
      taxa += 30

    taxa_total = taxa + desc_vagas + reserva

    # Armazenamento dos dados da unidade

    unidades[numAp + bloc] = {
        "Número do Apartamento": int(numAp),
        "Bloco": bloc,
        "Nome do Responsável": nome,
        "Cpf": cpf,
        "Sexo": sexo,
        "Idade": idade,
        "Tipo de Unidade": tipoAp,
        "Vagas Extras": vagas,
        "Possui Pet": pet,
        "Sindico": sindico,
        "Dia de Vencimento": str(vencimento),
        "Taxa Total": taxa_total
    }

    print("Unidade cadastrada com sucesso!")
    salvar_dados()


# Parte de Editar Unidade
def editar_unidade():
    print("\n[EDITAR UNIDADE]")
    numAp = input("Número do apartamento que deseja editar: ").strip()

    bloc = input("Bloco do apartamento (A, B, C): ").strip().upper()
    while bloc not in ["A", "B", "C"]:
        print("Insira somente os blocos permitidos: A, B ou C!")
        bloc = input("Bloco do apartamento (A, B, C): ").strip().upper()

    chave = numAp + bloc

    if chave not in unidades:
        print("Unidade não encontrada!")
        input("\nTecle ENTER para voltar ao menu...")
        return

    unidade = unidades[chave]
    print(f"\nEditando a unidade {numAp} - Bloco {bloc} de {unidade['Nome do Responsável']}")
    print("Caso queira manter o valor atual, basta pressionar ENTER sem digitar nada.\n")

    # 1. Nome do Responsável
    while True:
        nome = input(f"Nome do responsável [{unidade['Nome do Responsável']}]: ").strip()
        if not nome:
            nome = unidade['Nome do Responsável']
            break
        if not nome.replace(" ", "").isalpha():
            print("Nome inválido! Por favor insira somente letras.")
            continue
        if len(nome) > 80:
            print("Por favor insira somente as letras necessárias!")
            continue
        nome = nome.lower()
        if not validar_nome(nome):
            print("Nome inválido! Evite usar mais de duas letras repetidas em sequência.")
            continue
        nome = nome.title()
        break

    # 2. CPF
    while True:
        cpf = input(f"CPF [{unidade['Cpf']}]: ").strip()
        if not cpf:
            cpf = unidade['Cpf']
            break
        if any(u["Cpf"] == cpf and k != chave for k, u in unidades.items()):
            print("Este CPF já foi cadastrado em outra unidade!")
            continue
        if validar_cpf(cpf):
            print("CPF válido!")
            break
        else:
            print("CPF inválido! Tente novamente.")

    # 3. Sexo
    sexo_input = input(f"Sexo (1 - Feminino, 2 - Masculino) [{unidade['Sexo']}]: ")
    if not sexo_input:
        sexo = unidade['Sexo']
    else:
        while sexo_input not in ["1", "2"]:
            print("Insira um dado válido!")
            sexo_input = input("Sexo (1 - Feminino, 2 - Masculino): ")
        sexo = int(sexo_input)

    # 4. Idade
    idade_input = input(f"Idade [{unidade['Idade']}]: ")
    if not idade_input:
        idade = unidade['Idade']
    else:
        while not idade_input.isdigit() or int(idade_input) < 18 or int(idade_input) > 120:
            print("Insira uma idade válida!")
            idade_input = input("Idade do responsável (Entre 18 e 120): ")
        idade = int(idade_input)

    # 5. Tipo de Unidade
    print("Tipos de Apartamento:\n1- Standard (R$ 350)\n2- Luxo (R$ 500)\n3- Duplex (R$ 700)\n4- Cobertura (R$ 900)")
    tipo_input = input(f"Tipo de unidade [{unidade['Tipo de Unidade']}]: ")
    if not tipo_input:
        tipoAp = unidade['Tipo de Unidade']
    else:
        while tipo_input not in ["1", "2", "3", "4"]:
            print("Insira um valor válido!")
            tipo_input = input("Tipo de unidade: ").strip()
        tipoAp = int(tipo_input)

    # 6. Vagas Extras
    vagas_input = input(f"Vagas extras [{unidade['Vagas Extras']}]: ")
    if not vagas_input:
        vagas = unidade['Vagas Extras']
    else:
        while True:
            if not vagas_input.isdigit():
                print("Insira somente números por favor!")
            elif int(vagas_input) > 5:
                print("Você pediu por vagas demais! (Máximo de 5)")
            else:
                break
            vagas_input = input("Vagas extras (Máximo de 5): ")
        vagas = int(vagas_input)

    # 7. Possui Pet
    pet_input = input(f"Possui pet (1 - Sim, 0 - Não) [{unidade['Possui Pet']}]: ")
    if not pet_input:
        pet = unidade['Possui Pet']
    else:
        while pet_input not in ["0", "1"]:
            print("Insira um valor válido!")
            pet_input = input("Possui pet (1 - Sim, 0 - Não): ")
        pet = int(pet_input)

    # 8. Síndico
    sindico_input = input(f"Exerce a função de Síndico (1 - Sim, 0 - Não) [{unidade['Sindico']}]: ")
    if not sindico_input:
        sindico = unidade['Sindico']
    else:
        while sindico_input not in ["0", "1"]:
            print("Insira um valor válido!")
            sindico_input = input("Exerce a função de Síndico (1 - Sim, 0 - Não): ")
        sindico = int(sindico_input)

    # 9. Vencimento
    venc_input = input(f"Data de vencimento (Entre 1 e 28) [{unidade['Dia de Vencimento']}]: ")
    if not venc_input:
        vencimento = unidade['Dia de Vencimento']
    else:
        while not venc_input.isdigit() or int(venc_input) < 1 or int(venc_input) > 28:
            print("Insira uma data válida!")
            venc_input = input("Data de vencimento (Entre 1 e 28): ")
        vencimento = str(venc_input)

    # Recalculando Taxas
    taxas_valores = {
        1: {"base": 350, "vaga": 50},
        2: {"base": 500, "vaga": 70},
        3: {"base": 700, "vaga": 90},
        4: {"base": 900, "vaga": 120}
    }

    dados_tipo = taxas_valores[tipoAp]
    taxa_base = dados_tipo["base"]
    valor_vaga_unitaria = dados_tipo["vaga"]
    taxa_extra = valor_vaga_unitaria * vagas

    reserva = (taxa_base * 5) / 100

    if vagas > 2:
        desc_vagas = taxa_extra * 0.80
    else:
        desc_vagas = taxa_extra

    if sindico == 1:
        taxa_base = 0

    if idade >= 65 and sindico != 1:
        taxa_base = taxa_base * 0.85

    if pet == 1:
        taxa_base += 30

    taxa_total = taxa_base + desc_vagas + reserva

    # Grava as modificações
    unidades[chave] = {
        "Número do Apartamento": int(numAp),
        "Bloco": bloc,
        "Nome do Responsável": nome,
        "Cpf": cpf,
        "Sexo": sexo,
        "Idade": idade,
        "Tipo de Unidade": tipoAp,
        "Vagas Extras": vagas,
        "Possui Pet": pet,
        "Sindico": sindico,
        "Dia de Vencimento": str(vencimento),
        "Taxa Total": taxa_total
    }

    print("Unidade editada com sucesso!")
    salvar_dados()
    input("\nTecle ENTER para voltar ao menu...")


# Função para Remover Unidade
def remover_unidade():
    print("\n[REMOVER UNIDADE]")
    numAp = input("Número do apartamento que deseja remover: ")

    bloc = input("Bloco do apartamento (A, B, C): ").upper()
    while bloc not in ["A", "B", "C"]:
        print("Insira somente os blocos permitidos: A, B ou C!")
        bloc = input("Bloco do apartamento (A, B, C): ").upper()

    chave = numAp + bloc

    if chave not in unidades:
        print("Unidade não encontrada!")
        input("\nTecle ENTER para voltar ao menu...")
        return

    unidade = unidades[chave]
    print(f"\nUnidade Encontrada:")
    print(f"Apartamento: {unidade['Número do Apartamento']} - Bloco: {unidade['Bloco']}")
    print(f"Responsável: {unidade['Nome do Responsável']}")
    print(f"CPF: {unidade['Cpf']}")

    confirmacao = input("\nTem certeza de que deseja remover esta unidade? (S - Sim, N - Não): ").upper()
    if confirmacao == 'S':
        del unidades[chave]
        print("\nUnidade removida com sucesso!")
        salvar_dados()
    else:
        print("\nOperação de remoção cancelada pelo usuário.")

    input("\nTecle ENTER para voltar ao menu...")







# Parte do Menu
# Fabio

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
            print("\n[Interface] Entrou na opção: Cadastrar Unidade/Morador\n")
            cad_uni()
        elif opcao == '2':
            print("\n[Interface] Entrou na opção: Editar Unidade\n")
            editar_unidade()
        elif opcao == '3':
            print("\n[Interface] Entrou na opção: Remover Unidade\n")
            remover_unidade()
        elif opcao == '4':
            print("\n[Interface] Entrou na opção: Listagem Geral de Unidades\n")
            listar_geral()
        elif opcao == '5':
            print("\n[Interface] Entrou na opção: Listagem por Tipo de Imóvel\n")
            listar_por_tipo()
        elif opcao == '6':
            print("\n[Interface] Entrou na opção: Relatório Estatístico do Condomínio\n")
        elif opcao == '0':
            print("\nSaindo do sistema. Até logo!")
            time.sleep(2)
            break
        else:
            print("\nOpção inválida! Escolha de 0 a 6.\n")








#Parte da Listagem
#Denis

# ============================================================
# PARTE DE LISTAGEM - CONDOMÍNIO VIVER BEM
# Opção 4 - Listagem Geral / Opção 5 - Listagem por Tipo
# ============================================================


# Tabela de valores do PDF
TAXAS = {
    1: {"nome": "Standard", "base": 350.00, "vaga": 50.00},
    2: {"nome": "Luxo", "base": 500.00, "vaga": 70.00},
    3: {"nome": "Duplex", "base": 700.00, "vaga": 90.00},
    4: {"nome": "Cobertura", "base": 900.00, "vaga": 120.00},
}

def ler_unidades():
    dados_salvos = carregar_dados()
    lista_unidades = []
    for chave, u in dados_salvos.items():
        # Garante que chaves antigas e novas usem inteiros para os tipos que necessitam
        unidade_padronizada = u.copy()
        if isinstance(unidade_padronizada.get("Tipo de Unidade"), str):
            map_tipos = {"Standard": 1, "Standart": 1, "Luxo": 2, "Duplex": 3, "Cobertura": 4}
            unidade_padronizada["Tipo de Unidade"] = map_tipos.get(unidade_padronizada["Tipo de Unidade"], 1)

        unidade_padronizada["Vagas Extras"] = int(unidade_padronizada.get("Vagas Extras", 0))
        unidade_padronizada["Idade"] = int(unidade_padronizada.get("Idade", 0))
        unidade_padronizada["Possui Pet"] = int(unidade_padronizada.get("Possui Pet", 0))
        unidade_padronizada["Sindico"] = int(unidade_padronizada.get("Sindico", 0))
        lista_unidades.append(unidade_padronizada)

    lista_unidades.sort(key=lambda x: (x["Bloco"], x["Número do Apartamento"]))
    return lista_unidades

def calcular_taxa(unidade):
    dados = TAXAS[unidade["Tipo de Unidade"]]
    base_original = dados["base"]
    valor_vaga = dados["vaga"]

    # 1. Vagas Extras
    total_vagas = grid_vagas = unidade["Vagas Extras"] * valor_vaga
    if unidade["Vagas Extras"] > 2:
        total_vagas = total_vagas * 0.80  # 20% de desconto só nas vagas

    # 2. Isenção de Síndico (100% na Taxa Base)
    if unidade["Sindico"] == 1:
        base_final = 0
    else:
        base_final = base_original

    # 3. Desconto de Idoso (15% só na Taxa Base)
    if unidade["Idade"] >= 65 and unidade["Sindico"] != 1:
        base_final = base_final * 0.85

    # 4. Taxa de Pet
    taxa_pet = 30.00 if unidade["Possui Pet"] == 1 else 0

    # 5. Fundo de Reserva (5% da base ORIGINAL, sempre)
    fundo = base_original * 0.05

    taxa_total = base_final + total_vagas + taxa_pet + fundo
    return taxa_total

def mostrar_tabela(unidades, titulo):
    print(f"\n[{titulo}]")
    print("=" * 115)
    print(f"| {'Apto':<6} | {'Bloco':<5} | {'Nome do Responsável':<25} | {'Idade':<5} | {'Tipo':<10} | {'Vagas Ex.':<9} | {'Pet':<3} | {'Taxa Total':<11} | {'Vencimento':<10} |")
    print("-" * 115)
    for u in unidades:
        taxa = calcular_taxa(u)
        nome_tipo = TAXAS[u["Tipo de Unidade"]]["nome"]
        pet_txt = "Sim" if u["Possui Pet"] == 1 else "Não"
        venc = str(u["Dia de Vencimento"])
        # Se no arquivo estiver só o dia "10", mostra como 10/11/2026 igual o PDF
        if "/" not in venc:
            venc = f" {venc}/11/2026"
        print(f"| {u['Número do Apartamento']:<6} | {u['Bloco']:<5} | {u['Nome do Responsável']:<25} | {u['Idade']:<5} | {nome_tipo:<10} | {u['Vagas Extras']:<9} | {pet_txt:<3} | R$ {taxa:<7.2f} | {venc:<10} |")
    print("=" * 115)

def listar_geral():
    unidades = ler_unidades()
    if len(unidades) == 0:
        print("\n[LISTAGEM GERAL DE UNIDADES DE CONDOMÍNIO]")
        print("Nenhuma unidade cadastrada.")
    else:
        mostrar_tabela(unidades, "LISTAGEM GERAL DE UNIDADES DE CONDOMÍNIO")
    input("\nTecle ENTER para voltar ao menu...")

def listar_por_tipo():
    print("\n[LISTAGEM POR TIPO DE IMÓVEL]")
    print("1 - Standard")
    print("2 - Luxo")
    print("3 - Duplex")
    print("4 - Cobertura")
    try:
        tipo_escolhido = int(input("Digite o tipo desejado [1-4]: "))
    except:
        print("Tipo inválido!")
        input("\nTecle ENTER para voltar ao menu...")
        return

    if tipo_escolhido not in TAXAS:
        print("Tipo inválido!")
        input("\nTecle ENTER para voltar ao menu...")
        return

    unidades = ler_unidades()
    filtradas = [u for u in unidades if u["Tipo de Unidade"] == tipo_escolhido]

    if len(filtradas) == 0:
        print(f"\nNenhuma unidade do tipo {TAXAS[tipo_escolhido]['nome']} encontrada.")
    else:
        mostrar_tabela(filtradas, f"LISTAGEM POR TIPO DE IMÓVEL - {TAXAS[tipo_escolhido]['nome'].upper()}")
    input("\nTecle ENTER para voltar ao menu...")


# Executa apenas a interface do shell
main()
