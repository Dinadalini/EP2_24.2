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
    frota = {
    "porta-aviões":[
      [[],[],[],[]]
    ],
    "navio-tanque":[
      [[],[],[]],
      [[],[],[]]
    ],
    "contratorpedeiro":[
      [[],[]],
      [[],[]],
      [[],[]]
    ],
    "submarino": [
      [[]],
      [[]],
      [[]],
      [[]]
    ],
}