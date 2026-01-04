#%%
#atribuindo o arquivo a uma variavel
arquivo = "C:/introducao_python/arquivos/data.csv"

#%%
#lendo, processando e fechando o arquivo
with open(arquivo) as open_file:
    lines = open_file.readlines()
print(lines)

#%%
#percorrendo os dados que estao em formato de lista
for i in lines:
    print(i)

#%%
#criando um dicionario vazio
dados = dict()

#%%
#coletando as chaves para criar um dicionario com base nos dados
chaves = lines[0].strip("\n").split(";")
print(chaves)

#%%
#percorrendo a lista criada acima e atribuindo uma lista vazia para cada chave
for i in chaves:
    dados[i] = []
dados

#%%
#percorrendo cada registro dos meus dados e adicionando os registros no dicionario
for l in lines[1:]:
    valores = l.strip("\n").split(";")
    
    for i in range(0, len(valores)):
        dados[chaves[i]].append(valores[i])
dados  

#%%
#descobrindo a media de idade

idade = []

for i in dados["idade"]:
    idade.append(int(i))

media = sum(idade)/len(idade)
print(media)






