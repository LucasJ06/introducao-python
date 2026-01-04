import requests #para realizar requisições na web
import json #para tratar listas/dicionarios para arquivos
from tqdm import tqdm #para medir progresso
import pandas as pd

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",
    "58038200"
]

#endereço da requisição
url = "https://viacep.com.br/ws/{cep}/json/"

#armazenando o resultado da requisição com base nos ceps em uma lista
dados = []

dataset = pd.DataFrame(dados) #transformando os dados em dataframe
dataset.to_csv("ceps.csv", sep = ";") #exportando para csv

#realizando a requisição e salvando em json
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep = i))
    if resposta.status_code == 200:
        dados.append(resposta.json()) 
dados

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4) 

