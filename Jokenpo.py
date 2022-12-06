import random

#Variáveis

maxima_tentativa = 0;
lista_jogo = ['Pedra', 'Papel', 'Tesoura'];
op = 0;

# PC
pc = random.randint(0,2);


def jogo():
    print('''
Escolha uma das opções:
[1] - Pedra
[2] - Papel
[3] - Tesoura
    ''')
    op = int(input('Você Escolhe: '))
    
    if op == 1:
        op = 0;
        resultado();
    elif op == 2:
        op = 1;
        resultado();
    elif op == 3:
        op = 2;
        resultado();
    else:
        print('Opção inválida, tente novamente.')
        jogo();



def resultado():
    # Pedra
    if op == 0:
        #Pedra
        if pc == 0:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nDeu empate.');
        #Papel
        elif pc == 1:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nPC ganhou.');
        #Tesoura
        else:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nJogador ganhou.');
    
    # Papel
    if op == 1:
        #Pedra
        if pc == 0:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nJogador ganhou.');
        #Papel
        elif pc == 1:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nDeu empate.');
        #Tesoura
        else:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nPC ganhou.');
            

    # Tesoura
    if op == 1:
        #Pedra
        if pc == 0:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nPC ganhou.');
        #Papel
        elif pc == 1:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nJogador ganhou.');
        #Tesoura
        else:
            print(f'Você jogou: {lista_jogo[op]}\nPC jogou: {lista_jogo[pc]}\nDeu empate');
    
    jogar_novamente();
    
def jogar_novamente():
    print('''
    Quer jogar novamente?
    [1] - Sim
    [2] - Não
    ''')
    opcao = int(input('Sua escolha: '))
    if opcao == 1:
        jogo();
    elif opcao == 2:
        print('Fim de jogo!');
    else:
        print('Opção inválida, tenta novamente.');
        jogar_novamente();



jogo();