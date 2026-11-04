#========================================================================================
# CONDOMÍNIO Alto Da Serra - SHELL CLI
#========================================================================================
# 1 - Cadastrar Unidade/Morador
# 2 - Editar Unidade
# 3 - Remover Unidade
# 4 - Listagem Geral de Unidades
# 5 - Listagem por Tipo de Imóvel
# 6 - Relatório Estatístico do Condomínio
# 0 - Sair
#----------------------------------------------------------------------------------------
#Opção desejada [0-6]: _

#  == Cadastro de Morador ==
#dados da unidade e morador

unidades = {}

    #Cadastro de nova unidade

def cad_uni():
    numAp = input("Número do apartamento: ")
    bloc = input("Bloco do apartamento(ex.: A,B,C...): ")
    while numAp and bloc in unidades:
      print("Essa unidade já está cadastrada!")
      numAp = input("Número do apartamento: ")
      bloc = input("Bloco do apartamento(ex.: A,B,C...): ")
        
    nome = input("Nome do responsável pelo imóvel: ")
    while any(caractere.isdigit() for caractere in nome):
      print("Nome inválido! Por favor não insira números.")
      nome = input("Digite seu nome novamente: ")
    
    cpf = int(input("CPF (Apenas números) do responsável pelo imóvel: "))
    if cpf in unidades:
        print("Esse CPF já foi anexado à uma unidade!")
        return
    
    sexo = int(input("Sexo do responsável(1 - Feminino, 2 - Para masculino): "))
    
    idade = int(input("Idade do responsável: "))
    
    print("Tipos de Apartamento:\n1- Standart\n2- Luxo\n3- Duplex\n4- Cobertura")
    tipoAp = int(input("Insira seu tipo do apartamento: "))
    
    vagas_extras = int(input("Número de vagas extras de garagem: "))
    
    pet = int(input("Possui pet (1 - Sim, 0 - Não): "))
    
    sindico = int(input("Exerce a função de Síndico (1 - Sim, 0 - Não): "))

    venc_taxa = int(input("Data de vencimento da taxa Condominial (Somente o dia): "))

    # Armazenamento dos dados da unidade

    unidades[numAp,bloc] = {
        "numero_apartamento": numAp,
        "bloco": bloc,
        "nome_responsavel": nome_resp,
        "cpf": cpf,
        "sexo": sexo,
        "idade": idade,
        "tipo_unidade": tipoAp,
        "vagas_extras": vagas_extras,
        "possui_pet": pet,
        "sindico": sindico,
        "dia_vencimento": venc_taxa
    }

    print("Unidade cadastrada com sucesso!")

cad_uni()
print(unidades)

#Tabela de Taxa Base Condominial e Vagas Extras
#    standart
#    luxo
#    duplex
#    cobertura

#Regras de Negócio, Acréscimos e Descontos
#    Desconto vag extra
#    isencao sindico
#    desconto de idoso
#    taxa pet
#    fundo de reserva

