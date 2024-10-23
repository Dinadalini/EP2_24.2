def define_posicoes(linha, coluna, orientacao, tamanho):    
    posicoes_lista = []

    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes = [linha, coluna + i]
            posicoes_lista.append(posicoes)

    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes = [linha + i, coluna]
            posicoes_lista.append(posicoes)
    return posicoes_lista


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    
    return frota

def faz_jogada (tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

def posiciona_frota (frota):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    
    for navios in frota.keys():
        for posicoes in frota[navios]:
            for posicao in posicoes:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    navios_afundados = 0

    for navio in frota:
        for navio in frota[navio]:
            afundado = True
            for posicao in navio:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1
    
    return navios_afundados

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    navio_atual = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao_atual in navio_atual:
        linha_atual, coluna_atual = posicao_atual
        if linha_atual < 0 or linha_atual > 9 or coluna_atual < 0 or coluna_atual > 9:
            return False
        
    for navios in frota.values():
        for posicoes in navios:
            for posicao_ocupada in posicoes:
                if posicao_ocupada in navio_atual:
                    return False

    return True

