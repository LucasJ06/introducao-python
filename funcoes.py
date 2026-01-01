#criando uma função para saber o valor de f de x
def f(x):
    return(x + 1)

print(f(4))

#criando uma função para calcular juros compostos
def juros_compostos(aporte:int, taxa:float, anos:int) -> float:
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

#%%
#criando uma funcao que nao recebe parametro
def ola_mundo():
    print("Boas vindas! Olá para você!")

ola_mundo()

#funcao que retorna se o numero é par ou impar
def par_impar (numero: int)-> str:
    if numero % 2 == 0:
        print(f"O numero {numero} é par")
    else:
        print(f"O numero {numero} é impar")

numero = int(input("Entre com um numero para verificar se ele é par ou impar: "))

par_impar(numero)

#funcao de soma
def soma(a:float, b:float)-> float:
    return a + b

#funcao de media usando a funcao de soma
def media(a:float, b:float)-> float:
    return soma(a,b) / 2

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

print(f"Média: {media(a,b)}")


#%%
#criando funcao de soma com n argumentos

def soma(a:float, b:float, *args)-> float:
    valores = [a,b] + list(args) 
    return sum(valores)

#%%
#criando funcao de media com n argumentos
def media(a:float, b:float, *args)-> float:
    return soma(a, b, *args) / (len(args) + 2)

#%%
a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
d = float(input("Entre com o valor de d: "))
print(f"Média: {media(a,b)}")