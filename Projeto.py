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
        "dia_vencimento": vencimento
    }

    print("Unidade cadastrada com sucesso!")

cad_uni()
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

    
#Tabela de Taxa Base Condominial e Vagas Extras

#    standart 350 VE 50
#    luxo 500 VE 70
#    duplex 700 VE 90
#    cobertura 900 VE 120

#Regras de Negócio, Acréscimos e Descontos

#    Desconto vag extra >2 = 20% VE
#    isencao sindico 100% TB
#    desconto de idoso >65 A 15% TB
#    taxa pet pet == 1  += 30R$
#    fundo de reserva 5% TB
