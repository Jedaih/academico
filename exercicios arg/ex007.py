#Crie um algoritmo que tenha como entrada um nome e idade e traga como saída a possibilidade ou não de alistamento militar
nome = str(input('Qual seu nome: '))
idade = int(input('Qual a sua idade: '))

if idade >= 18:
    print(f'{nome} Caso não tenha se alistado, você deve se alistar.')
else:
    print(f'{nome} voce ainda não precisa se alistar.')