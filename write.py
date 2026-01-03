#%%
#atribuindo o caminho do arquivo a uma variavel
arquivo = "C:/introducao_python/arquivos/historia_2.txt"

#%%
#texto que sera usado no modo escrita
txt = "Esqueci o nome do arquivo\n"

#%%
#abrindo o arquivo
with open(arquivo, mode="a") as open_file:
    open_file.write(txt)