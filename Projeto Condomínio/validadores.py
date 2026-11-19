import re


def validar_cpf(cpf):
    cpf = cpf.strip().replace(".", "").replace("-", "")
    
    #Verifica se tem 11 digitos
    if not cpf.isdigit() or len(cpf) != 11:
        return False
        
    #Verifica se os digitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    #Calculo do Dígito Verificador
    for tamanho in (9, 10):
        soma = 0
        for i in range(tamanho):
            soma += int(cpf[i]) * (tamanho + 1 - i)
        resto = (soma * 10) % 11
        digito = 0 if resto == 10 else resto
        if digito != int(cpf[tamanho]):
            return False
    return True


def validar_nome(nome):
    #Verifica se um mesmo digito está repetido mais que 2 vezes
    repetidos = re.compile(r"(\w)\1{2,}")
    
    #Procura pela repetição no nome e invalida
    if repetidos.search(nome):
        return False
    return True
