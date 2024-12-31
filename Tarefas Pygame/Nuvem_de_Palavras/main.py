#####################################################
# Tarefa 12 - Nuvem de palavras (Pygame)
# Aluno:Everton Pereira Militão
#####################################################
import pygame
import random

width = 800 #Largura Janela
height = 600 #Altura Janela
pygame.display.set_caption("\t Nuvem de Palavras")

def load():
  global preto, branco, azul, roxo, laranja, rosa,  clock, listCoordenadas, listWord, listCount, random_word, listRandom, tamanho_lista_random, count_w1, count_w2, count_w3, count_w4, count_w5, count_w6, count_w7, count_w8, count_w9,count_w10, cores, listaCores, font_size, cor_faixa1, cor_faixa2, cor_faixa3, cor_faixa4, cor_text, listPositionRandom
  listCount = []
  listRandom = []
  cor_text = []
  cor_faixa1 = None
  cor_faixa2 = None
  cor_faixa3 = None
  cor_faixa4 = None

  #Fontes:
  font_size = []

  #Cores:
  preto = (0,0,0)
  branco = (255,255,255)
  azul = (0,0,255)
  roxo = (148,0,211)
  laranja = (255,165,0)
  rosa = (222, 49, 99)
  cores = []
  listaCores = [azul, laranja, roxo, rosa]
  clock = pygame.time.Clock()
  
  #Contadores:
  count_w1 = 0
  count_w2 = 0
  count_w3 = 0
  count_w4 = 0
  count_w5 = 0
  count_w6 = 0
  count_w7 = 0
  count_w8 = 0
  count_w9 = 0
  count_w10 = 0

  #Selecionei uma imagem de uma Espiral inseri ela na tela, capturei alguns pontos usando mouse.get_pos() e defini eles como parte da minha espiral 
  listCoordenadas = [(395,260), (350,335), (400,180), (286,390), (280,150), (387,495), (254,85), (596,156), (594, 435), (153,279)]

  listWord = ['Programação', 'Computação', 'Python', 'CSS', 'Pygame', 'Java', 'Php', 'HTML', 'Ciência', 'Django']

  # Gerando posições diferentes em cada inicialização
  listPositionRandom = random.sample(listCoordenadas, 10)

  #Gerando 40 palavras aleatórias 
  for i in range(1,41):
    random_word = random.choice(listWord)
    listRandom.append(random_word)

  tamanho_lista_random = len(listRandom)

  #Fazendo a frequência de repetição das palavras:
  for palavra in range(0,len(listRandom)):
    if listRandom[palavra] == listWord[0]:
      count_w1 += 1
    elif listRandom[palavra] == listWord[1]:
      count_w2 += 1
    elif listRandom[palavra] == listWord[2]:
      count_w3 += 1
    elif listRandom[palavra] == listWord[3]:
      count_w4 += 1
    elif listRandom[palavra] == listWord[4]:
      count_w5 += 1
    elif listRandom[palavra] == listWord[5]:
      count_w6 += 1
    elif listRandom[palavra] == listWord[6]:
      count_w7 += 1
    elif listRandom[palavra] == listWord[7]:
      count_w8 += 1
    elif listRandom[palavra] == listWord[8]:
      count_w9 += 1
    elif listRandom[palavra] == listWord[9]:
      count_w10 += 1

  listCount = [count_w1, count_w2, count_w3, count_w4, count_w5, count_w6, count_w7, count_w8, count_w9,count_w10]

  #Dividindo os valores em quatro faixas (0-25%, 25-50%, 50-75%, 75-100%)
  max_value = max(listCount)
  min_value = min(listCount)
  faixa1 = (max_value-min_value) * 0.25 + min_value
  faixa2 = (max_value-min_value) * 0.5 + min_value
  faixa3 = (max_value-min_value) * 0.75 + min_value

  font_size = []
  for valor in listCount:
    if valor <= faixa1:
      font_size.append(12)
    elif valor <= faixa2:
      font_size.append(18)
    elif valor <= faixa3:
      font_size.append(24)
    else:
      font_size.append(30)
    
  #Criando Cores para cada valor na faixa
  cor_text = random.sample(listaCores, 4)
  
  
def draw(screen):
  global cor_text
  screen.fill(branco)
  # Fazendo cada fonte com sua respectiva cor e inserindo a palavra na tela
  for i in range(len(listCoordenadas)):
    x,y = listPositionRandom[i]
    palavra = listWord[i]
    if font_size[i] == 12:
      fonte = pygame.font.Font("font_normal.OTF", font_size[i])
      texto = fonte.render(palavra, True, cor_text[0])
      screen.blit(texto, (x,y))
    elif font_size[i] == 18:
      fonte = pygame.font.Font("font_normal.OTF", font_size[i])
      texto = fonte.render(palavra, True, cor_text[1])
      screen.blit(texto, (x,y))
    elif font_size[i] == 24:
      fonte = pygame.font.Font("font_normal.OTF", font_size[i])
      texto = fonte.render(palavra, True, cor_text[2])
      screen.blit(texto, (x,y))
    elif font_size[i] == 30:
      fonte = pygame.font.Font("font_normal.OTF", font_size[i])
      texto = fonte.render(palavra, True, cor_text[3])
      screen.blit(texto, (x,y))

def update(dt):
  pass 

def main_loop(screen):
  global clock
  running = True
  while running:
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        running = False
        break

      clock.tick(30)
      dt = clock.get_time()
      update(dt)
      draw(screen)
      pygame.display.update()


#Programa principal:
pygame.init()
screen = pygame.display.set_mode((width,height))
load()
main_loop(screen)
pygame.quit()
