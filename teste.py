#fazendo um programa que recebe 4 alturas usando um laço de repetição
#e realizando a soma dessas alturas
contador = 1
altura = 0

while contador <= 4:
    altura += float(input("Entre com a altura: "))
    contador += 1
print(f"A soma das alturas é de {altura}")

