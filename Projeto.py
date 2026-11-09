import time
#  == Cadastro de Morador ==
#dados da unidade e morador

unidades = {}

    #Cadastro de nova unidade

def cad_uni():

    numAp = input("Número do apartamento: ")
    while not numAp.isdigit() or len(numAp) > 4:
      print("Insira números válidos!")
      numAp = input("Número do apartamento: ")
    numAp = int(numAp)


    bloc = input("Bloco do apartamento(ex.: A,B,C...): ")
    while not bloc.isalpha() or len(bloc) > 1:
      print("Insira somente Uma Letra!")
      bloc = input("Bloco do apartamento(ex.: A,B,C...): ")

    while numAp and bloc in unidades:
      print("Essa unidade já está cadastrada!")
      numAp = input("Número do apartamento: ")
      bloc = input("Bloco do apartamento(ex.: A,B,C...): ")


    nome = input("Nome do responsável pelo imóvel: ")
    while not nome.replace(" ", "").isalpha():
      print("Nome inválido! Por favor insira somente letras.")
      nome = input("Digite seu nome novamente: ")

#CPF
    while True:
      cpf = input("Digite seu CPF: ")

      while cpf in unidades:
        print("Este CPF já foi cadastrado à uma unidade!")
        cpf = input("Digite seu CPF: ")

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
        idade = input("Idade do responsável: ")
    idade = int(idade)


    print("Tipos de Apartamento:\n1- Standart\n2- Luxo\n3- Duplex\n4- Cobertura")
    tipoAp = input("Insira seu tipo do apartamento: ")
    while tipoAp not in ["1","2","3","4"]:
      print("Insira um valor válido!")
      tipoAp = input("Insira seu tipo do apartamento: ")


    vagas = input("Número de vagas extras de garagem: ")
    while not vagas.isdigit():
      print("Insira somente números por favor!")
      vagas = input("Número de vagas extras de garagem: ")
    vagas = int(vagas)


    pet = input("Possui pet (1 - Sim, 0 - Não): ")
    while not pet.isdigit() or pet not in ["0", "1"]:
      print("Insira um valor válido!")
      pet = input("Possui pet (1 - sim, 0 - Não): ")


    sindico = input("Exerce a função de Síndico (1 - Sim, 0 - Não): ")
    while not sindico.isdigit() or sindico not in ["0", "1"]:
      print("Insira um valor válido!")
      sindico = input("Exerce a função de Síndico (1 - Sim, 0 - Não): ")

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

    if tipoAp == "1":
      taxa = standart
      taxa_extra = extra_standart

    if tipoAp == "2":
      taxa = luxo
      taxa_extra = extra_luxo

    if tipoAp == "3":
      taxa = duplex
      taxa_extra = extra_duplex

    if tipoAp == "4":
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

    if sindico == "1":
      taxa = 0

# Idoso
    if idade >= 65:
      taxa = taxa - ((taxa * 15)/100)

# Taxa Pet
    if pet == "1":
      taxa += 30

    taxa_total = taxa + desc_vagas + reserva
    
    # Armazenamento dos dados da unidade

    unidades[numAp,bloc] = {
        "numero_apartamento": numAp,
        "bloco": bloc,
        "nome_responsavel": nome,
        "cpf": cpf,
        "sexo": sexo,
        "idade": idade,
        "tipo_unidade": tipoAp,
        "vagas_extras": vagas,
        "possui_pet": pet,
        "sindico": sindico,
        "dia_vencimento": vencimento,
        "Taxa Total": taxa_total
    }

    print("Unidade cadastrada com sucesso!")


    print(unidades)


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





# Parte do Menu

def exibir_menu():
    print("=" * 88)
    print("CONDOMÍNIO ALTO DA SERRA - SHELL CLI")
    print("=" * 88)
    print("1 - Cadastrar Unidade/Morador")
    print("2 - Editar Unidade")
    print("3 - Remover Unidade")
    print("4 - Listagem Geral de Unidades")
    print("5 - Listagem por Tipo de Imóvel")
    print("6 - Re latório Estatístico do Condomínio")
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
        elif opcao == '3':
            print("\n[Interface] Entrou na opção: Remover Unidade\n")
        elif opcao == '4':
            print("\n[Interface] Entrou na opção: Listagem Geral de Unidades\n")
        elif opcao == '5':
            print("\n[Interface] Entrou na opção: Listagem por Tipo de Imóvel\n")
        elif opcao == '6':
            print("\n[Interface] Entrou na opção: Relatório Estatístico do Condomínio\n")
        elif opcao == '0':
            print("\nSaindo do sistema. Até logo!")
            time.sleep(2)
            break
        else:
            print("\nOpção inválida! Escolha de 0 a 6.\n")

# Executa apenas a interface do shell
main()
