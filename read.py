#forma menos usual de abrir um arquivo usando py
#atribuindo o caminho do arquivo a uma variavel
arquivo = "C:/introducao_python/arquivos/historia.txt"

#abrindo o arquivo
open_file = open(arquivo)
print(open_file)

#lendo o conteudo do arquivo
conteudo = open_file.read()
print(conteudo)

#fechando o arquivo
open_file.close()


#forma mais usual
#atribuindo o caminho do arquivo a uma variavel
arquivo = "C:/introducao_python/arquivos/historia.txt"

"""
enquanto o arquivo estiver aberto, atribua-o para a variavael
open_file e execute o que estiver dentro do escopo do with.
Nesse caso o escopo do with tem a leitura do arquivo.
"""
with open(arquivo) as open_file:
    conteudo = open_file.read()
print(conteudo)

