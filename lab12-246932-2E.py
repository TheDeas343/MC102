#Definicoes de funcoes

def quadrado(quadro,i,j,l,k):
    ''' Uma função que faz as bordas de um quadrado, com centro em (i,j), recursivamente,
    até completar a área de um quadrado de lado L, dentro dos limites do quadro.

    Isso ocorre utilizando uma matriz quadro alterando de '-' para 'x' suas entradas
    qie estiverem dentro do interalo desse quadrado.

    k representa uma variavel auxiliar da recursão que se inicia com o valor L 
    e vai diminuindo a cada execução da função de 2 em 2 até o valor de 1.
    '''
    if k == 1:
        quadro[i][j] ='x'
    else:
        for n in range(-(l//2),(l//2)+1):
            if j+n>=0 and j+n<len(quadro[0]):
                if i+k//2 < len(quadro):
                    quadro[i+k//2][j+n]= 'x'

                if i-k//2 >=0 :
                    quadro[i-k//2][j+n]= 'x'

            if i+n>=0 and i+n <len(quadro):
                if j+k//2 < len(quadro[0]):
                    quadro[i+n][j+k//2]= 'x'

                if j-k//2 >=0:
                    quadro[i+n][j-k//2]= 'x'
        
        quadrado(quadro,i,j,l,k-2)

def circulo(quadro,i,j,r,k):
    ''' A função faz um círculo levando em conta os pontos que estão na borda de um quadrado 2k+1
    e com centro em (i,j).
    Sendo que k representa uma variavel auxiliar da recursão que se inicia com o valor 'r' 
    e vai diminuindo de 1 em 1 até o valor de 0.

    Se a distancia euclidiana deste ponto ao centro for menor ou igual ao raio r,
    então este ponto faz parte do circulo

    Isso ocorre utilizando uma matriz quadro alterando de '-' para 'x' suas entradas
    que estiverem dentro do intervalo desse círculo.

    Distancia euclidiana de um ponto A = (i +/- k, j +/- k) até o centro (i,j):
    ((i +/- k) - i)**2 + ((j +/- k) - j)**2 = k**2 + n**2
    '''
    if k == 0:
        quadro[i][j] ='x'
    else:
        for n in range(-k,k+1):
            
            if j+n>=0 and j+n<len(quadro[0]):
                if i+k < len(quadro):
                    if k**2 + n**2 <= r**2:
                        quadro[i+k][j+n]= 'x'

                if i-k >=0 :
                    if k**2 + n**2 <= r**2:
                        quadro[i-k][j+n]= 'x'

            if i+n>=0 and i+n <len(quadro):
                if j+k < len(quadro[0]):
                    if n**2 + k**2 <= r**2:
                        quadro[i+n][j+k]= 'x'

                if j-k >=0:
                    if n**2 + k**2 <= r**2:
                        quadro[i+n][j-k]= 'x'
        
        circulo(quadro,i,j,r,k-1)


# Leitura de entradas e execuções das funções

N,M = [int(e) for e in input().split(' ')]
Q = int(input())

quadro=[(M*['-']) for n in range(N)]

for i in range(Q):
    figura,i,j,d = [int(e) if e.isdecimal() else e for e in input().split(' ')]

    if figura == 'quadrado':
        quadrado(quadro,i,j,d,d)
    else:
        circulo(quadro,i,j,d,d)


# Print do quadro

for i in range(len(quadro)):
    for j in range(len(quadro[0])):
        print(quadro[i][j],end=' ')
    print()
