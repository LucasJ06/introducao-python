#criando um dicionario
dados_lucas = {
    "sobrenome":"Juan",
    "nome":"Lucas",
    "filhos":False,
    "formacao":["Data Science", "Administracao"],
    "cargos":[
        {"nome":"Jovem Aprendiz", "empresa": "PDtec"},
        {"nome":"Assistente de RH", "empresa":"PDtec"},
        {"nome":"Assistente de People Analytics", "empresa": "Renner S.A"}
    ]
}

#acessando os elementos do dicionario
print(dados_lucas)
print(dados_lucas["formacao"][-1])
print(dados_lucas["cargos"][-1]["empresa"])

#atribuindo novos elementos ao dicionario
dados_lucas["estado civil"] = "Solteiro"
print(dados_lucas)

#descobrindo as chaves do dicionario
print(dados_lucas.keys())

#deixando mais visual
for i in dados_lucas.keys():
    print(i)

#descobrindo os valores
print(dados_lucas.values())

#deixando mais visual
for i in dados_lucas.values():
    print(i)

#acessando cada elemento do dicionario usando for
for i in dados_lucas:
    print(f"{i} - {dados_lucas[i]}")
#outra forma de acessar
for chave, valor in dados_lucas.items():
    print(chave,"-", valor)