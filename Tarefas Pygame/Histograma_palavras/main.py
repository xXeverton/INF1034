#####################################################
# Tarefa 11.2 - Palavras - Histograma (Pygame)
# Aluno:Everton Pereira Militão
#####################################################
#Utilizei algumas funções e ideias da tarefa 11.1
import pygame
import random 

width = 800 #Largura Janela
height = 600 #Altura Janela
pygame.display.set_caption("\t Histograma Palavras")

def load():
  global sys_font1, sys_font2, sys_font3, clock, listWord, count2, azul, preto, py, listaNumero,count_w1, count_w2, count_w3, count_w4, count_w5, count_w6, count_w7, count_w8, count_w9, count_w10, count, listRandom,y_tela, largura
  azul = (0,0,255)
  preto = (0,0,0)
  listWord = []
  listRandom = []
  sys_font1 = pygame.font.Font("Ios_font.OTF", 20)
  sys_font2 = pygame.font.Font("Ios_font.OTF", 15)
  sys_font3 = pygame.font.Font("Ios_font.OTF", 25)
  clock = pygame.time.Clock()
  py = 30
  y_tela = 7.50*4
  listaNumero = list(range(0,10))
  largura = 30

  count = 1
  #Contadores:
  count2 = 0
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

  #Usuário digita a palavra:
  #Apresentação no Console:
  print("-------------------Histograma de Palavras-------------------------")

  #Teste
  listWord = ['Programação', 'Computação', 'Python', 'CSS', 'Pygame', 'Java', 'Php', 'HTML', 'Ciência', 'Django']
  
  for i in range(1,41):
    random_word = random.choice(listWord)
    listRandom.append(random_word)

  #Fazendo a contagem de repetição das palavras:
  for palavra in range(len(listRandom)):
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

  print("A palavra %s aparece %d vezes" %(listWord[0], count_w1) )
  print("A palavra %s aparece %d vezes" %(listWord[1], count_w2) )
  print("A palavra %s aparece %d vezes" %(listWord[2], count_w3) )
  print("A palavra %s aparece %d vezes" %(listWord[3], count_w4) )
  print("A palavra %s aparece %d vezes" %(listWord[4], count_w5) )
  print("A palavra %s aparece %d vezes" %(listWord[5], count_w6) )
  print("A palavra %s aparece %d vezes" %(listWord[6], count_w7) )
  print("A palavra %s aparece %d vezes" %(listWord[7], count_w8) )
  print("A palavra %s aparece %d vezes" %(listWord[8], count_w9) )
  print("A palavra %s aparece %d vezes" %(listWord[9], count_w10) )

  

  print("Total de palavras verificados:%d" %(count_w1+count_w2+count_w3+count_w4+count_w5+count_w6+count_w7+count_w8+count_w9+count_w10))
  

def draw(screen):
  global  azul, preto, py, listaNumero,count_w1, count_w2, count_w3, count_w4, count_w5, count_w6, count_w7, count_w8, count_w9,count_w10, y_tela
  screen.fill((255,255,255))

  #Retas do gráfico:
  #Eixo_X
  pygame.draw.line(screen, (0,0,0), (100,400), (600,400), 3)

  #Retas_Y
  for i in range(1,10):
    f = py*i
    pygame.draw.line(screen, (0,0,0), (100,400 - f), (600,400-f), 1)

  #Legenda_Y
  
  for i in range(0,10):
    g = py*i
    listaNumero[i] 
    numero = sys_font2.render(str(listaNumero[i]), True, preto)
    screen.blit(numero,(85,390-g))
  
  pygame.draw.rect(screen, azul, (100, 400 - count_w1*y_tela , largura , count_w1*y_tela ))
  pygame.draw.rect(screen, azul, (150, 400 - count_w2*y_tela , largura , count_w2*y_tela ))
  pygame.draw.rect(screen, azul, (200, 400 - count_w3*y_tela , largura , count_w3*y_tela ))
  pygame.draw.rect(screen, azul, (250, 400 - count_w4*y_tela , largura , count_w4*y_tela ))
  pygame.draw.rect(screen, azul, (300, 400 - count_w5*y_tela , largura , count_w5*y_tela ))
  pygame.draw.rect(screen, azul, (350, 400 - count_w6*y_tela , largura , count_w6*y_tela ))
  pygame.draw.rect(screen, azul, (400, 400 - count_w7*y_tela , largura , count_w7*y_tela ))
  pygame.draw.rect(screen, azul, (450, 400 - count_w8*y_tela , largura , count_w8*y_tela ))
  pygame.draw.rect(screen, azul, (500, 400 - count_w9*y_tela , largura , count_w9*y_tela ))
  pygame.draw.rect(screen, azul, (550, 400 - count_w10*y_tela , largura , count_w10*y_tela ))

  #Legenda_Eixo_X
  for x in range(len(listWord)):
    k = 50 * x
    word_leg = sys_font2.render(str(listWord[x]),True,preto)
    word_leg_rotate = pygame.transform.rotate(word_leg,60)
    screen.blit(word_leg_rotate, (80+k, 410))

  titulo = sys_font3.render("QUANTIDADE", True, preto)
  screen.blit(titulo, (250, 50))
    
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

      clock.tick(60)
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
  

  
  
