"""
Escrevendo um programa que recebe uma lista de numeros
do usuario e conte quantas vezes um numero especifico aparece na lista.
"""

lista_numeros = [] #os numeros digitados serão armazenados aqui
contador = 0 #contando quantos numeros foram imputados

while True:
    numeros = input(f"Entre com o {contador + 1}° número ou digite sair: ")
    if numeros == "sair":
        break
    contador += 1
    lista_numeros.append(int(numeros))


repetidos = 0 #contando quantas vezes o numero escolhido foi digitado no laço while
contar_num = int(input("Qual número você quer contar? "))
for i in lista_numeros:
    if i == contar_num:
        repetidos += 1

print(f"O número {contar_num} aparece {repetidos} vez(es)")
print(lista_numeros)


"""programa que recebe idade"""

idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

#mostrando algumas estatisticas com base nas idades recebidas
media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtd = len(idades)

print(f"Média {media}")
print(f"Minimo {minimo}")
print(f"Maximo {maximo}")
print(f"Qtde {qtd}")