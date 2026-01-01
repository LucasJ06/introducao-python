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

#Fazendo programa que recebe o nome de uma fruta e devolve o valor:
fruta = input("Entre com o nome da fruta: ").upper()

frutas = {
    "PERA": "R$1,25",
    "GOIABA": "R$2,15",
    "ABACAXI": "R$3,20",
    "JACA": "R$5,80",
    "LARANJA": "R$0,65",
    "LIMÃO": "R$1,25",
    "MAÇÃ": "R$1,50",
    "BANANA": "R$2,75",
    "UVA": "R$1,90"
}
if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor valido!")

#criando programa que conta quantas vezes a frase imputada se repete

dados = {}
contador = 0
while True:
    frase = input(f"Entre com a {contador + 1}° frase: ")
    if frase == "":
        break
    contador += 1

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1
for i, j in dados.items():
    print(i,"->", j)