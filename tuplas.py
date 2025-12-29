#%%
#criando uma tupla
tupla_lucas = (22, 1, "Solteiro", "Data Engineer", ["Maria", "Antonia", "Ana Julia"])
print(type(tupla_lucas))
print(tupla_lucas)

#%%
#acessando elementos da tupla
tupla_lucas[-1][1:]

#%%
#a tupla não pode ser alterada, mas a lista dentro da tupla pode
tupla_lucas[-1].append("Carolina")
print(tupla_lucas)