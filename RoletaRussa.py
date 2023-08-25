import random
import os

number = random.randint(1,10)

numero = input("Digite um numero de 1 a 10:")
numero = int(numero)

caminho = ("")# caminho do arquivo, arrumar a \ para / 


if numero == number:
    print('Parabens voce acertou!')
else:
    os.remove(caminho)