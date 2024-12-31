#Everton Pereira Militão
import pygame
import math

#Algumas constantes
tile_size = 64 #Tamanho do personagem
width = tile_size * 14 #largura da tela
height = tile_size * 10 #Altura da tela
#Regiões de Preenchimento do mapa
mapa = [
  "SSSSSSSSSSSSSS",
  "SGGPGGGGGGGGGF",  
  "SGGPGGGGGGGGGF",
  "SGGPGGRGGGGGGF",
  "SGGPGGRGGGGGGF",
  "SGGGGGRGGGGGGF",
  "SGGGGGRGGGGGGF",
  "SSSSSSSSSSSSSS",
  "TTTTTTTTTTTTTT",
  "TTTTTTTTTTTTTT",
]
hero_frame = 1
hero_pos_x = 120
hero_pos_y = 225
hero_time = 0
dir = 3


def load():
  global clock,tile, sheet, spt_wdt, spt_hgt, hero_frame, collider_mapa1, collider_mapa2, collider_mapa3, collider_mapa4,collider_mapa5,collider_mapa6,  collider_jogador, tilset
  clock = pygame.time.Clock()
  tilset = pygame.image.load("Tile_Ground.png")
  sheet = pygame.image.load("Tile_Personagem.png")  # 3 x 4 
  spt_wdt = sheet.get_width() / 3   # Largura de um sprite
  spt_hgt = sheet.get_height() / 4   # Altura de um sprite

  #Regiões de Colisão do Mapa
  collider_mapa1 = pygame.Rect(0, 0, 896, 64)
  collider_mapa2 = pygame.Rect(0, 64, 64, 6*64)
  collider_mapa3 = pygame.Rect(0, 64*7, 896, 64)
  collider_mapa4 = pygame.Rect(64*3, 64, 64, 64*4 )
  collider_mapa5 = pygame.Rect(64*6, 64*3, 64, 64*4 )
  collider_mapa6 = pygame.Rect(64*13, 64, 64, 6*64)


def update(dt):
  global camera, hero_frame, hero_pos_x, hero_time, dir, hero_pos_y, collider_jogador_copy, collider_jogador, colliders
  keys = pygame.key.get_pressed()
  old_x, old_y = hero_pos_x, hero_pos_y

  #Movimentação do Personagem
  if keys[pygame.K_LEFT]:  #Para Esquerda
    dir = 3
    hero_pos_x = hero_pos_x - (0.1 * dt)
    hero_time = hero_time + dt
    if hero_time > 100:
      hero_frame = hero_frame + 1
      if hero_frame > 2:
          hero_frame = 0
      hero_time = 0
   
  elif keys[pygame.K_RIGHT]: #Para a Direita
    dir = 2
    hero_pos_x = hero_pos_x + (0.1 * dt)
    hero_time = hero_time + dt
    if hero_time > 100:
      hero_frame = hero_frame + 1
      if hero_frame > 2:
          hero_frame = 0
      hero_time = 0
  
  elif keys[pygame.K_DOWN]: #Baixo
    dir = 1
    hero_pos_y = hero_pos_y + (0.1 * dt)
    hero_time = hero_time + dt
    if hero_time > 100:
        hero_frame = hero_frame + 1
        if hero_frame > 2:
            hero_frame = 0
        hero_time = 0
  
  elif keys[pygame.K_UP]: #Cima
    dir = 0
    hero_pos_y = hero_pos_y - (0.1 * dt)
    hero_time = hero_time + dt
    if hero_time > 100:
        hero_frame = hero_frame + 1
        if hero_frame > 2:
            hero_frame = 0
        hero_time = 0

  #Condicionais de colisão (verifica se o personagem colidiu com a região delimitada)
  collider_jogador = pygame.Rect(hero_pos_x, hero_pos_y, 64, 64)
  if collider_jogador.colliderect(collider_mapa1):
    hero_pos_x = old_x
    hero_pos_y = old_y
    
  if collider_jogador.colliderect(collider_mapa2):
    hero_pos_x = old_x
    hero_pos_y = old_y
   
  if collider_jogador.colliderect(collider_mapa3):
    hero_pos_x = old_x
    hero_pos_y = old_y

  if collider_jogador.colliderect(collider_mapa4):
    hero_pos_x = old_x
    hero_pos_y = old_y
    
  if collider_jogador.colliderect(collider_mapa5):
    hero_pos_x = old_x
    hero_pos_y = old_y

  if collider_jogador.colliderect(collider_mapa6):
    hero_pos_x = old_x
    hero_pos_y = old_y

def draw_screen(screen):
  screen.fill((152,209,250))

  #Preenchimento do Mapa (Seleção do sprite) 
  for i, linha in enumerate(mapa):
    for j, char in enumerate(linha):
      if char == "G":
        screen.blit(tilset, (j*64, i*64), (0, 0, 64, 64))
      elif char == "F":
        screen.blit(tilset, (j*64, i*64), (0, 64, 64, 64))
      elif char == "B":
        screen.blit(tilset, (j*64, i*64), (0, 128, 64, 64))
      elif char == "T":
        screen.blit(tilset, (j*64, i*64), (64, 0, 64, 64))
      elif char == "R":
        screen.blit(tilset, (j*64, i*64), (64, 64, 64, 64))
      elif char == "C":
        screen.blit(tilset, (j*64, i*64), (64, 128, 64, 64))
      elif char == "A":
        screen.blit(tilset, (j*64, i*64), (128, 0, 64, 64))
      elif char == "P":
        screen.blit(tilset, (j*64, i*64), (128, 64, 64, 64))
      elif char == "S":
        screen.blit(tilset, (j*64, i*64), (128, 128, 64, 64))
      

  #desenha o personagem usando o indice da animação (Seleção do sprite)
  screen.blit(sheet,(hero_pos_x, hero_pos_y),(spt_wdt * hero_frame,dir*spt_hgt,spt_wdt,spt_hgt))

def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT: # fechamento do prog
                running = False
                break

        # Define FPS máximo
        clock.tick(60)
        # Tempo transcorrido desde a última atualização 
        dt = clock.get_time()
        # Atualiza posição dos objetos
        update(dt)
        # Desenha objetos
        draw_screen(screen)
        # Pygame atualiza a visualização da tela
        pygame.display.update()

# Programa principal
pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()
