#####################################################
# Tarefa 11.1 - Notas de provas - Histograma (Pygame)
# Aluno:Everton Pereira Militão
#####################################################
import pygame
import random

width = 800 #Largura Janela
height = 600 #Altura Janela
pygame.display.set_caption("\t Histograma Notas")

def load():
  global sys_font, sys_fonty, clock, listaNotas, numeros, c0_2, c2_4, c4_6, c6_8, c8_10, px, y_tela, vermelho_escuro,vermelho,vermelho_claro,azul_claro,azul,azul_escuro, px1, preto, legendaY
  sys_font = pygame.font.Font("Ios_font.OTF", 20)
  sys_fonty = pygame.font.Font("Ios_font.OTF", 15)
  clock = pygame.time.Clock()
  px = 30
  px1 = 100
  y_tela = 6.2
  legendaY = list(range(0,50,5))

  #Cores:
  vermelho_escuro = (73,16,16)
  vermelho = (169,0,0)
  vermelho_claro = (151,49,48)
  azul_claro = (0,255,255)
  azul = (25,229,230)
  azul_escuro = (36,167,168)
  preto = (0,0,0)
  
  #Lista com 50 numeros entre 0 e 10
  listaNotas = []
  for i in range(1,51):
    numero = random.uniform(0,10)
    listaNotas.append(round(numero,1))
    
  #Contadores
  c0_2 = 0
  c2_4 = 0
  c4_6 = 0
  c6_8 = 0
  c8_10 = 0


  for nota in range(len(listaNotas)):
    #vermelho_escuro
    if listaNotas[nota] < 2:
      c0_2 += 1
    elif listaNotas[nota] < 4:
      c2_4 += 1
    #vermelho_
    elif listaNotas[nota] < 6:
      c4_6 += 1
    elif listaNotas[nota] < 8:
      c6_8 += 1
    elif listaNotas[nota] <= 10:
      c8_10 += 1

  print("----------------Histograma Notas--------------------")
  print("De 0 a 1.9 há %d notas" %c0_2)
  print("De 2 a 3.9 há %d notas"%c2_4)
  print("De 4 a 5.9 há %d notas" %c4_6)
  print("De 6 a 7.9 há %d notas" %c6_8)
  print("De 8 a 10 há %d notas" %c8_10)
  print("Total de notas verificadas:%d" %int(c0_2+c2_4+c4_6+c6_8+c8_10) )
    
  
def draw(screen):
  screen.fill((64,84,71))

  #Retas do gráfico
  pygame.draw.line(screen, (0,0,0), (100,400), (600,400), 3)
  pygame.draw.line(screen, (0,0,0), (75, 390), (75, 90), 3)

  #Eixo_X
  pygame.draw.line(screen, (0,0,0), (100,400), (100,410),3) #0
  pygame.draw.line(screen, (0,0,0), (200,400), (200,410),3) #2
  pygame.draw.line(screen, (0,0,0), (300,400), (300,410),3) #4
  pygame.draw.line(screen, (0,0,0), (400,400), (400,410),3) #6
  pygame.draw.line(screen, (0,0,0), (500,400), (500,410),3) #8
  pygame.draw.line(screen, (0,0,0), (600,400), (600,410),3) #10

  #legendaEixoX
  zero = sys_font.render('0', True, preto)
  screen.blit(zero, (95,408))
  dois = sys_font.render('2', True, preto)
  screen.blit(dois, (195,408))
  quatro = sys_font.render('4', True, preto)
  screen.blit(quatro, (295,408))
  seis = sys_font.render('6', True, preto)
  screen.blit(seis, (395,408))
  oito = sys_font.render('8', True, preto)
  screen.blit(oito, (495,408))
  dez = sys_font.render('10', True, preto)
  screen.blit(dez, (595,408))

  notas = sys_font.render("Notas", True, preto)
  screen.blit(notas, (295,460) )

  frequencia = sys_fonty.render("Frequência", True, preto)
  frequencia_rotacionado = pygame.transform.rotate(frequencia, 90)
  screen.blit(frequencia_rotacionado, (20, 390-5.8*px))

  
  #Eixo_Y
  pygame.draw.line(screen, (0,0,0), (75, 390), (65, 390), 3) #0
  pygame.draw.line(screen, (0,0,0), (75, 390-px), (65, 390-px), 3) #5
  pygame.draw.line(screen, (0,0,0), (75, 390-2*px), (65, 390-2*px), 3) #10
  pygame.draw.line(screen, (0,0,0), (75, 390-3*px), (65, 390-3*px), 3) #15
  pygame.draw.line(screen, (0,0,0), (75, 390-4*px), (65, 390-4*px), 3) #20
  pygame.draw.line(screen, (0,0,0), (75, 390-5*px), (65, 390-5*px), 3) #25
  pygame.draw.line(screen, (0,0,0), (75, 390-6*px), (65, 390-6*px), 3) #30
  pygame.draw.line(screen, (0,0,0), (75, 390-7*px), (65, 390-7*px), 3) #35
  pygame.draw.line(screen, (0,0,0), (75, 390-8*px), (65, 390-8*px), 3) #40
  pygame.draw.line(screen, (0,0,0), (75, 390-9*px), (65, 390-9*px), 3) #45
  pygame.draw.line(screen, (0,0,0), (75, 390-10*px), (65, 390-10*px), 3) #50

  #Legenda Eixo_y:
  zeroy = sys_fonty.render('0', True,preto)
  screen.blit(zeroy, (50, 385))
  cinco = sys_fonty.render('5', True,preto)
  screen.blit(cinco, (50, 385-px))
  dezy = sys_fonty.render('10', True,preto)
  screen.blit(dezy, (45, 385-2*px))
  quinze = sys_fonty.render('15', True,preto)
  screen.blit(quinze, (45, 385-3*px))
  vinte = sys_fonty.render('20', True,preto)
  screen.blit(vinte, (45, 385-4*px))
  vinte_cinco = sys_fonty.render('25', True,preto)
  screen.blit(vinte_cinco, (45, 385-5*px))
  trinta = sys_fonty.render('30', True,preto)
  screen.blit(trinta, (45, 385-6*px))
  trinta_cinco = sys_fonty.render('35', True,preto)
  screen.blit(trinta_cinco, (45, 385-7*px))
  quarenta = sys_fonty.render('40', True,preto)
  screen.blit(quarenta, (45, 385-8*px))
  quarenta_cinco = sys_fonty.render('45', True,preto)
  screen.blit(quarenta_cinco, (45, 385-9*px))
  cinquenta = sys_fonty.render('50', True,preto)
  screen.blit(cinquenta, (45, 385-10*px))

  #Gráficos
  pygame.draw.rect(screen, vermelho_escuro, (100, 390 - c0_2*y_tela , 100 , c0_2*y_tela ))
  pygame.draw.rect(screen, vermelho, (200, 390 - c2_4*y_tela , 100 , c2_4*y_tela ))
  pygame.draw.rect(screen, vermelho_claro, (300, 390 - c4_6*y_tela , 100, c4_6*y_tela ))
  pygame.draw.rect(screen, azul_claro, (400, 390 - c6_8*y_tela , 100 , c6_8*y_tela ))
  pygame.draw.rect(screen, azul_escuro, (500, 390 - c8_10*y_tela , 100 , c8_10*y_tela ))

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
