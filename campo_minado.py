import os
import numpy as np

rng = np.random.default_rng()

'''
Elementos para melhorar no futuro:

- Arranjar uma maneira mais inteligente e simples de mostrar a quantidade de minas em cada lugar
- Fazer o código funcionar mesmo quando o tiver 1  linha ou 1 coluna
'''



#Programa Principal
def limpa_tela():
    os.system('cls')

def main():
   limpa_tela()
   linhas_colunas()


def opcao_invalida():
    limpa_tela()
    print('Opção inválida, aperte enter para voltar para a pagina inicial')
    input()
    main()

def linhas_colunas():
    try:
        global linhas, colunas
        linhas = int(input('Digite o numero de linhas: '))
        colunas = int(input('Digite o numero de colunas: '))
        selecionando_minas()
    except:
        opcao_invalida()
    
def selecionando_minas():
    global elementos_totais, minas
    elementos_totais = linhas*colunas
    N_minas = int(elementos_totais*0.3)
    minas = rng.choice(elementos_totais, size = N_minas, replace = False)
    minas.sort()
    criar_matriz()

def criar_matriz():
    global matriz, matriz_posicao, matriz_auxiliar
    matriz = []
    matriz_posicao = np.zeros((elementos_totais,), dtype = int)
    
    matriz_auxiliar = np.arange(1, elementos_totais+1)
    matriz_auxiliar = np.array(matriz_auxiliar).reshape(linhas, colunas)
    
    for cont in minas:
        matriz_posicao[cont-1] = 1

    for cont in range(linhas):
        matriz.append(matriz_posicao[cont*colunas:(colunas*(cont+1))])
    
    matriz_posicao = np.zeros((linhas,colunas),dtype = int)

    for l in range(linhas):
        for c in range(colunas):
            if l == 0 and c == 0:
                n_minas_lado = matriz[l] [c+1]  + matriz[l+1] [c] + matriz[l+1] [c+1]
                matriz_posicao[l] [c] = n_minas_lado
                
            elif l == linhas-1 and c == 0:
                n_minas_lado = matriz[l-1] [c]  + matriz[l-1] [c+1] + matriz[l] [c+1]
                matriz_posicao[l] [c] = n_minas_lado

            elif l == 0 and c == colunas-1:
                n_minas_lado = matriz[l] [c-1]  + matriz[l+1] [c] + matriz[l+1] [c-1]
                matriz_posicao[l] [c] = n_minas_lado

            elif l == linhas-1 and c == colunas-1:
                n_minas_lado = matriz[l-1] [c]  + matriz[l-1] [c-1] + matriz[l] [c-1]
                matriz_posicao[l] [c] = n_minas_lado

            elif l == 0 and c > 0 and  c < colunas-1:
                n_minas_lado =  matriz[l] [c-1] + matriz[l] [c+1] + matriz[l+1] [c-1] + matriz[l+1] [c] + matriz[l+1] [c+1]
                matriz_posicao[l] [c] = n_minas_lado

            elif l == linhas-1 and c > 0 and  c < colunas-1:
                n_minas_lado = matriz[l-1] [c-1] + matriz[l-1] [c] + matriz[l-1] [c+1] + matriz[l] [c-1] + matriz[l] [c+1]
                matriz_posicao[l] [c] = n_minas_lado

            elif c == 0 and l > 0 and l < linhas-1:
                n_minas_lado = matriz[l-1] [c] + matriz[l-1] [c+1] + matriz[l] [c+1] +  matriz[l+1] [c] + matriz[l+1] [c+1]
                matriz_posicao[l] [c] = n_minas_lado

            elif c == colunas-1 and l > 0 and l < linhas-1:
                n_minas_lado = matriz[l-1] [c-1] + matriz[l-1] [c] + matriz[l] [c-1] + matriz[l+1] [c-1] + matriz[l+1] [c]
                matriz_posicao[l] [c] = n_minas_lado

            elif l-1 >= 0 and c-1 >= 0 and l+1 <= linhas-1 and c+1 <= colunas-1:
                n_minas_lado = matriz[l-1] [c-1] + matriz[l-1] [c] + matriz[l-1] [c+1] + matriz[l] [c-1] + matriz[l] [c+1] + matriz[l+1] [c-1] + matriz[l+1] [c] + matriz[l+1] [c+1]
                matriz_posicao[l] [c] = n_minas_lado
    tela()

def tela():
    limpa_tela()
    cont = 0
    for aux in matriz_auxiliar:
        for aux2 in aux:
            print(f'{str(aux2).ljust(4)}  ', end='')
        print('\n')
    
    print(matriz)
    print(matriz_posicao)

    e = int(input('Escolha um numero: '))
    teste(e)

def teste(n_escolhido):
    l = int(n_escolhido/colunas )
    c = n_escolhido % colunas - 1

    if c == -1:
        l -= 1
        c = colunas - 1
    
    
    if matriz [l] [c] != 1:
        matriz_auxiliar [l] [c] = matriz_posicao [l] [c]
        tela()
    else:
        print('Você escolheu uma mina. GAME OVER!!!')

if __name__ == '__main__':
    main()
