#Crie um programa que receba o nome de aluno e duas notas e traga como saída a seguinte informação:
#a.	Se a média for menor que 7, o aluno reprova
#b.	Se a média estiver entre 7 e 8 o aluno está aprovado, porém está na média
#c.	Se a média estiver entre 8,5 e 10 o aluno está aprovado com excelência

nome = str(input('Qual o nome do aluno: '))
n1 = float(input('Qual a primeira nota do aluno ?: '))
n2 = float(input('Qual a primeira nota do aluno ?: '))
n3 = float(input('Qual a primeira nota do aluno ?: '))
media = (n1 + n2 + n3) / 3

if media <= 7:
    print('Você foi Reprovado.')
elif media > 7 and media < 8.5:
    print('Parabéns, você foi aprovado, porém ficou na média.')
elif media > 8.5:
    print('Parabéns, você foi aprovado com excelência.')
