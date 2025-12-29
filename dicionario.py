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

#%%
#acessando os elementos do dicionario
print(dados_lucas["formacao"][-1])
print(dados_lucas["cargos"][-1]["empresa"])