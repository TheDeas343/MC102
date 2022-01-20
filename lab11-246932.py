# Definições de funcoes

def Maior_Dist(Esconderijos,y):
    '''Dado o lista dos esconderijos e uma coordeana de y, 
    a função cálcula todas as distâncias ao quadrado(para melhor otimização) entre essa coordenada e os esconderijos
    devolvendo a maior dessas distancias.
    '''
    maior_dist = (Esconderijos[0][1] -y )**2 + (Esconderijos[0][0])**2

    for p in Esconderijos[1::]:
        dist = (p[1] - y )**2 + (p[0] )**2
        if dist > maior_dist:
            maior_dist = dist
    return maior_dist

def Distancia(Max_Dists,Esconderijos,y):
    ''' Dado uma lista de Distancias Maximas para cada coordenada no eixo y,
    se houver uma distancia ja calculada a funçao devolve essa distancia,
    do contrário ela calcula a maior distancia pela funcao Maior_Dist,
    além de adicionar essa distancia calculada na posicao certa da lista de Distancias Maximas.
    '''
    if Max_Dists[y] != 0 :
        return Max_Dists[y] 
    else:
        dist = Maior_Dist(Esconderijos,y)
        Max_Dists[y] = dist
        return  dist

def Minimizar(Esconderijos,Y):
    '''A partir da analise da lista Max_Dists, percebe-se que esta segue um padrão:
    A lista é decrescente até o menor valor e depois crescente apos o menor valor (côncava para cima).

    Com isso, essa funçao faz uma busca em uma lista que estará ordenada, com um método similar a busca binária:
    Começando do meio da lista e sempre calculando as distancias de um ponto do meio o da direita e da esquerda, 
    para saber como a lista de comporta naqeuele ponto:
    crescente pou  decrescente.

    Assim, a função vai pegando os pontos médios para a analise, o que otimiza drasticamente a execução do código.

    Quando acha um ponto médio em que os pontos a esquerda e a direita são maiores, 
    então este ponto é o ponto de mínimo, então a função printa o Y desse ponto.
    '''
    Max_Dists = [0]*(Y)

    e = 1 #esquerda
    d = (Y-1) #direita
    while e <= d:
        m = (e+d)//2
        dm = Distancia(Max_Dists,Esconderijos,m) # distancia do meio
        
        if m + 1 < Y and m-1 > 0:
            de = Distancia(Max_Dists,Esconderijos,m-1) # distancia a esquerda do meio
            dd = Distancia(Max_Dists,Esconderijos,m+1) # distancia a direita do meio

            if dm < de and dm < dd:
                Yi = m
                print(Yi)
                break
            elif dm > de and dm < dd:
                d = m - 1
            elif dm < de and dm > dd:
                e = m + 1
                    
        else: # Se os calculos chegaram nos extremos da lista, então um dos extremos é o valor máximo
            Yi = e
            for d in range(e,d+1):
                if Max_Dists[d] < Max_Dists[Yi]:
                    Yi = d 
            print(Yi)
            break


# Leitura de entradas
while True:
    N,Y = [int(i) for i in input().split(' ')]

    if N == 0:
        break
    else:
        Esconderijos = []
        for n in range(N):
            p = tuple(int(i) for i in input().split(' '))
            Esconderijos.append(p)
    
# Calcular e printar as saídas
    Minimizar(Esconderijos,Y)           