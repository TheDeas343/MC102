
Lista_T = [] # Armazenar Tamanho
Lista_PC = [] # Armazenar as peças e a casas delas

tamanho = int(input())
posicao = input()

Lista_T.append(tamanho)
Lista_PC.append(posicao)

conta = 1   #Contagem do numero de pecas

while tamanho != 0:

    tamanho = int(input())
    if tamanho == 0:
        break

    posicao = input()
    conta += 1

    Lista_T.append(tamanho)
    Lista_PC.append(posicao)

   
# Individualizando os termos da lista e fazendo o tabulerio correspondente
#      
for x in range (conta): # A lista começa do 0,pois de 0 até (conta-1) sao (conta) numeros
    
    n = int(Lista_T[x])
    casa = Lista_PC[x].split(" ")
    
    peca = str(casa[0]) 
    coluna = (ord(casa[1]) - 96)  # Pois em ASCII a relaçao letra=numero dista 96 unidades(a=97,b=98)
                                  # Logo , para manter a igualdade a=1, b=2 ..., subtrai 96
    linha = int(casa[2])
    
    coluna_print = casa[1] #valor que vai ser printado(sem a codificação ASCII)



# PEAO

    if peca == "Peao":
        print("Movimentos para a peca ",peca," a partir da casa ",coluna_print,linha,".",sep = "")

        i = 0

        for i in range (n + 1): # escrever cada linha e o número que esta na frente dela
            n_linha = n - i 

            if n_linha > 0 : # Uma hora o indice sera maior que o n, e as linhas serao negativas
                    print(n_linha, end = " ") # Imprimir o numero da linha

                    if n_linha == linha: # Colocar a peça na casa corresponedente
                        for p in range (1, n + 1):
                            if p == coluna: 
                                print("o",end = " ")
                            else:
                                print("-", end = " ")

                    elif n_linha == linha + 1 : #Marcar a casa em que o peao pode se mover(uma a frente)
                            for p in range (1, n + 1):
                                if p == coluna : 
                                    print("x",end = " ")
                                else:
                                    print("-", end = " ")

                    elif linha == 2 and n_linha == linha + 1 + 1 : #Duas casas a sua frente quando esta na linha 2 
                        for p in range (1, n + 1):
                            if p == coluna : 
                                print("x",end = " ")
                            else:
                                print("-", end = " ")
            
                    else:
                        for p in range (1, n + 1): # Deamis casas nao usadas
                            print("-", end = " ")

                    print()
        b = 0
        print(" ", end=" ")
        for p in range(n):
            print(chr(ord("a") + b), end = " ")
            b += 1
        print()
        print()
   

# TORRE

    if peca == "Torre":
        print("Movimentos para a peca ",peca," a partir da casa ",coluna_print,linha,".",sep = "")

        i = 0

        for i in range (n + 1): # escrever cada linha e o número que esta na frente dela
            n_linha = n - i 

            if n_linha > 0 : # Uma hora o indice sera maior que o n, e as linhas serao negativas
                    print(n_linha, end = " ") # Imprimir o numero da linha

                    if n_linha == linha: # Colocar a peça na casa corresponedente
                        for p in range (1, n + 1):
                            if p == coluna: 
                                print("o",end = " ")
                            else:
                                print("x", end = " ") # Torre ataca toda sua linha

                    else:
                        for p in range (1, n + 1):
                            if p == coluna:
                                print("x", end = " ") # A torre ataca toda sua coluna
                            else:    
                                print("-", end = " ")

                    print()
        b = 0
        print(" ", end=" ")
        for p in range(n):
            print(chr(ord("a") + b), end = " ")
            b += 1
        print()
        print()

# REI

    if peca == "Rei":
            print("Movimentos para a peca ",peca," a partir da casa ",coluna_print,linha,".",sep = "")

            i = 0

            for i in range (n + 1): # escrever cada linha e o número que esta na frente dela
                n_linha = n - i 

                if n_linha > 0 : # Uma hora o indice sera maior que o n, e as linhas serao negativas
                        print(n_linha, end = " ") # Imprimir o numero da linha

                        if n_linha == linha: # Colocar a peça na casa corresponedente
                            for p in range (1, n + 1):
                                if p == coluna: 
                                    print("o",end = " ")
                                else:
                                    if p == coluna - 1 or p == coluna + 1: # Casas da linha do rei
                                        print("x", end = " ")
                                    else:
                                        print("-", end = " ")
                                        
                
                        else:
                            for p in range (1, n + 1):
                                    if n_linha == linha - 1 or n_linha == linha + 1:       # Casas da coluna do rei
                                        if p == coluna - 1 or p == coluna + 1 or p == coluna: # Casas da diagonal do rei
                                            print("x", end = " ")
                                        else:
                                            print("-", end = " ")
                                    else:
                                        print("-", end = " ")
                        

                        print()
            b = 0
            print(" ", end=" ")
            for p in range(n):
                print(chr(ord("a") + b), end = " ")
                b += 1
            print()
            print()

#CAVALO
   
    if peca == "Cavalo":
            print("Movimentos para a peca ",peca," a partir da casa ",coluna_print,linha,".",sep = "")

            i = 0

            for i in range (n + 1): # escrever cada linha e o número que esta na frente dela
                n_linha = n - i 

                if n_linha > 0 : # Uma hora o indice sera maior que o n, e as linhas serao negativas
                        print(n_linha, end = " ") # Imprimir o numero da linha

                        if n_linha == linha: # Colocar a peça na casa corresponedente
                            for p in range (1, n + 1):
                                if p == coluna: 
                                    print("o",end = " ")
                                else:
                                    print("-", end = " ")
                                        
                
                        else:
                            for p in range (1, n + 1):
                                    if n_linha == linha - 1 or n_linha == linha + 1:   # Casas que o cavalo ataca 
                                        if p == coluna - 2 or p == coluna + 2 :        #uma linha pra cima e pra baixo
                                            print("x", end = " ")
                                        else:
                                            print("-", end = " ")

                                    elif n_linha == linha - 2 or n_linha == linha + 2:  # Casas que o cavalo ataca 
                                        if p == coluna - 1 or p == coluna + 1 :         #duas linhas pra cima e pra baixo
                                            print("x", end = " ")
                                        else:
                                            print("-", end = " ")

                                    else:
                                        print("-", end = " ")
                        

                        print()
            b = 0
            print(" ", end=" ")
            for p in range(n):
                print(chr(ord("a") + b), end = " ")
                b += 1
            print()
            print()

#BISPO

    if peca == "Bispo":
            print("Movimentos para a peca ",peca," a partir da casa ",coluna_print,linha,".",sep = "")

            i = 0

            for i in range (n + 1): # escrever cada linha e o número que esta na frente dela
                n_linha = n - i 

                if n_linha > 0 : # Uma hora o indice sera maior que o n, e as linhas serao negativas
                        print(n_linha, end = " ") # Imprimir o numero da linha

                        if n_linha == linha: # Colocar a peça na casa corresponedente
                            for p in range (1, n + 1):
                                if p == coluna: 
                                    print("o",end = " ")
                                else:
                                    print("-", end = " ")
                                        
                
                        else:
                            for p in range (1, n + 1):
                                casa_cima = n - linha       #Saber a quantidade de casas as cima e a baixo 
                                casa_baixo = n - casa_cima  #para fazer "for in range"
                                   
                                    #Cima
                                for r in range (1,casa_cima + 1):
                                    if n_linha == linha + r:    # Casas diagonais que o bispo ataca a cima dele
                                        if p == coluna - r or p == coluna + r : # A cada linha acima do bispo 
                                            print("x", end = " ")               #as casas atacadas aumentam em 1 sua distancia
                                        else:
                                            print("-", end = " ")
                                    

                                    #Baixo
                                for r in range (1,casa_baixo+1):
                                    if n_linha == linha - r:    # Casas diagonais que o bispo ataca a baixo dele
                                        if p == coluna - r or p == coluna + r : # A cada linha abaixo do bispo 
                                            print("x", end = " ")               #as casas atacadas aumentam em 1 sua distancia
                                        else:
                                            print("-", end = " ")

                                    
                        

                        print()
            b = 0
            print(" ", end=" ")
            for p in range(n):
                print(chr(ord("a") + b), end = " ")
                b += 1
            print()
            print()

#DAMA- personalizar o codigo do bispo com o da torre

    if peca == "Dama":
            print("Movimentos para a peca ",peca," a partir da casa ",coluna_print,linha,".",sep = "")

            i = 0

            for i in range (n + 1): # escrever cada linha e o número que esta na frente dela
                n_linha = n - i 

                if n_linha > 0 : # Uma hora o indice sera maior que o n, e as linhas serao negativas
                        print(n_linha, end = " ") # Imprimir o numero da linha

                        if n_linha == linha: # Colocar a peça na casa corresponedente
                            for p in range (1, n + 1):
                                if p == coluna: 
                                    print("o",end = " ")
                                else:
                                    print("x", end = " ") # A dama ataca toda sua linha

                        else:
                         
                            for p in range (1, n + 1):
                                casa_cima = n - linha       #Saber a quantidade para fazer "for in range"
                                casa_baixo = n - casa_cima
                                   
                                    #Cima
                                for r in range (1,casa_cima + 1):
                                    if n_linha == linha + r:    # Casas diagonais que a dama ataca a cima dele
                                        if p == coluna - r or p == coluna + r or p == coluna: # A cada linha acima do dama 
                                            print("x", end = " ")                             #as casas atacadas aumentam em 1 sua distancia
                                        else:
                                            print("-", end = " ")
                                    

                                    #Baixo
                                for r in range (1,casa_baixo+1):
                                    if n_linha == linha - r:    # Casas diagonais que o dama ataca a baixo dele
                                        if p == coluna - r or p == coluna + r or p == coluna: # A cada linha abaixo do dama 
                                            print("x", end = " ")                             #as casas atacadas aumentam em 1 sua distancia
                                        else:
                                            print("-", end = " ")
                        print()
            b = 0
            print(" ", end=" ")
            for p in range(n):
                print(chr(ord("a") + b), end = " ")
                b += 1
            print()
            print()
