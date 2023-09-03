#Crie um programa que faça a multiplicação de dois números e traga a saída se o resultado é par ou impar.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resul = n1 * n2
par = resul % 2
print(f'o resultado da multiplicação é {resul} e é um número {par}')
