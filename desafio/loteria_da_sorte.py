"""
Construa um programa que realiza o sorteio de um número entre 1 e 15;
O usuário terá 3 chances de acertar o valor;
A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado;
Caso o usuário acerte, dê os parabéns.
"""

#%%
#importando biblioteca para gerar numero aleatorio
import random

#tratando possíveis erros e atribuindo a uma função
def get_input():
    
    while True:
        try:
            chute = int(input(f"Entre com um numero, {i + 1}° tentativa: "))

        except ValueError as err:
            print("Entre com um numero válido!")
            continue

        if 1 <= chute <= 15:
            return chute
        print("Valor inválido! O valor deve ser entre 1 e 15")

#numero sorteado
numero = random.randint(1, 15)

#tentativas
for i in range(3):
    chute = get_input()

    if chute == numero:
        print("Parabens você acertou!")
        break
    elif chute < numero:
        print(f"O numero é maior que {chute}, você tem {(i - 2) * -1} chances")
    else:
        print(f"O numero é menor que {chute}, você tem {(i - 2) * -1} chances")

else:
    print("Suas tentativas acabaram!")