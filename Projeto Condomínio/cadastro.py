from bancodedados import carregar_dados, salvar_dados
from validadores import validar_cpf, validar_nome
from calculos import TAXAS, calcular_taxa


def cad_uni():
    
    unidades = carregar_dados()
    
    numAp = input("Número do apartamento: ")
    while not numAp.isdigit() or len(numAp) > 4:
        print("Insira números válidos!")
        numAp = input("Número do apartamento: ")
    while int(numAp) < 1:
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

    #Dicionário para calcular a Taxa Total
    unidade_calc = {
        "Tipo de Unidade": tipoAp,
        "Vagas Extras": vagas,
        "Sindico": sindico,
        "Idade": idade,
        "Possui Pet": pet
    }
    taxa_total = calcular_taxa(unidade_calc)

    #A forma como a unidade será salva no Arquivo
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

    tipos_nome = {1: "Standard - R$350.00", 2: "Luxo - R$500.00", 3: "Duplex - R$700.00", 4: "Cobertura - R$900.00"}
    print("\n" + "=" * 50)
    print("          CADASTRO REALIZADO COM SUCESSO!")
    print("=" * 50)
    print(f"• Apartamento: {numAp} - Bloco: {bloc}")
    print(f"• Responsável: {nome}")
    print(f"• CPF: {cpf}")
    print(f"• Sexo: {'Feminino' if sexo == 1 else 'Masculino'}")
    print(f"• Idade: {idade} anos")
    print(f"• Tipo de Unidade: {tipos_nome.get(tipoAp, 'Tipo')}")
    print(f"• Vagas Extras de Garagem: {vagas}")
    print(f"• Possui Pet: {'Sim' if pet == 1 else 'Não'}")
    print(f"• Síndico: {'Sim' if sindico == 1 else 'Não'}")
    print(f"• Dia de Vencimento da Taxa: {vencimento}")
    print(f"• Taxa Total Calculada: R$ {taxa_total:.2f}")
    print("=" * 50 + "\n")

    salvar_dados(unidades)


def editar_unidade():
    unidades = carregar_dados()
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

    nome_alterado = False
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
        if nome != unidade['Nome do Responsável']:
            nome_alterado = True
        break

    while True:
        if nome_alterado:
            print("Como o Nome do responsável foi alterado, você precisa Obrigatoriamente fornecer um novo CPF!")
            cpf = input("Novo CPF: ").strip()
            if not cpf:
                print("O CPF não pode ficar em branco quando o nome é alterado!")
                continue
        else: 
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

    sexo_input = input(f"Sexo (1 - Feminino, 2 - Masculino) [{unidade['Sexo']}]: ")
    sexo = int(sexo_input) if sexo_input in ["1", "2"] else unidade['Sexo']

    idade_input = input(f"Idade [{unidade['Idade']}]: ")
    if not idade_input:
        idade = unidade['Idade']
    else:
        while not idade_input.isdigit() or int(idade_input) < 18 or int(idade_input) > 120:
            print("Insira uma idade válida!")
            idade_input = input("Idade do responsável (Entre 18 e 120): ")
        idade = int(idade_input)

    print("Tipos de Apartamento:\n1- Standard (R$ 350)\n2- Luxo (R$ 500)\n3- Duplex (R$ 700)\n4- Cobertura (R$ 900)")
    tipo_input = input(f"Tipo de unidade [{unidade['Tipo de Unidade']}]: ")
    tipoAp = int(tipo_input) if tipo_input in ["1", "2", "3", "4"] else unidade['Tipo de Unidade']

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

    pet_input = input(f"Possui pet (1 - Sim, 0 - Não) [{unidade['Possui Pet']}]: ")
    pet = int(pet_input) if pet_input in ["0", "1"] else unidade['Possui Pet']

    sindico_input = input(f"Exerce a função de Síndico (1 - Sim, 0 - Não) [{unidade['Sindico']}]: ")
    sindico = int(sindico_input) if sindico_input in ["0", "1"] else unidade['Sindico']

    venc_input = input(f"Data de vencimento (Entre 1 e 28) [{unidade['Dia de Vencimento']}]: ")
    if not venc_input:
        vencimento = unidade['Dia de Vencimento']
    else:
        while not venc_input.isdigit() or int(venc_input) < 1 or int(venc_input) > 28:
            print("Insira uma data válida!")
            venc_input = input("Data de vencimento (Entre 1 e 28): ")
        vencimento = str(venc_input)

    unidade_temp = {
        "Tipo de Unidade": tipoAp,
        "Vagas Extras": vagas,
        "Sindico": sindico,
        "Idade": idade,
        "Possui Pet": pet
    }
    taxa_total = calcular_taxa(unidade_temp)

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
    salvar_dados(unidades)


def remover_unidade():
    unidades = carregar_dados()
    
    print("\n[REMOVER UNIDADE]")
    numAp = input("Número do apartamento que deseja remover: ")
    bloc = input("Bloco do apartamento (A, B, C): ").upper()
    chave = numAp + bloc

    if chave not in unidades:
        print("Unidade não encontrada!")
        input("\nTecle ENTER para voltar ao menu...\n")
        return

    unidade = unidades[chave]
    print(f"\nUnidade Encontrada:")
    print(f"Apartamento: {unidade['Número do Apartamento']} - Bloco: {unidade['Bloco']}")
    confirmacao = input("\nTem certeza de que deseja remover esta unidade? (S - Sim, N - Não): ").upper()
    if confirmacao == 'S':
        del unidades[chave]
        print("\nUnidade removida com sucesso!")
        salvar_dados(unidades)
    else:
        print("\nOperação de remoção cancelada pelo usuário.")
    input("\nTecle ENTER para voltar ao menu...\n")
