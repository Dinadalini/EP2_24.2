def define_posicoes (linha, coluna, orientacao, tamanho):
    posicoes_lista = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes = [linha, coluna+i]
            posicoes_lista.append(posicoes)
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes = [linha+i, coluna]
            posicoes_lista.append(posicoes)
    return posicoes_lista

def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    
    return frota

print (preenche_frota({'porta-aviões': [[[1, 2], [2, 2], [3, 2], [4, 2]], [[0, 4], [1, 4], [2, 4], [3, 4]]]}, 'contratorpedeiro', 5, 4, 'vertical', 2))
