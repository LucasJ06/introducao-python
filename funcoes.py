#criando uma função para saber o valor de f de x
def f(x):
    return(x + 1)

print(f(4))

#criando uma função para calcular juros compostos
def juros_compostos(aporte, taxa, anos):
    return aporte * (1 + taxa) ** anos

juros_compostos(taxa = 0.13, anos = 4, aporte = 1000)