from funcoes import *
import random
random.seed(1)


#define a frota do jogador
frota_jogador = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}   

#define a frota do computador
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

#dicionário com os tamanhos dos navios
tamanhos_navios = { #[qtd, tamanho]
    "porta-aviões": [1, 4], 
    "navio-tanque": [2, 3], 
    "contratorpedeiro": [3, 2], 
    "submarino": [4, 1] 
    } 


#percorre a lista de navios do jogador para colocar no tabuleiro checando se está disponível
for nome, dados in tamanhos_navios.items():
    j = 0
    while j < dados[0]:
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {dados[1]}')	
        linha_atual = int(input("Qual linha deseja colocar o navio? ")) 
        coluna_atual = int(input("Qual coluna deseja colocar o navio? ")) 

        if nome != "submarino":
            orientacao = int(input("Qual orientação deseja colocar o navio? "))
            if orientacao == 1:
                orientacao = "vertical"
            elif orientacao == 2:
                orientacao = "horizontal"
        else:
            orientacao = "horizontal" 

        tamanho = dados[1]

        if posicao_valida(frota_jogador, linha_atual, coluna_atual, orientacao, tamanho):
            preenche_frota(frota_jogador, nome, linha_atual, coluna_atual, orientacao, tamanho)
            j += 1  
        else:
            print("Esta posição não está válida!")

#cria o tabuleiro dos dois jogadores
tabuleiro_oponente= posiciona_frota(frota_oponente)
tabuleiro_jogador= posiciona_frota (frota_jogador)


#cria o looping do jogo 
jogando= True

#cria as listas de onde foram os tiros
tiros_jogador=[]
tiros_oponente=[]


#looping do jogo 
while jogando:

    #faz o tabuleiro usando a função do prof
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    #pergunta ao jogador onde ele quer atirar
    linha_tiro_jogador = int(input("Qual linha deseja atirar? "))
    while linha_tiro_jogador not in list(range(0, 10)):
        print("Linha inválida!")
        linha_tiro_jogador = int(input("Qual linha deseja atirar? "))

    coluna_tiro_jogador = int(input("Qual coluna deseja atirar? "))
    while coluna_tiro_jogador not in list(range(0, 10)):
        print("Coluna inválida!")
        coluna_tiro_jogador = int(input("Qual coluna deseja atirar? "))

    tiro_atual = [linha_tiro_jogador, coluna_tiro_jogador]

    #checa se o tiro e valido e se não for entra em um looping até que fique valido
    while tiro_atual in tiros_jogador:
        print(f"A posição linha {linha_tiro_jogador} e coluna {coluna_tiro_jogador} já foi informada anteriormente!")
        linha_tiro_jogador = int(input("Qual linha deseja atirar? "))
        while linha_tiro_jogador not in list(range(0, 10)):
            print("Linha inválida!")
            linha_tiro_jogador= int(input("Qual linha deseja atirar? "))
        
        coluna_tiro_jogador = int(input("Qual coluna deseja atirar? "))
        while coluna_tiro_jogador not in list(range(0, 10)):
            print("Coluna inválida!")
            coluna_tiro_jogador= int(input("Qual coluna deseja atirar? "))

        tiro_atual= [linha_tiro_jogador, coluna_tiro_jogador]

    tiros_jogador.append(tiro_atual)
    jogada_jogador= faz_jogada(tabuleiro_oponente, linha_tiro_jogador, coluna_tiro_jogador)
    
    #se o jogador não tiver afundado todos os navios do computador, então roda o resto do codigo
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando= False
        break

    
    #ve onde o computador vai atirar
    linha_tiro_oponente = random.randint(0,9)
    coluna_tiro_oponente = random.randint(0,9)
    tiro_atual_oponente = [linha_tiro_oponente, coluna_tiro_oponente]

    #checa se o tiro e valido e se não for entra em um looping até que fique valido
    while tiro_atual_oponente in tiros_oponente:
        linha_tiro_oponente = random.randint(0,9)
        coluna_tiro_oponente = random.randint(0,9)
        tiro_atual_oponente = [linha_tiro_oponente, coluna_tiro_oponente]

    tiros_oponente.append(tiro_atual_oponente)

    #dado que o tiro do computador é valido, imprime no terminal onde ele está atirando
    print(f'Seu oponente está atacando na linha {linha_tiro_oponente} e coluna {coluna_tiro_oponente}')
    
    #faz a jogada colocando nos tabuleiros se acertou na água ou em um barco com "-" e "x"
    jogada_oponente= faz_jogada(tabuleiro_jogador, linha_tiro_oponente, coluna_tiro_oponente)

    #checa se todos os barcos foram afundados do jogadore e se sim encerra o jogo
    if afundados(frota_jogador, tabuleiro_jogador) == 10:
        print('Xi! O oponente derrubou toda a sua frota =(')
        jogando= False
