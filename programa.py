from funcoes import *
import random

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}   

tamanhos_navios = { 
    "porta-aviões": [1, 4], 
    "navio-tanque": [2, 3], 
    "contratorpedeiro": [3, 2], 
    "submarino": [4, 1] 
    } 

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

        if posicao_valida(frota, linha_atual, coluna_atual, orientacao, tamanho):
            preenche_frota(frota, nome, linha_atual, coluna_atual, orientacao, tamanho)
            j += 1  
        else:
            print("Esta posição não está válida!")

frota_oponente = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}
tamanhos_navios_oponente = { 
    "porta-aviões": [1, 4], 
    "navio-tanque": [2, 3], 
    "contratorpedeiro": [3, 2], 
    "submarino": [4, 1] 
    } 

for nome_oponente, dados_oponente in tamanhos_navios_oponente.items():
    j_oponente = 0
    while j_oponente < dados_oponente[0]:	
        linha_atual_oponente = random.randint(0,9) 
        coluna_atual_oponente = random.randint(0,9) 
        if nome_oponente != "submarino":
            orientacao_oponente = random.randint(1,2) 
            if orientacao_oponente == 1:
                orientacao_oponente = "vertical"
            elif orientacao_oponente == 2:
                orientacao_oponente = "horizontal"
        else:
            orientacao_oponente = "horizontal" 

        tamanho_oponente = dados_oponente[1]

        if posicao_valida(frota_oponente, linha_atual_oponente, coluna_atual_oponente, orientacao_oponente, tamanho_oponente):
            preenche_frota(frota_oponente, nome_oponente, linha_atual_oponente, coluna_atual_oponente, orientacao_oponente, tamanho_oponente)
            j_oponente += 1  

tabuleiro_oponente= posiciona_frota(frota_oponente)
tabuleiro_jogador= posiciona_frota (frota)

jogando= True
tiros_jogador=[]
tiros_oponente=[]

while jogando:

    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto

    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    linha_tiro_jogador= int(input("Qual linha deseja atirar? "))
    linha_tiro_oponente= random.randint(0,9)
    # while linha_tiro_jogador < 0 or linha_tiro_jogador > 9:
    while linha_tiro_jogador not in [0,1,2,3,4,5,6,7,8,9]:
        print("Linha inválida!")
        linha_tiro_jogador= int(input("Qual linha deseja atirar? "))

    coluna_tiro_jogador= int(input("Qual coluna deseja atirar? "))
    coluna_tiro_oponente= random.randint(0,9)
    # while coluna_tiro_jogador < 0 or coluna_tiro_jogador > 9:
    while coluna_tiro_jogador not in [0,1,2,3,4,5,6,7,8,9]:
        print("Coluna inválida!")
        coluna_tiro_jogador= int(input("Qual coluna deseja atirar? "))

    
    tiro_atual= [linha_tiro_jogador, coluna_tiro_jogador]
    tiro_atual_oponente= [linha_tiro_oponente, coluna_tiro_oponente]
    while tiro_atual in tiros_jogador:
        print(f"A posição linha {linha_tiro_jogador} e coluna {coluna_tiro_jogador} já foi informada anteriormente!")
        linha_tiro_jogador= int(input("Qual linha deseja atirar? "))
        # while linha_tiro_jogador < 0 or linha_tiro_jogador > 9:
        while linha_tiro_jogador not in [0,1,2,3,4,5,6,7,8,9]:
            print("Linha inválida!")
            linha_tiro_jogador= int(input("Qual linha deseja atirar? "))
        
        coluna_tiro_jogador= int(input("Qual coluna deseja atirar? "))
        # while coluna_tiro_jogador < 0 or coluna_tiro_jogador > 9:
        while coluna_tiro_jogador not in [0,1,2,3,4,5,6,7,8,9]:
            print("Coluna inválida!")
            coluna_tiro_jogador= int(input("Qual coluna deseja atirar? "))

        tiro_atual= [linha_tiro_jogador, coluna_tiro_jogador]
    tiros_jogador.append(tiro_atual)

    while tiro_atual_oponente in tiros_oponente:
        linha_tiro_oponente= random.randint(0,9)
        coluna_tiro_oponente= random.randint(0,9)
        tiro_atual_oponente= [linha_tiro_oponente, coluna_tiro_oponente]
    tiros_oponente.append(tiro_atual_oponente)

    print(f'Seu oponente está atacando na linha {linha_atual_oponente} e coluna {coluna_atual_oponente}')
    
    jogada_jogador= faz_jogada(tabuleiro_oponente, linha_tiro_jogador, coluna_tiro_jogador)
    jogada_oponente= faz_jogada(tabuleiro_jogador, linha_tiro_oponente, coluna_tiro_oponente)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando= False
    if afundados(frota, tabuleiro_jogador) == 10:
        print('Xi! O oponente derrubou toda a sua frota =(')
        jogando= False
