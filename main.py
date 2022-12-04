import random

def menu():
    logo = 'JoKenPo';
    linha = '*-*' * 6;
    print(linha);
    print(logo.center(18));
    print(linha);
    regras();
    jogo()
    
    
    
def regras():
    print('''
REGRAS:
1- Você deve escolher entre Pedra, Papel e Tesoura.
2 - A Pedra ganha da Tesoura.
3 - O Papel ganha da Pedra.
4 - A Tesoura ganha do Papel.
    ''')

def jogo():
    lista = ['pedra', 'papel', 'tesoura']
    
    while True:
        
        print('''
        Qual das opções você escolhe?
        [1] - Pedra
        [2] - Papel
        [3] - Tesoura
        ''')
        jogador = int(input('Opção do jogador: '));
        
        lista = ['pedra', 'papel', 'tesoura']
        pc = random.randint(0,2);
        
        if jogador == 1: # Pedra
            jogador = 0
            if jogador == 0: # Pedra
                if pc == 0: # Pedra
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('Deu empate!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
                    
                elif pc == 1: # Papel
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('O PC ganhou!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
                    
                else: # Tesoura
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('O Jogador Ganhou!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
            
            
        elif jogador == 2: # Papel
            jogador = 1;
            if jogador == 1: # Papel
                if pc == 0: # Pedra
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('O Jogador Ganhou!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
                    
                elif pc == 1: # Papel
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('Deu empate!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
                    
                else: # Tesoura
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('O PC ganhou!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
            
            
        elif jogador == 3: # Tesoura
            jogador = 2;
            if jogador == 2: # Tesoura
                if pc == 0: # Pedra
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('O PC ganhou!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
                    
                elif pc == 1: # Papel
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('O Jogador ganhou!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
                    
                else: # Tesoura
                    print(f'O Jogador escolheu: {lista[jogador]}\nO PC escolheu: {lista[pc]}');
                    print('Deu empate!');
                    print('''
                    Deseja Continuar ?
                    [1] - Sim
                    [2] - Não
                    ''')
                    op = int(input('Opção: '));
                    if op == 1:
                        print('Boa partida.')
                    elif op == 2:
                        print('Fim de Jogo!!');
                        break;
                    else:
                        print('''
                        Deseja Continuar ?
                        [1] - Sim
                        [2] - Não
                        ''')
                        op = int(input('Opção: '));
                    
            
        else:
            print('Opção inválida, tente novamente.');
            jogo();


menu();
