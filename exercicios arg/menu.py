def parimpar(): 
    import random
    print('-------PAR OU IMPAR-------')
    jogador = str(input('Digite [PAR] ou [IMPAR]: '))
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









