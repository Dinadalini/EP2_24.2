from funcoes import * 

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}   

tamanho_navio = { 
    "porta-aviões": [1, 4], 
    "navio-tanque": [2, 3], 
    "contratorpedeiro": [3, 2], 
    "submarino": [4, 1]
} 

for nome, dados in tamanho_navio.items():
    j = 0
    while j < dados[0]:
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {dados[1]}')	
        linha_atual = int(input("Qual linha deseja colocar o navio? ")) - 1
        coluna_atual = int(input("Qual coluna deseja colocar o navio? ")) - 1

        if nome != "submarino":
            orientacao = int(input("Qual orientação deseja colocar o navio? [1] Vertical [2] Horizontal > "))
            if orientacao == 1:
                orientacao = "vertical"
            elif orientacao == 2:
                orientacao = "horizontal"
            else:
                print("Orientação inválida! Tente novamente.")
                continue 
        else:
            orientacao = "horizontal" 

        tamanho = dados[1]

        if posicao_valida(frota, linha_atual, coluna_atual, orientacao, tamanho):
            preenche_frota(frota, nome, linha_atual, coluna_atual, orientacao, tamanho)
            j += 1  
        else:
            print("Esta posição não está válida!")

print(frota)