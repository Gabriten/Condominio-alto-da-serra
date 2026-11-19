import os
import json


ARQUIVO = "condominio.txt"


def carregar_dados():
    #Procura se o arquivo existe, caso não, cria uma lista vazia
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}
    #Essa lista vazia será salva posteriormente


def salvar_dados(unidades):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(unidades, f, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso no arquivo!\n")
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo: {e}")
        #Se der algum erro, o programa mostrará qual erro ocorreu ao usuário


def ler_unidades():
    dados_salvos = carregar_dados()
    lista_unidades = []
    for chave, u in dados_salvos.items():
        unidade_padronizada = u.copy()
        unidade_padronizada["Vagas Extras"] = int(unidade_padronizada.get("Vagas Extras", 0))
        unidade_padronizada["Idade"] = int(unidade_padronizada.get("Idade", 0))
        unidade_padronizada["Possui Pet"] = int(unidade_padronizada.get("Possui Pet", 0))
        unidade_padronizada["Sindico"] = int(unidade_padronizada.get("Sindico", 0))
        lista_unidades.append(unidade_padronizada)
    lista_unidades.sort(key=lambda x: (x["Bloco"], x["Número do Apartamento"]))
    return lista_unidades
