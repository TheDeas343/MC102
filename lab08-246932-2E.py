# Funções utilizadas

def operacoes(linha,variaveis):
    ''' Operacao que procura por operadores na lista linha e ao acha-lo faz a operacao com o operando que antecede e sucede esse operador.
    Em seguida substitui esses tres indices da lista linha peo valor da expressao

    Segue uma preferencia:
    1º procura por operadores aritiméticos: "+" e "-".
    2º procura por operadores boleanos : "<", "<=", ">", ">=", "==" e "!=".
    3º procura por operadores logicos : "AND" e "OR".
    '''

    if linha[1] == '=': # Diferenciar as operações normais da atribuição de valor para uma variável
        c = 3
    else:
        c = 1

    for op in linha[c::2]: # intervalo dos operadores
        i = linha.index(op)
        if op == "+":
            conta = sub_op(linha,variaveis,i)
            linha[i-1:i+2] = [str(conta[0] + conta[1])] 
        elif op == "-":
            conta = sub_op(linha,variaveis,i)
            linha[i-1:i+2] = [str(conta[0] - conta[1])]
            
    for op in linha[c::2]:  
        i = linha.index(op)        
        if op == "==":
            conta = sub_op(linha,variaveis,i)
            if conta[0] == conta[1] :
                linha[i-1:i+2] = ["1"]                           
            else:
                linha[i-1:i+2] = ["0"] 
        elif op == ">":
            conta = sub_op(linha,variaveis,i)
            if conta[0] > conta[1]:
                linha[i-1:i+2] = ["1"]
            else:
                linha[i-1:i+2] = ["0"]
        elif op == ">=":
            conta = sub_op(linha,variaveis,i)
            if conta[0] >= conta[1]:
                linha[i-1:i+2] = ["1"]
            else:
                linha[i-1:i+2] = ["0"]
        elif op == "<":
            conta = sub_op(linha,variaveis,i)
            if conta[0] < conta[1]:
                linha[i-1:i+2] = ["1"]
            else:
                linha[i-1:i+2] = ["0"]
        elif op == "<=":
            conta = sub_op(linha,variaveis,i)
            if conta[0] <= conta[1]:
                linha[i-1:i+2] = ["1"]
            else:
                linha[i-1:i+2] = ["0"]
        elif op == "!=":
            conta = sub_op(linha,variaveis,i)
            if conta[0] != conta[1]:
                linha[i-1:i+2] = ["1"]
            else:
                linha[i-1:i+2] = ["0"]

    for op in linha[c::2]:
        i = linha.index(op) 
        conta = sub_op(linha,variaveis,i)
        if op == "AND":                       
            if conta[0] and conta[1] == 1:
                linha[i-1:i+2] = ["1"]
            else:
                linha[i-1:i+2] = ["0"]
        elif op == "OR":
            if conta[0] or conta[1] == 1:
                linha[i-1:i+2] = ["1"]
            else:
                linha[i-1:i+2] = ["0"]

def sub_op(linha,variaveis,i):
    '''Suboperacao que analisa se o os operandos envolvidos em uma expressao com um operador 
    é uma variavel ou uma constante.

    caso for uma variavel devolve seu valor armazenado no dicionario variaveis.
    caso for uma constante devolve seu valor em int.
    '''

    if linha[i-1][0].isalpha():
        if linha[i+1][0].isalpha():
            return  [int(variaveis[linha[i-1]]),int(variaveis[linha[i+1]])]
        else:
            return  [int(variaveis[linha[i-1]]),int(linha[i+1])]
    else:
        if linha[i+1][0].isalpha():
            return  [int(linha[i-1]),int(variaveis[linha[i+1]])]
        else:
            return  [int(linha[i-1]),int(linha[i+1])]

def verify(linha):
    '''Funcao que verifica se ha alguma variavel não definida em uma linha'''
    
    if linha[1] == '=': # Diferenciar as operações normais da atribuição de valor para uma variável
        c = 2
    else:
        c = 0

    for a in range(c,len(linha),2): 
        if (linha[a])[0].isalpha() and linha[a] != "AND" and linha[a] != "OR" and linha[a] not in variaveis:
            print(f"Erro de referencia: a variavel {linha[a]} nao foi definida.")
            return False 

    return True

# Leituras de entradas e execucao das operações

variaveis = {}

while True:
    try:
        linha = input().split(" ")

        if len(linha) == 1: # Quando so é digitado um valor

            if linha[0][0].isalpha(): # Se for uma variavel
                if linha[0] in variaveis:
                    print(variaveis[linha[0]]) 
                else:
                    print(f"Erro de referencia: a variavel {linha[0]} nao foi definida.")

            else: # Se nao for uma variavel
                print(linha[0]) 
                    
        else:
            if linha[1] == "=": # Se o "=" esta na segunda posição entao a primeira posição é uma variavel.
                for i in linha[0]: # Verificar se  a variavel esta nos padroes
                    if (i == linha[0][0]  and i.isalpha() == False) or (i.isalpha() ==  False and i not in "0123456789" ) :
                        print(f"Erro de sintaxe: {linha[0]} nao e um nome permitido para uma variavel.")
                        break
                else:
                    if len(linha) == 3:  # Se tivermos "variavel1 = variavel2" devemos atribuir o valor da variavel2 para a variavel1
                        if linha[2][0].isalpha():
                            if linha[2] not in variaveis:
                                print(f"Erro de referencia: a variavel {linha[2]} nao foi definida.")
                            else:   
                                variaveis[linha[0]] = variaveis[linha[2]]  
                        else:
                            variaveis[linha[0]] = linha[2]
                    else:  # Verificar se a variavel depende de outras variaveis nao definidas
                        if verify(linha):
                            operacoes(linha,variaveis)  # depois de todas as operaçoes sobrara apenas a linha = ["variavel","=","valor"]
                            variaveis[linha[0]] = linha[2]        

            else: # Se é apenas uma expressao. Tambem devemos ver se tem variaveis não definidas      
                if verify(linha):
                    operacoes(linha,variaveis) # depois de todas as operacoes sobrara linha = ["valor"]
                    print(linha[0])

    except EOFError:
        print("Encerrando... Bye-bye.")
        break