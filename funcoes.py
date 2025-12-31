#criando uma função para saber o valor de f de x
def f(x):
    return(x + 1)

print(f(4))

#criando uma função para calcular juros compostos
def juros_compostos(aporte, taxa, anos):
    """
    juros compostos serve para calcular o retorno financeiro a partir de um aporte.
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para 
    calculo do valor a ser retornado.

    aporte:
        um numero inteiro, que represente o valor em reais
    
    taxa:
        um numero entre 0 e 1 que represente o valor da taxa de juros

    anos:
        um numero inteiro >= 1 que representa o tempo que o investimento 
        tera liquidez
    """
    return aporte * (1 + taxa) ** anos

juros_compostos(taxa = 0.13, anos = 4, aporte = 1000)