# Funções Utilizadas

def Formar_Matriz(x):
    '''A funcao recebe x linhas com x entradas, separadas por espaço, e as organiza em uma matriz, ou seja, uma lista de listas'''
    Matriz = []
    for i in range(x):
        entradas = input().split(' ')
        linha = []
        for a in range (x):
            linha.append(int(entradas[a]))
        Matriz.append(linha)
    return Matriz

def supermatriz_comum(G,P,g,p):
    ''' A funcao recebe uma matriz quadrada G de tamanho g 
    e recebe uma matriz quadrada P de tamanho p. (Sendo g > p)
    A funcao retorna uma tupla com o tamanho da menor matriz que contem a matriz G e P.

    No início :(da esquerda pra direita e de cima pra baixo) 
    a funcao busca pela primeira entrada da matirz P que esteja em uma coluna de G
    Sendo as coordenadas dessa entrada (i,j).

    Em seguida: (da direita pra esquerda e de baixo pra cima)
    a funcao busca pela primeira entrada da matirz P que esteja em uma coluna de G
    Sendo as coordenadas dessa entrada (a,b).

    Com isso, a funcao consegue o tamanho da matriz intersecao entra G e P, 
    já que obteve as coordenadas dos vertices opostos dessa matriz. Tamanho = (a - i + 1) x (b - j + 1)

    Assim, a funcao retorna a uniao entra as matrizes : a soma dos tamanhos menos o tamanho da intersecao
    '''
    # Da direita pra esquerda e de cima pra baixo
    for i in range(p):
        for j in range(p):
            for k in range(g):

                if P[i][j] in G[k]: 
                    # Da esquerda pra direita e de baio pra cima
                    for a in range(p-1,i-1,-1):
                        for b in range(p-1,j-1,-1):
                            for c in range (g-1,k-1,-1):

                                if P[a][b] in G[c]: 

                                    colunas_matriz_intersecao = b - j + 1
                                    linhas_matriz_intersecao = a - i + 1

                                    linha_resposta = m + n - linhas_matriz_intersecao
                                    coluna_resposta = m + n - colunas_matriz_intersecao
                                        
                                    return (linha_resposta,coluna_resposta)


# Leitura das entradas e impressao das respostas

while True:
    ordens = input().split(' ')
    m = int(ordens[0])
    n = int(ordens[1])
    if m == 0 and n == 0:
        break # Final do programa
    else:
        M = Formar_Matriz(m)
        N = Formar_Matriz(n)
                                                                           
    if m >= n : 
        resultado = supermatriz_comum(M,N,m,n)                                                                               
    else:
        resultado = supermatriz_comum(N,M,n,m)
    
    p,q = resultado

    print(f'{p} x {q}')
                                                                                                          