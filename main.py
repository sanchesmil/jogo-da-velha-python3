def jogoDaVelha(jogador1,jogador2):
    tabuleiro = [1,2,3,4,5,6,7,8,9]
    quadradoMagico = [4,9,2,3,5,7,8,1,6]
    
    def imprimeTabuleiro():
        print()
        print('',tabuleiro[0],"|",tabuleiro[1] ,"|",tabuleiro[2])
        print("---|---|---")
        print('',tabuleiro[3],"|",tabuleiro[4] ,"|",tabuleiro[5])
        print("---|---|---")
        print('',tabuleiro[6],"|",tabuleiro[7] ,"|",tabuleiro[8])
        print()      
        
    def pegarNumero():
        while True:
            numero = input()
            try:
                numero = int(numero)
                if numero in range(1,10):
                    return numero
                else:
                    print('O valor informado deve ser um número entre 1 e 9. Tente novamente.')
            except ValueError:
                print('O valor informado deve ser um número entre 1 e 9. Tente novamente')
                continue               
        
    def marcarJogada(jogador):
        posicao_escolhida = pegarNumero() - 1
        
        if tabuleiro[posicao_escolhida] == "X" or tabuleiro[posicao_escolhida] == "O":
            print('A posição escolhida já possui um valor, escolha outro número.')
            marcarJogada(jogador)  
        else: 
            tabuleiro[posicao_escolhida] = jogador
        
    def checaVitoria(jogador):
        jogadas = 0
        
        global vitorias_X
        global vitorias_O
    
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if tabuleiro[x] == jogador and tabuleiro[y] == jogador and tabuleiro[z] == jogador:
                            if quadradoMagico[x] + quadradoMagico[y] + quadradoMagico[z] == 15:
                                
                                if jogador == 'X':
                                    vitorias_X += 1
                                else:
                                    vitorias_O += 1
                                print('Jogador ',jogador, ' ganhou! \n')                                
                                return True
    
        for i in range(9):
            if tabuleiro[i] == 'X' or tabuleiro[i] == 'O':
                jogadas+=1    
            if jogadas == 9:
                print('Partida empatada! \n')
                return True        
            
    while True:
        
        imprimeTabuleiro()
        acabou = checaVitoria(jogador1)
        if acabou == True:
            break
        print('Jogador', jogador2 ,', escolha um espaço.')
        marcarJogada(jogador2)

        imprimeTabuleiro()
        acabou = checaVitoria(jogador2)
        if acabou == True:
            break
        print('Jogador', jogador1 ,', escolha um espaço.')
        marcarJogada(jogador1)
        
    if input('Deseja jogar novamente? (S/N)').upper() == 'S':
        print()
        
        if jogador1 == 'X':
            jogador1 = 'O'
            jogador2 = 'X'
        else:
            jogador1 = 'X'
            jogador2 = 'O'
            
        jogoDaVelha(jogador1, jogador2)
    else:   
        print('Fim de Jogo')
        print()
        print('Pontuação Final: \n Jogador X: ', vitorias_X, '\n Jogador O: ',vitorias_O)
        print()
        

## inicia o jogo da velha
    
print('Bem vindo ao jogo da velha')

jogador1 = 'O'
jogador2 = 'X'

vitorias_X = 0
vitorias_O = 0

jogoDaVelha(jogador1,jogador2)