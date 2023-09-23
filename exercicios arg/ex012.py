#Crie o jogo da advinhação, esse jogo deve receber seu nome e um número, esse número será comparado com um número escolhido pela máquina, se você advinhar o número escolhido pela máquina você ganhou, senão, você perdeu.
import random
nome = str(input('Digite seu nome: '))
numjogador = int(input('Digite um número de 0 a 10: '))
numcomp = random.choice ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
if numjogador == numcomp:
    print(f'{nome}, você escolheu o número {numjogador} e a máquina escolheu {numcomp}, você ganhou!!!')
else:
    print(f'{nome}, você escolheu o número {numjogador} e a máquina escolheu {numcomp}, você perdeu!!!')