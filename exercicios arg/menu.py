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




