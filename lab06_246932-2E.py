# Definições das classes

class Medalutador:
  def __init__(self,ID,H,K,M,medalhao,T,P,D,E,Medabot):
      
      self.ID = ID                  # Identificacao do Medalutador
      self.H = H                    # Habilidade Original
      self.H_atual = H              # Habilidade Atual
      self.K = K                    # Recuperacao
      self.M = M                    # Numero de Medapecas
      self.medalhao = medalhao      # Medalhão com o bonus de ataque e defesa
      self.T = T                    # Lista com as medapecas do torso
      self.P = P                    # Lista com as medapecas da perna
      self.D = D                    # Lista com as medapecas do braco direito
      self.E = E                    # Lista com as medapecas do braco esquerdo
      self.Medabot = Medabot        # Medabot montado com as melhores peças e o medalhão
      
  def obter_ID(self):
      return self.ID

  def __repr__(self):
      return str(self.ID)
    
  def obter_H(self):
      return self.H_atual

  def obter_K(self):
      return self.K

  def alterar_H(self,nova_H):
    self.H_atual = nova_H
    
  def atualizar_medabot(self):
    if 0 not in [len(self.T),len(self.P),len(self.D),len(self.E)]:  # Método max() nao pode receber uma lista vazia
      MT = max(self.T)
      MP = max(self.P)
      MD = max(self.D)
      ME = max(self.E)
      Am = int(self.medalhao[0])
      Dm = int(self.medalhao[1])


      self.Medabot = Medabot(Am,Dm,MT,MP,MD,ME)

class Medabot:
  def __init__(self,Am,Dm,MT,MP,MD,ME):
    self.Am = Am   # Bonus de ataque do medalhao
    self.Dm = Dm   # Bonus de defesa do medalhao
    self.MT = MT   # Peça com Maior pontuação do Torso
    self.MP = MP   # Peça com Maior pontuação das Pernas
    self.MD = MD   # Peça com Maior pontuação do braço Direito
    self.ME = ME   # Peça com Maior pontuação do braço Esquerdo

  def obter_Am(self):
    return self.Am

  def obter_Dm(self):
    return self.Dm

  def obter_MT(self):
    return self.MT

  def obter_MP(self):
    return self.MP

  def obter_MD(self):
    return self.MD

  def obter_ME(self):
    return self.ME
    
  def Ataque(self):
    """Soma as pontuacoes do Braco  Esquerdo e Direito mais o bonus de ataque que o medalhao fornece."""

    Ataque = self.ME + self.MD + self.Am
    return Ataque

  def Defesa(self):
    """Soma as pontuacoes do Torso, das Pernas e do bonus de defesa que o medalhao fornece."""

    Defesa = self.MT + self.MP + self.Dm
    return Defesa
     
# Funcoes necessarias para aplicar a rodada de batalhas 
         
def batalhar(i,j):
  """ Fornece o vencedor em uma batalha entre dois medalutadores."""

  if (i.Medabot.Ataque() > j.Medabot.Defesa() or j.Medabot.Ataque() > i.Medabot.Defesa()) and  i.Medabot.Ataque()-j.Medabot.Defesa() != j.Medabot.Ataque()-i.Medabot.Defesa() :
    if  i.Medabot.Ataque()-j.Medabot.Defesa() > j.Medabot.Ataque()-i.Medabot.Defesa():
      return i
    else:
      return j  
  elif i.obter_H() != j.obter_H():
    if i.obter_H() > j.obter_H():
      return i
    else:
      return j
  else:
    if i.obter_ID() < j.obter_ID():
      return i
    else:
      return j

def imprimir_ficha_tecnica(i,j):
  """ Imprime a lista de ataques, defesas e habilidades de dois competidores medabots."""

  competidores = [i,j]
  for x in competidores:  
    print(f"\tA{x.obter_ID()} = E{x.Medabot.obter_ME()} + D{x.Medabot.obter_MD()} + {x.Medabot.obter_Am()} = {x.Medabot.Ataque()}")
    print(f"\tD{x.obter_ID()} = T{x.Medabot.obter_MT()} + P{x.Medabot.obter_MP()} + {x.Medabot.obter_Dm()} = {x.Medabot.Defesa()}")
    print(f"\tH{x.obter_ID()} = {x.obter_H()}")

def imprimir_resultado_da_batalha(i,j,k):
  """ Imprimi o resultado da batalha entre dois medalutadores."""

  print(f'Medalutador {k} venceu e recebeu a {medapeca_ganha(i,j,k,True)}{medapeca_ganha(i,j,k,False)}\n')


# Funcoes que organizam e preparam os medalutadores para a proxima cyberluta

def lista_peca_medabot(lista,X):
  """Recebe uma lista com todas as medapecas e separa os pontos em ordem crescente de acordo com uma determinada medapeca X."""
    
  lista_pontuacao = []
  for i in range(len(lista)):
      if str(X) in lista[i]:
          atual = lista[i].split(" ")
          lista_pontuacao.append(int(atual[1]))
    
  return lista_pontuacao

def alterar_habilidade(i,j,k):
  """ Estabelece as novas habilidades para a proxima cyberluta baseada em 
  k(vencedor) e p(perdedor) entre dois medalutadores(i e j)."""
  
  if i == k:
    v,p = i,j
  else:
    v,p = j,i

  # Para o vencedor
  if v.obter_H() - p.obter_H() < 0:
    if  v.obter_K() > v.H:
      nova_H = v.H
    else:
      nova_H = v.obter_K()
        
  else:
    nova_H = v.obter_H()-p.obter_H() + v.obter_K()
    if  nova_H  > v.H:
      nova_H = v.H
        
      
  v.alterar_H(nova_H)

  # Para o perdedor
  if p.obter_H() // 2 + p.obter_K() > p.H:
    nova_H = p.H
  else:
    nova_H = p.obter_H() // 2 + p.obter_K()
      
  p.alterar_H(nova_H)

def medapeca_ganha(i,j,k,TIPO):
  """ Fornece a medapeca ou a pontuacao da medapeca ganha pelo vencedor da batalha entre dois medalutadores.

  Se TIPO == True, devolve a medapeca, se TIPO == False, devolve a pontuacao da medapeca.
  """

  if i == k:
    v,p = i,j
  else:
    v,p = j,i
  
  delta_T = (p.Medabot.obter_MT()) - (v.Medabot.obter_MT())
  delta_P = (p.Medabot.obter_MP()) - (v.Medabot.obter_MP())
  delta_D = (p.Medabot.obter_MD()) - (v.Medabot.obter_MD())
  delta_E = (p.Medabot.obter_ME()) - (v.Medabot.obter_ME())
  
  deltas = [delta_T,delta_P,delta_D,delta_E]

  if delta_T == max(deltas):
    if TIPO :
      return "T" 
    else:
      return p.Medabot.obter_MT()
  elif delta_E == max(deltas):
    if TIPO :
      return "E" 
    else:
      return p.Medabot.obter_ME()
  elif delta_D == max(deltas):
    if TIPO :
      return "D" 
    else:
      return p.Medabot.obter_MD()
  else:
    if TIPO :
      return "P" 
    else:
      return p.Medabot.obter_MP()

def adicionar_retirar_medapeca(i,j,k, tipo_medapeca, pontuacao):

  """ Adiciona a pontuacao de uma determinada medapeca na respectiva lista do vencedor, ordenanado esta 
  de forma crescente de novo, e retira essa mesma medapeca da respectiva lista do perdedor.
  """
  if i == k:
    v,p = i,j
  else:
    v,p = j,i
  

  # Para o vencedor
  if tipo_medapeca == "T":
    v.T.append(pontuacao)
    
  elif tipo_medapeca == "D":
    v.D.append(pontuacao)
    
  elif tipo_medapeca == "P":
    v.P.append(pontuacao)
    
  elif tipo_medapeca == "E":
    v.E.append(pontuacao)
  
  v.atualizar_medabot()
  
  
  # Para o perdedor   
  if tipo_medapeca == "T":
    p.T.remove(pontuacao)
    

  if tipo_medapeca == "D":
    p.D.remove(pontuacao)
      

  if tipo_medapeca == "P":
    p.P.remove(pontuacao)

  if tipo_medapeca == "E":
    p.E.remove(pontuacao)

  p.atualizar_medabot()


# Funcoes que executam as cyberlutas

def simular_torneios_de_cyberlutas(lista_de_medalutadores):

  lista_torneio_principal = []
  lista_de_repescagem     = []

  for medalutador in lista_de_medalutadores:
    lista_torneio_principal.append(medalutador)

  while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:

    lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
    lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)

  i = lista_torneio_principal.pop(0)
  j = lista_de_repescagem.pop(0)

  print('Cyberluta Final')
  print(f'Medalutadores: {i} vs {j}')

  imprimir_ficha_tecnica(i, j)
  k = batalhar(i, j)

  print(f'Campeao: medalutador {k}')

def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
  
  if len(lista_de_medalutadores) < 2:
    return lista_de_medalutadores

  lista_de_vencedores = []

  while len(lista_de_medalutadores) >= 2:

    i = lista_de_medalutadores.pop(0) 
    j = lista_de_medalutadores.pop(0)

    if i.obter_ID() > j.obter_ID():
      i, j = j, i

    if lista_de_repescagem != None:
      print('Cyberluta do Torneio Principal')
    else:
      print('Cyberluta da Repescagem')

    print(f'Medalutadores: {i} vs {j}')
    
    imprimir_ficha_tecnica(i,j)
    k = batalhar(i,j)
    imprimir_resultado_da_batalha(i,j,k)

    # Adicionar a medapeca ganha ao vencedor e retirar a mesma do perdedor.
    adicionar_retirar_medapeca(i,j,k, medapeca_ganha(i,j,k,True),medapeca_ganha(i,j,k,False))

    # Estabelecer as novas habilidades para a proxima partida baseada em quem perde e ganha.
    alterar_habilidade(i,j,k)   
   
    if lista_de_repescagem != None:
      if i == k:
        lista_de_repescagem.append(j)
      else:
        lista_de_repescagem.append(i)

    lista_de_vencedores.append(k)
  lista_de_vencedores.extend(lista_de_medalutadores)

  return lista_de_vencedores


# Armezenar os inputs na lista de medalutadores pertencendo a classe Medalutador

N = int(input()) # Numero de medalutadores

lista_de_medalutadores=[]
for a in range(N):

  ID = a + 1
  caracteristicas = input().split(" ")
  H = int(caracteristicas[0])
  K = int(caracteristicas[1])
  M = int(caracteristicas[2])

  medalhao = input().split(" ")
  Am = int(medalhao[0])
  Dm = int(medalhao[1])

  lista_pecas = []
   
  for b in range(M):
      peca = input()
      lista_pecas.append(peca)

  T = lista_peca_medabot(lista_pecas,"T")
  P = lista_peca_medabot(lista_pecas,"P")
  D = lista_peca_medabot(lista_pecas,"D")
  E = lista_peca_medabot(lista_pecas,"E")

  MT = max(T)
  MP = max(P)
  MD = max(D)
  ME = max(E)

  lista_de_medalutadores.append(Medalutador(ID,H,K,M,medalhao,T,P,D,E,Medabot(Am,Dm,MT,MP,MD,ME)))
    

# Executar a as cyberlutas

simular_torneios_de_cyberlutas(lista_de_medalutadores)
