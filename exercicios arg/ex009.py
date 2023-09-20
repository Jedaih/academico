#Crie um game do par ou impa. Esse programa deve receber a palavra par ou ímpar e um número de escolha do usuário, esse número será somado a um número escolhido pelo computador e a saída será a seguinte:
#a.	Se a palavra escolhida for par e a soma for par “você ganhou”
#b.	Se a palavra escolhida for ímpar e a soma for ímpar “você ganhou”
#c.	Se a palavra for par e a soma for ímpar “você perdeu”
#d.	Se a palavra for ímpar e a soma for par “você perdeu”
#Dica: usar biblioteca Random (comando) import random usar and, or, not

#Ramdom choice ([0,1,2,3,4,5,6,7,8,9,10])
import random

print('*DIGITE MAIUSCULO*')
escjogador = str(input('Escolha [PAR] ou [IMPAR]: '))
numjogador = int(input('Digite o seu número: '))
numcomp = random.choice ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
soma = numjogador + numcomp
if soma %2 == 0 and escjogador == 'PAR':
    print(f'Você escolheu: {escjogador} e o número: {numjogador}, a máquina jogou {numcomp}: Você venceu. ')
elif soma %2 == 1 and escjogador == 'PAR':
    print(f'Você escolheu: {escjogador} e o número: {numjogador}, a máquina jogou {numcomp}: Você perdeu. ')
elif soma %2 == 0 and escjogador == 'IMPAR':
    print(f'Você escolheu: {escjogador} e o número: {numjogador}, a máquina jogou {numcomp}: Você perdeu ')
elif soma %2 == 1 and escjogador =='IMPAR':
    print(f'Você escolheu: {escjogador} e o número: {numjogador}, a máquina jogou {numcomp}: Você venceu ')

    