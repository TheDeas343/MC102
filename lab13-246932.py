# Definições de funções

def potencia_2(n):

    ''' Função que quecebe um numero 'n' e verifica se este é uma potência de 2.
    Caso seja uma potencia de 2, retorna True e o expoente dessa potência.
    Caso não seja, retorna False e o expoente da maior potencia de 2 menor que 'n'
    '''
    i = 0
    while True :
        
        if n == 2**i:
            return (True,i)
        elif n < 2**i:
            return (False,i-1)

        i += 1 

def submagias(M,N,dic):

    '''Função recebe dois lados de um retângulo e um dicionário vazio.
    Primeiramente, separa os lados em lado maior 'D' e lado menor 'd'.
    
    Por ser uma função de Dividir e Conquistar temos:

    Dividir:
    Se 'D' ou 'd' não forem ambos potências de 2, então a função divide esse retângulo em outros retângulos.
    Sendo um deles o maior retângulo cujo ambos lados sejam potência de 2.
    Os outros retângulos, se houver, serão as partes que sobraram da primeira divisão. 
    Assim, recursivamente aplica submagias nestes demais retângulos.

    Conquistar:
    Caso ambos os lados sejam potência de 2, a função calcula o numero de quadrados de lado 'd' que cabem no retângulo.
    Armazenado esse cálculo como valor de uma chave no dicionário. Esta chave é o expoente da potendia de 2 de 'd'.
    Da forma: dic[i] = quantidade, sendo d == 2**i.

    No final, teremos um dicionário que relaciona o lado do quadrado(potencia de 2) 
    com o número de vezes que ele aparece pra completar o retângulo original.
    '''

    if M >= N:
        D,d = M,N
    else:
        D,d = N,M
    
    ver_D = potencia_2(D) 
    ver_d = potencia_2(d) 

    if  ver_D[0]  and  ver_d[0]  :
        qtd_submagias = D/d
        nivel = ver_d[1] 
        if nivel in dic.keys(): 
            dic[nivel] += int(qtd_submagias)
        else:
            dic[nivel] = int(qtd_submagias) 

    else:
        expd = 2**(ver_d[1])
        expD = 2**(ver_D[1])

        submagias(expd,expD,dic)
        if d-expd != 0:
            submagias(d-expd,D,dic)
            if D-expD !=0:    
                submagias(expd,D-expD,dic)
        else:
            submagias(d,D-expD,dic)
            
# Leitura de entradas e print das saídas

M,N=[int(e) for e in input().split(' ')]

dic = {}
submagias(M,N,dic)

print('---')
print("Grimorio de Teraf L'are")
print('---')


for i in sorted(dic.keys()): # Printar em ordem crescente dos lados dos quadrados de lado 2**i
    print(f'{dic[i]} submagia(s) de nivel {i}')

print('---')

# Cálculo e print do Total de Submagias e o Total de PM

Tsm = 0
TPM = 0

for i in sorted(dic.keys()):
    Tsm += dic[i]
    TPM += (2**i)*dic[i]

print(f'Total de submagia(s) conjurada(s): {Tsm}')
print(f'Total de PM gasto: {TPM}')

print('---')

