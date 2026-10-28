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
#    Cadastro de nova unidade
def cad_uni():
    numAp = input("Número do apartamento: ")

    if numAp in unidades:
        print("Essa unidade já está cadastrada!")
        return

    print("Tipos de Apartamento:\n1- Standart\n2- Luxo\n3- Duplex\n 4- Cobertura")
    tipoAp = input("Insira seu tipo do apartamento: ")
#    bloco
#    nome do resp
#    cpf
#    sexo
#    idade
#    tipo de unidade
#    vagas de garag extras
#    pet
#    sindico
#    data de venc

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

