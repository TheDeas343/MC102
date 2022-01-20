# Primeiros Dados

dados = input().split(" ")

senha = int(dados[0])
tentativas = int(dados[1])


#FUNÇÕES UTILIZADAS

def qtd_algarismos(x): 
    """Dado um numero x, pertencente aos naturais, essa função retorna o número de algarismos desse numero."""
    total = 1
    while x // 10 > 0:  
        x = x // 10
        total += 1

    return total

def semelhanca(teste): 
    """Dado uma senha teste, essa funcao devolve a semelhanca, quantidade de algarismos na mesma posição, 
    entre o teste e  a senha original.
    """

    semelhanca = 0

    for m in range (0,qtd_algarismos(senha)):
        if list(str(senha))[m] == list(str(teste))[m]:    # compara os indices da string senha e da string teste
            semelhanca += 1
    
    return semelhanca


# Pegando os inputs e printando a comparacao da tentativa com a  senha

tentativas_restantes = tentativas - 1

for p in range (tentativas):

    teste = int(input())
        
    if teste != senha:
        print("Senha incorreta")

        if qtd_algarismos(teste) == qtd_algarismos(senha):
            print("Semelhanca:", semelhanca(teste))
        else:
            print("Semelhanca: Erro: quantidade de digitos incongruente")
            
        print("Tentativas restantes:", tentativas_restantes)

        if tentativas_restantes == 0:
            print()
            print("Tentativas esgotadas. Acionando defesas...")
        else:
            print()

    else:
        print("Senha reconhecida. Desativando defesas...")
        break           # Parar o laço caso a senha for correta, finalizando os prints
    
    tentativas_restantes -= 1
