# Jokenpo

import random


#Lista do Jogo
lista_jokenpo = ['Pedra', 'Papel', 'Tesoura'];


def pula():
    print('\n')


while True:

    #variavel PC
    pc = random.randint(0,2);

    print('''
    Escolha uma das opções:
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
    ''')
    op = int(input('Indique aqui: '));

    #Pedra
    if op == 1:
        op = 0
        # Pedra
        if pc == 0:
            pula();
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('Deu empate!')
            pula();
        # Papel
        if pc == 1:
            pula();
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('PC ganhou!')
            pula();

        # Tesoura
        if pc == 2:
            pula();
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('Você ganhou!')
            pula();

    #Papel
    elif op == 2:
        op = 1
        # Pedra
        if pc == 0:
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('Você ganhou!')
        # Papel
        if pc == 1:
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('Deu empate!')

        # Tesoura
        if pc == 2:
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('PC ganhou!')

    #Tesoura
    elif op == 2:
        
        if pc == 0:
            
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('PC ganhou!')
        # Papel
        if pc == 1:
            
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('Você ganhou!')

        # Tesoura
        if pc == 2:
            
            print(f'Você escolheu: {lista_jokenpo[op]}')
            print(f'PC escolheu: {lista_jokenpo[pc]}')
            print('Deu empate!')
