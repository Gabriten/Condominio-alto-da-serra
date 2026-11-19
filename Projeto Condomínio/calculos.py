TAXAS = {
    1: {"nome": "Standard  - R$350", "base": 350.00, "vaga": 50.00},
    2: {"nome": "Luxo      - R$500", "base": 500.00, "vaga": 70.00},
    3: {"nome": "Duplex    - R$700", "base": 700.00, "vaga": 90.00},
    4: {"nome": "Cobertura - R$900", "base": 900.00, "vaga": 120.00},
}


def calcular_taxa(unidade):
    dados = TAXAS[unidade["Tipo de Unidade"]]
    base_original = dados["base"]
    valor_vaga = dados["vaga"]
    total_vagas = unidade["Vagas Extras"] * valor_vaga
    
    if unidade["Vagas Extras"] > 2:
        total_vagas = total_vagas * 0.80

    if unidade["Sindico"] == 1:
        base_final = 0
    else:
        base_final = base_original

    if unidade["Idade"] >= 65 and unidade["Sindico"] != 1:
        base_final = base_final * 0.85

    taxa_pet = 30.00 if unidade["Possui Pet"] == 1 else 0
    fundo = base_original * 0.05

    taxa_total = base_final + total_vagas + taxa_pet + fundo
    
    return taxa_total
