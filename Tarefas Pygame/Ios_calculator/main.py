import pygame

#Configurando a tela:
width = 800  # Largura Janela
height = 600  # Altura Janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("IOS_CALCULATOR")
white = (255, 255, 255)
numeros_visor = ["", ""]


def word(text, font, text_color, x, y):
  visor_texto = font.render(text, True, text_color)
  screen.blit(visor_texto, (x, y))


#Definindo fontes
pygame.font.init()
sys_font1 = pygame.font.Font("fontIos.OTF", 100)
sys_font = pygame.font.Font("fontIos.OTF", 20)


def text():
  global numero_no_visor
  global numeros_visor
  t = sys_font.render("".join(numeros_visor), True, (255, 255, 255))
  screen.blit(t, t.get_rect(top=120, left=220))
  numero_no_visor = str("".join(numeros_visor))


#Desenhando a Calculadora:
def draw_screen():
  # Preenche o fundo da tela
  screen.fill((17, 17, 17))

  #tela:
  pygame.draw.rect(screen, (0, 0, 0), (200, 40, 250, 450), 200, 50)
  pygame.draw.rect(screen, (192, 192, 192), (200, 40, 250, 450), 5, 50)

  #1ª Linha
  pygame.draw.rect(screen, (192, 192, 192), (220, 200, 45, 45), 200, 50)  #ac
  pygame.draw.rect(screen, (192, 192, 192), (275, 200, 45, 45), 200, 50)  #+/-
  pygame.draw.rect(screen, (192, 192, 192), (325, 200, 45, 45), 200, 50)  #%
  pygame.draw.rect(screen, (255, 165, 0), (375, 200, 45, 45), 200, 50)  #/
  #2ª Linha
  pygame.draw.rect(screen, (101, 101, 101), (220, 250, 45, 45), 200, 50)  #7
  pygame.draw.rect(screen, (101, 101, 101), (275, 250, 45, 45), 200, 50)  #8
  pygame.draw.rect(screen, (101, 101, 101), (325, 250, 45, 45), 200, 50)  #9
  pygame.draw.rect(screen, (255, 165, 0), (375, 250, 45, 45), 200, 50)  #*
  #3ª Linha
  pygame.draw.rect(screen, (101, 101, 101), (220, 300, 45, 45), 200, 50)  #4
  pygame.draw.rect(screen, (101, 101, 101), (275, 300, 45, 45), 200, 50)  #5
  pygame.draw.rect(screen, (101, 101, 101), (325, 300, 45, 45), 200, 50)  #6
  pygame.draw.rect(screen, (255, 165, 0), (375, 300, 45, 45), 200, 50)  #-
  #4ª Linha
  pygame.draw.rect(screen, (101, 101, 101), (220, 350, 45, 45), 200, 50)  #1
  pygame.draw.rect(screen, (101, 101, 101), (275, 350, 45, 45), 200, 50)  #2
  pygame.draw.rect(screen, (101, 101, 101), (325, 350, 45, 45), 200, 50)  #3
  pygame.draw.rect(screen, (255, 165, 0), (375, 350, 45, 45), 200, 50)  #+
  #5ª Linha
  pygame.draw.rect(screen, (101, 101, 101), (220, 400, 90, 45), 200, 50)  #0
  pygame.draw.rect(screen, (101, 101, 101), (325, 400, 45, 45), 200, 50)  #C
  pygame.draw.rect(screen, (255, 165, 0), (375, 400, 45, 45), 200, 50)  #=

  #Detalhes calculadora:
  pygame.draw.rect(screen, (255, 255, 255), (275, 460, 100, 10), 5, 50)

  #Digitos/operadores e afins...
  #C
  texto = sys_font.render("C", True, (0, 0, 0))
  screen.blit(texto, (234, 209))
  #+/-
  texto = sys_font.render("+/-", True, (0,0,0))
  screen.blit(texto, (284, 209))
  #%
  texto = sys_font.render("%", True, (0, 0, 0))
  screen.blit(texto, (340, 209))

  #/
  texto = sys_font.render("÷", True, (0, 0, 0))
  screen.blit(texto, (392, 209))
  #×
  texto = sys_font.render("×", True, (0, 0, 0))
  screen.blit(texto, (392, 260))
  #-
  texto = sys_font.render("-", True, (0, 0, 0))
  screen.blit(texto, (393, 310))
  #+
  texto = sys_font.render("+", True, (0, 0, 0))
  screen.blit(texto, (392, 360))
  #=
  texto = sys_font.render("=", True, (0, 0, 0))
  screen.blit(texto, (392, 408))
  #7
  texto = sys_font.render("7", True, (255, 255, 255))
  screen.blit(texto, (237, 260))
  #4
  texto = sys_font.render("4", True, (255, 255, 255))
  screen.blit(texto, (237, 311))
  #1
  texto = sys_font.render("1", True, (255, 255, 255))
  screen.blit(texto, (237, 361))
  #0
  texto = sys_font.render("0", True, (255, 255, 255))
  screen.blit(texto, (237, 412))
  #8
  texto = sys_font.render("8", True, (255, 255, 255))
  screen.blit(texto, (292, 260))
  #5
  texto = sys_font.render("5", True, (255, 255, 255))
  screen.blit(texto, (292, 311))
  #2
  texto = sys_font.render("2", True, (255, 255, 255))
  screen.blit(texto, (292, 361))
  #9
  texto = sys_font.render("9", True, (255, 255, 255))
  screen.blit(texto, (342, 260))

  #6
  texto = sys_font.render("6", True, (255, 255, 255))
  screen.blit(texto, (342, 311))

  #3
  texto = sys_font.render("3", True, (255, 255, 255))
  screen.blit(texto, (342, 361))


#Operando
def number_click(x, number):
  global n1
  mouse_click = pygame.mouse.get_pressed()
  if mouse_click[0] and number.collidepoint(pygame.mouse.get_pos()) == True:
    numeros_visor.append(str(x))
    if x == "+" or x == "*" or x == "/" or x == "-":
      n1 = float(str(numero_no_visor[0:]))
    elif x == "%":
      n1 = float(str(numero_no_visor[0:])) / 100
    elif x ==  '~':
      n1 = float(str(numero_no_visor[0:]))* -1


#Operações
def simbolo_igual():
  global n2, num_i, n_p, n1
  mouse_click = pygame.mouse.get_pressed()
  if mouse_click[0] and num_i.collidepoint(pygame.mouse.get_pos()) == True:
    numero_igual = str(numero_no_visor + "=")
    a1 = numero_igual.find("+")
    a2 = numero_igual.find("*")
    a3 = numero_igual.find("-")
    a4 = numero_igual.find("/")
    a5 = numero_igual.find("%")
    a6 = numero_igual.find("~")

    if a1 != -1:
      n2 = float(int(numero_igual[a1 + 1:-1]))
      numeros_visor.clear()
      numeros_visor.append(str(n1 + n2))
    elif a2 != -1:
      n2 = float(int(numero_igual[a2 + 1:-1]))
      numeros_visor.clear()
      numeros_visor.append(str(n1 * n2))
    elif a1 != -1:
      n2 = float(int(numero_igual[a2 + 1:-1]))
      numeros_visor.clear()
      numeros_visor.append(str(n1 + n2))
    elif a3 != -1:
      n2 = float(int(numero_igual[a3 + 1:-1]))
      numeros_visor.clear()
      numeros_visor.append(str(n1 - n2))
    elif a4 != -1:
      n2 = float(int(numero_igual[a4 + 1:-1]))
      if n2 == 0:
        numeros_visor.clear()
        numeros_visor.append('Division by Zero!')
      else:
        numeros_visor.clear()
        numeros_visor.append(str(n1 / n2))
    elif a5 != -1:
      numeros_visor.clear()
      numeros_visor.append(str(n1))
    elif a6 != -1:
      numeros_visor.clear()
      numeros_visor.append(str(n1))


def nova_conta():
  global numero_visor, num_c
  mouse_click = pygame.mouse.get_pressed()
  if mouse_click[0] and num_c.collidepoint(pygame.mouse.get_pos()) == True:
    numeros_visor.clear()


clock = pygame.time.Clock()


def uptade():
  number_click("0", num_0)
  number_click("1", num_1)
  number_click("2", num_2)
  number_click("3", num_3)
  number_click("4", num_4)
  number_click("5", num_5)
  number_click("6", num_6)
  number_click("7", num_7)
  number_click("8", num_8)
  number_click("9", num_9)
  number_click("+", num_a)
  number_click("-", num_s)
  number_click("*", num_m)
  number_click("/", num_d)
  number_click("%", num_p)
  number_click("~", num_menos1)
  simbolo_igual()
  nova_conta()


#Loop Principal
running = True
while running:
  draw_screen()
  num_1 = pygame.Rect(220, 350, 45, 45)
  num_2 = pygame.Rect(275, 350, 45, 45)
  num_3 = pygame.Rect(325, 350, 45, 45)
  num_4 = pygame.Rect(220, 300, 45, 45)
  num_5 = pygame.Rect(275, 300, 45, 45)
  num_6 = pygame.Rect(325, 300, 45, 45)
  num_7 = pygame.Rect(220, 250, 45, 45)
  num_8 = pygame.Rect(275, 250, 45, 45)
  num_9 = pygame.Rect(325, 250, 45, 45)
  num_0 = pygame.Rect(220, 400, 90, 45)
  num_a = pygame.Rect(375, 350, 45, 45)
  num_s = pygame.Rect(375, 300, 45, 45)
  num_m = pygame.Rect(375, 250, 45, 45)
  num_i = pygame.Rect(375, 400, 45, 45)
  num_c = pygame.Rect(220, 200, 45, 45)
  num_d = pygame.Rect(375, 200, 45, 45)
  num_p = pygame.Rect(325, 200, 45, 45)
  num_menos1 = pygame.Rect(275, 200, 45, 45)
  text()
  for evente in pygame.event.get():
    if evente.type == pygame.MOUSEBUTTONDOWN:
      uptade()

  clock.tick(60)
  pygame.display.update()

pygame.quit()
