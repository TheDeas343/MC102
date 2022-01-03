#TODAS AS FUNCOES

# Definir as funcoes que ordenam os caracteres segundo um padrão.

def minuscula(x):
    ''' Faz a contagem de letras minusculas em um determinado string.'''

    conta = 0

    for i in range (len(list(x))):
        if list(x)[i] != " " and list(x)[i].islower():
            conta += 1
            
    return conta

def maiuscula(x):
    ''' Faz a contagem de letras maiusculas em um determinado string.'''

    conta = 0

    for i in range (len(list(x))):
        if list(x)[i] != " " and list(x)[i].isupper():
            conta += 1
            
    return conta

def alfabeto(x):
    ''' Faz a contagem de letras do alfabeto em um determinado string.'''

    conta = 0

    for i in range (len(list(x))):
        if list(x)[i] != " " and list(x)[i].isalpha():
            conta += 1
            
    return conta
    
def palavras(x):
    ''' Faz a contagem de palavras em um determinado string.'''

    conta = 1 # Se ha N espaços entao ha N+1 palavras, ja que eles estao entre palavras

    for i in range (len(list(x))):
        if list(x)[i] == " ":
                conta += 1
            
    return conta
    
def ASCII(x):
    ''' Faz a soma das letras em abse ACII em um determinado string.'''

    conta = 0

    for i in range (len(list(x))):
        conta += ord(list(x)[i])
            
    return conta

#Definir as funcoes que oganizaram as entradas de acordo com o dia da semana

def Segunda(x):
    '''Ordenar em forma crescente com base no numero de letras minusculas.'''
    
    crescente = sorted(x,key = minuscula)
    return crescente

def Terca(x):
    '''Ordenar em forma decrescente com base no numero de letras maisculas.'''
    
    decrescente = sorted(x,key = maiuscula, reverse = True)
    return decrescente

def Quarta(x):
    '''Ordenar em forma crescente com base no numero de letras do alfabeto.'''
    
    crescente = sorted(x,key = alfabeto)
    return crescente

def Quinta(x):
    '''Ordenar em forma crescente com base no numero de palavras.'''
    
    crescente = sorted(x,key = palavras)
    return crescente

def Sexta(x):
    '''Ordenar em forma decrescente com base no soma dos valores ASII dos caracteres.'''
    
    decrescente = sorted(x,key = ASCII, reverse = True)
    return decrescente


# LEITURAS DE ENTRADAS
dia_n = input().split(" ")

dia = dia_n[0]
n = int(dia_n[1])

enderecos = []
for i in range (n):
    local = input()
    enderecos.append(local)


# Relacionar o dia com a funcao a ser usada
if dia == "Segunda":
    lista_print = Segunda(enderecos)

elif dia == "Terca":
    lista_print = Terca(enderecos)

elif dia == "Quarta":
    lista_print = Quarta(enderecos)

elif dia == "Quinta":
    lista_print = Quinta(enderecos)
       
else:
    lista_print = Sexta(enderecos)

# Printar
for i in range(len(enderecos)):
    print(lista_print[i])


