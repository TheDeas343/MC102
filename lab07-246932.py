# Definir as funções que serão usadas


# Codificar

def ASCII(mensagem):
    """ Transforma cada caracter de uma mensagem para ASCII e devolve uma lista com esses valores."""

    ASCII = [] # Listar as letras em formato ASCII 
    for a in mensagem:
        ASCII.append(str(ord(a)))
    return ASCII

def codificar_impar(mensagem,enxerto):
    """ Codifica uma mensagem passando para ASCII e a retorna em base HEXADECIMAL, com letras maiusculas.
    O enxerto é para o que o programa saiba identificar exatamente o que esta tentando decodificar.
    """
    #Transformar para ASCII
    a = ASCII(mensagem)
    
    # Codificar para a base hexadecimal
    Codificado = []
    for b in a:
        hexa = "{:X}".format(int(b))
        Codificado.append(str(hexa))
    
    # Fazer o enxerto
    for i in range(len(a)):
        Codificado[i] = Codificado[i].zfill(enxerto)
    
    Saida = "".join(Codificado)

    return Saida
        
def codificar_par(mensagem,enxerto):
    """ Codifica uma mensagem primeiro invertendo a mensagem, depois passando para ASCII e 
    a retorna em base OCTAL
    O enxerto é para o que o programa saiba identificar exatamente o que esta tentando decodificar.
    """

    #Inverte a mensagem
    mensagem = mensagem[::-1]

    #Transformar para ASCII
    a = ASCII(mensagem)
    
    # Codificar para base octal
    Codificado = []
    for b in a:
        oct = "{:o}".format(int(b))
        Codificado.append(str(oct))
    
    # Fazer o enxerto
    for i in range(len(a)):
        Codificado[i] = Codificado[i].zfill(enxerto)
    
    Saida = "".join(Codificado)

    return Saida
    
# Decodificar

def Des_ASCII(lista):
    """ Transforma os elementos de uma lista de ASCII para sua forma original.
    """
    for i in range(len(lista)):
        lista[i] = chr(int(lista[i]))

    return lista

def decodificar_impar(mensagem,enxerto):
    """ Decodifica uma mensagem pela base hexadecimal e depois a decodificar pela base ASCII. 
    O enxerto é para o que o programa saiba identificar exatamente o que esta tentando decodificar.
    """

    # Decodifcar pela base hexadecimal
    des_hexa = []

    for i in range(0,len(mensagem),enxerto): # Dando passos do tamanho do enxerto
        des_hexa.append(str( int( mensagem [i:enxerto + i] ,16))) # Pegando strings do tamanho do enxerto
    
    # Decodifcar pela base ASCII
    Decodificado = Des_ASCII(des_hexa)
    Saida = "".join(Decodificado)
    
    return Saida

def decodificar_par(mensagem,enxerto):
    """ Decodifica uma mensagem pela base octal e depois a decodificar pela base ASCII, e desinverter a mensagem. 
    O enxerto é para o que o programa saiba identificar exatamente o que esta tentando decodificar.
    """

    # Decodifcar pela base octal
    des_oct = []

    for i in range(0,len(mensagem),enxerto): # Dando passos do tamanho do enxerto
        des_oct.append(str( int( mensagem [i:enxerto + i] ,8))) # Pegando strings do tamanho do enxerto
    
    # Decodifcar pela base ASCII
    Decodificado = Des_ASCII(des_oct)

    # Desinverter lista
    Decodificado = "".join(Decodificado)
    Saida = Decodificado[::-1]

    return Saida


# Obter as entradas e organiza-las
dados = input().split(" ")

modo = int(dados[0])
enxerto = int(dados[1])
n = int(dados[2])

lista_mensagens = []
for i in range(n):
    mensagem = input() 
    lista_mensagens.append(mensagem)

# Printar de acordo com o modo 1 = Codificar ou 2 = Descodificar 
if modo == 1:
    for a in range(len(lista_mensagens)):
        if (a+1) % 2 == 0: # pois a lista comeca no 0
            print(codificar_par(lista_mensagens[a],enxerto))
        else:
            print(codificar_impar(lista_mensagens[a],enxerto))

else:
    for a in range(len(lista_mensagens)):
        if (a+1) % 2 == 0: # pois a lista comeca no 0
            print(decodificar_par(lista_mensagens[a],enxerto))
        else:
            print(decodificar_impar(lista_mensagens[a],enxerto))




    
