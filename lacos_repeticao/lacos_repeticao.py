count = 1 #contador para sair do laco de repeticao
while count < 10:
    print("Entrei no laço", count)
    count = count + 1


#tabuada
numero = int(input("Entre com um número para fazer a tabuada: "))
contador = 0

while contador <= 10:
    print(numero, "*" ,contador, "=" , numero * contador)
    contador += 1


#numeros divisiveis por 4 em um range de 4 - 100 com while
contador = 4
while contador <= 100:
    resto = contador % 4
    if resto == 0:
        print(contador)
    
    contador += 1

#numeros divisiveis por 4 em um range de 4 - 100 com for
for i in range (4, 101):
    if i % 4 == 0:
        print(i)


#fazendo um programa que recebe 4 alturas usando um laço de repetição
#e realizando a soma dessas alturas utilizando o while
contador = 1
altura = 0

while contador <= 4:
    altura += float(input("Entre com a altura: "))
    contador += 1
print(f"A soma das alturas é de {altura}")


#fazendo um programa que recebe 4 alturas usando um laço de repetição
#e realizando a soma dessas alturas utilizando o for
soma = 0

for i in range(4):
    altura = float(input(f"Digite a altura {i + 1}: "))
    soma += altura
print(f"A soma das alturas é de {soma}")


'''
Fazendo um programa que recebe uma quantidade indefinida de valores correspondentes a "saldo em conta",
mas quando o usuario apertar "enter" sem digitar valor algum, o programa para de receber valores, 
e exibe a soma de todos os valores digitados anteriormente. 
'''

saldo_conta = 0

while True:
    valor = input("Entre com um valor ou digite enter para sair: ")
    
    if valor == "":
        break
    
    saldo_conta += float(valor)    

print(f"Saldo total {saldo_conta}")

#contando quantas letras A tem no input
nome = input("Entre com um nome para contar a quantidade de letra A: ")
contador = 0
for i in nome:
    if i in ("A", "a"):
        contador +=1
print(contador)


