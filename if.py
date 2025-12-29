#logica para validar se a pessoa é maior de idade ou não
idade = 16

if idade >= 70:
    print("Cuidado com a bebida.")
    print("Consulte seu geriatra!")
elif idade >= 18:
    print("Você pode beber cerveja!")
    print("Beba com moderação")
elif idade == 17:
    print("Você ainda não pode beber cerveja!")
    print("Fique no refri!")
else:
    print("Você não pode beber!")



#programa que vende água
texto = """ 
Escolha a sua água para comprar:
(1) Água mineral natural - R$1,50
(2) Água mineral com gás - R$2,50
"""
opcao = input(texto)
valor_item = 0

if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Entre com a opção correta!")

else: 
    qtde = int(input("Digite a quantidade: "))
    valor_total = valor_item * qtde
    print(f"Sua conta deu {valor_total}")


    

