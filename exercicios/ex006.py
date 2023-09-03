#Crie um programa que receba o ano atual e o ano em que você nasceu e traga como saída a sua idade.
ano_atual = int(input('Digite o ano atual: '))
ano_nasc = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nasc
print(f'estamos em {ano_atual}  e você nasceu em {ano_nasc} então sua idade é: {idade}')