from funcoes import *

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}   

tamanho_navio={"porta-aviões":[1, 4], "navio-tanque":[2, 3], "contratorpedeiro":[3, 2], "submarino":[4, 1]} #[qtd, tamanho]

for nome, dados in tamanho_navio.items():
    j=1
    while j<=dados[0]:
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {dados[1]}')	
        linha_atual= int(input("Qual linha deseja colocar o navio? "))
        coluna_atual= int(input("Qual coluna deseja colocar o navio? "))
        if nome!= "submarino":
            orientacao = int(input("Qual orientação deseja colocar o navio? "))
            if orientacao==1:
                orientacao="vertical"
            elif orientacao==2:
                orientacao="horizontal"
        #navio_atual_define_posicoes = define_posicoes(linha_atual, coluna_atual, orientacao, dados[1])
        tamanho= dados[1]
        #print(tamanho)
        navio_atual_posicao_valida = posicao_valida(frota, linha_atual, coluna_atual, orientacao, tamanho)
        if navio_atual_posicao_valida== True:
            #dado true, tem colocar as posicoes ocupadas na lista de posicoes da frota
            j+=1
        else:
            print("Esta posição não está válida!")



    
