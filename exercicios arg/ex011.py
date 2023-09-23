#Crie um programa que receba dois números e mostre na tela se o resultado da multiplicação deles é par ou impar (Sem usar o if).
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resto = (n1 * n2) %2
par = resto == 0
print(f'a multiplicação dos números {n1} e {n2} é: {par}')