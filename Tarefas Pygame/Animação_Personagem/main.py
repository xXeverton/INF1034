# Utilize como base o código do exemplo 1 ou 2.
# Basta copiar e colar aqui um deles.
import pygame
width = 800
height = 600
hero_frame = 1
hero_pos_x = 100
hero_pos_y = 225
hero_time = 0
dir = 3

def load():
    global clock, sheet, spt_wdt, spt_hgt, hero_frame
    clock = pygame.time.Clock()
    sheet = pygame.image.load("sprite_sheet.png")  # 4 x 4 
    spt_wdt = sheet.get_width() / 4    # Largura de um sprite
    spt_hgt = sheet.get_height() / 4   # Altura de um sprite

def update(dt):
    global hero_frame, hero_pos_x, hero_time, dir, hero_pos_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:  
      dir = 3
      hero_pos_x = hero_pos_x + (0.1 * dt)
      hero_time = hero_time + dt
      if hero_time > 100:
        hero_frame = hero_frame + 1
        if hero_frame > 3:
            hero_frame = 0
        hero_time = 0

  
    elif keys[pygame.K_LEFT]:
      dir = 2
      hero_pos_x = hero_pos_x - (0.1 * dt)
      hero_time = hero_time + dt
      if hero_time > 100:
        hero_frame = hero_frame + 1
        if hero_frame > 3:
            hero_frame = 0
        hero_time = 0
    
    elif keys[pygame.K_UP]:
      dir = 1
      hero_pos_y = hero_pos_y - (0.1 * dt)
      hero_time = hero_time + dt
      if hero_time > 100:
          hero_frame = hero_frame + 1
          if hero_frame > 3:
              hero_frame = 0
          hero_time = 0

    elif keys[pygame.K_DOWN]:
      dir = 0
      hero_pos_y = hero_pos_y + (0.1 * dt)
      hero_time = hero_time + dt
      if hero_time > 100:
          hero_frame = hero_frame + 1
          if hero_frame > 3:
              hero_frame = 0
          hero_time = 0
  

def draw_screen(screen):
    screen.fill((255,255,255))
    #desenha o personagem usando o indice da animação (Seleção do sprite)
    screen.blit(sheet,(hero_pos_x, hero_pos_y),(spt_wdt * hero_frame,dir*spt_hgt,spt_wdt,spt_hgt))


#####################################################
# A PRINCIPIO NÃO PRECISA ALTERAR DAQUI PRA BAIXO   #
#####################################################
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