#Crie um algoritmo que receba o nome de aluno e 3 notas de provas e tenha como saída a seguinte frase, "o nome do aluno e a média."
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
media = (nota1 + nota2 + nota3) / 3
if (media >= 6):
    
    print(f'Aluno aprovado')
else:
    print(f'Aluno Reprovado')

print(f'o {nome} teve como média: {media}')