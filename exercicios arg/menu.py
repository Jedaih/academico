def parimpar(): 
    import random
    print('-------PAR OU IMPAR-------')
    jogador = str(input('Digite [PAR] ou [IMPAR]: ').upper())
    num = int(input('Digite um número: '))
    comp = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    soma = num + comp
    if jogador == 'PAR' and soma % 2==0: #PAR COM 0
        print(f'Você Ganhou, você escolheu {jogador} e o número {num}, o computador escolheu o número {comp}. A soma dos dois números é {soma}.')
    elif jogador == 'IMPAR' and soma % 2==1:#IMPAR COM 1 
        print(f'Você ganhou, você escolheu {jogador} e o número {num}, o computador escolheu o número {comp}. A soma dos dois números é {soma}.')
    elif jogador == 'IMPAR' and soma %2==0: #IMPAR COM 0
        print(f'Você perdeu, você escolheu {jogador} e o número {num}, o computador escolheu o número {comp}. A soma dos dois números é {soma}.')
    else: #PAR COM 1
        print(f'Você perdeu, você escolheu {jogador} e o número {num}, o computador escolheu o número {comp}. A soma dos dois números é {soma}.')
    return
def advsif():#opção do jogo da advinhação sem o if
    import random
    jogador = int(input('escolha um número de 1 a 10 que você acha que a máquina vai jogar: '))
    maquina = random.choice ([0, 1, 2, 3, 4, 5, 6])
    resultado = (maquina == jogador)
    print(resultado)
    return
def advcif():#opção do jogo da advinhação com o if
    import random
    jogador = int(input('Advinhe o número que a máquina vai jogar: (de 1 a 10)'))
    maquina = random.choice([0, 1, 2, 3, 4, 5, 6])
    if(jogador == maquina):
        print(f'você venceu, a maquina jogou {maquina} e você jogou {jogador}.')
    else:
        print(f'Você perdeu, a máquina jogou {maquina} e você jogou {jogador}.')
    return
def media():
    
    while True:
        nomealuno = str(input('Escreva o nome do aluno: '))
        nomeprof = str(input('Digite o nome do professor: '))
        
        if nomealuno == '' or nomeprof == '':
            print("COLOQUE OS NOMES CORRETAMENTE.")
        else:
            break
        
    nota1 = float(input('Digite a nota 1 do aluno: '))
    nota2 = float(input('Digite a nora 2 do aluno: '))
    nota3 = float(input('Digite a nota 3 do aluno: '))
    media = (nota1 + nota2 + nota3)/3
    
    if (media >= 7):
        print(f'O Aluno {nomealuno} foi aprovado pelo Professor {nomeprof} com a média {media}. ')
    elif (media == 6):
        print(f'O Aluno {nomealuno} foi aprovado pelo conselho com a média {media}. ')
    else:
        print(f'O Aluno {nomealuno} foi reprovado pelo Professor {nomeprof} com a média {media}. ')
    return

while True:
    print('Menu: \n'
          '1) Jogo do par ou impar: \n'
          '2) Jogo da advinhação sem o if: \n'
          '3) Jogo da advinhação com o if: \n'
          '4) calcular media: \n'
          '5) Sair do programa: \n')
    
    while True:
        escolha = str(input('Escolha uma das opções acima: '))
        if escolha == '':
            print('Digite apenas uma das opções acima: ')
        elif escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4' and escolha != '5':
            print('Digite apenas uma das opções acima: ')
        else:
            break
    if escolha == '1':
        parimpar()
    elif escolha == '2':
        advsif()
    elif escolha == '3':
        advcif()
    elif escolha == '4':
        media()
    elif escolha == '5':
        break
