# Definições de funções

def Caracteristicas(Dados_Dossie,Nome):
    '''Função que que armezena um dicionário com o Perfil ({tipo_de_caracteritica: caracteritica}) 
    de uma pessoa em um dicionário chamado Dados_Dossie.

    Quando a ultima entrada for '-', retorna True, pois significa que mais perfis de pessoas serão armazenados.
    Quando a ultima entrada for '--', retorna False, pois significa que nenhum poutro perfil será armazenado.

    '''
    Perfil_do_Suspeito = {}
    while True:
        entrada = input().split(' ') 
        if entrada != ['-'] and entrada != ['--']:
            Tipo_de_Caracteristica = entrada[0][0:-1]
            Caracteristica = entrada[1]
            Perfil_do_Suspeito[Tipo_de_Caracteristica] = Caracteristica
        else:
            Dados_Dossie[Nome] = Perfil_do_Suspeito
            if entrada == ['-']:
                return True
            elif entrada == ['--']:
                return False

def Evidencias(Dados_Evidencias):
    '''Função que armazena o tipo_de_evidencia como chave e a evidencia como valor do dicionario Dados_Evidencias.
    
    Quando a entrada for '---', retorna False, pois não receberá mais evidencias.
    '''
    while True:
        entrada = input().split(' ') 
        if entrada != ['---'] :
            Tipo_de_Evidencia = entrada[0][0:-1]
            Evidencia = entrada[1]
            Dados_Evidencias[Tipo_de_Evidencia] = Evidencia
        else:
            return False

def Suspeitometro(Dados_Dossie,Dados_Evidencias):
    '''Função que Busca no Perfil das pessoas, presente no Dados_Dossie, as caracteristicas que estão presente
    no Dados_Evidencias.

    Assim, armazena no dicionário Suspeitometro o nome da pessoa e o respectivo grau de suspeito 
    (numero de evidencias iguais suas caracteristicas), retornando este dicionário.
    
    '''
    Suspeitometro = {}
    for Nome,perfil_suspeito in Dados_Dossie.items():
        Suspeitometro [Nome] = 0
        for tipo_de_caracteristca,caracteristica in perfil_suspeito.items():

            for tipo_de_evidencia,evidencia in Dados_Evidencias.items():

                if (tipo_de_caracteristca,caracteristica) == (tipo_de_evidencia,evidencia):
                    Suspeitometro [Nome] += 1 
    return Suspeitometro

def Suspeitos_Finais(Suspeitometro,Dados_Evidencias):    
    '''A partir do Suspeitometro, essa função todas as evidencias estão presentes nas caracteristicas do suspeito.
    Se o grau de suspeito é o mesmo numeor de evidencias.
    
    Assim, a função coloca esse suspeito na lista de Suspeitos_Finais, retornando essa lista ao final da averiguação'''
    Suspeitos_Finais = []
    for suspeitos,conta in Suspeitometro .items():

        if conta == len(Dados_Evidencias.keys()):
            Suspeitos_Finais.append(suspeitos)                

    return sorted(Suspeitos_Finais)


# Leitura de entradas 

Dados_Dossie = {}
Dados_Evidencias = {}

while True:
    entrada = input().split(':')
    Nome = entrada[1].strip()
    
    Anotar_Suspeitos = Caracteristicas(Dados_Dossie,Nome)

    if Anotar_Suspeitos == False:
        Anotar_Evidencias = Evidencias(Dados_Evidencias)
        break
    

# Comparação das Caracteristicas do Dossie com as Evidencias

Suspeitometro = Suspeitometro(Dados_Dossie,Dados_Evidencias)
Veredito = Suspeitos_Finais(Suspeitometro,Dados_Evidencias)


# Print dos Suspeitos(as)   

if len(Veredito) == 0:
    print('Nenhum suspeito(a) com essas caracteristicas foi identificado(a).')
elif len(Veredito) == 1:
    print('Suspeito(a):')
    print(Veredito[0])
else:
    print('Suspeitos(as):')
    for suspeito in Veredito:
        print(suspeito)
