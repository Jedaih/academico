#Crie um programa que receba um nome e uma idade, mostre os dois na tela e posteriosmente diga se a pessoa deve se alistar ou não.
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
alistar = idade >= 18
print(f'Seu nome é: {nome} e sua idade: {idade} e você deve se alistar: {alistar}')