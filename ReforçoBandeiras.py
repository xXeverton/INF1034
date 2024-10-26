import turtle

t = turtle.Turtle()
t.speed(0)
#Funções:
def triangulo(posX, posY, extensão, cor):
  t.penup()
  t.goto(posX, posY)
  t.lt(90)
  t.fillcolor(cor)
  t.begin_fill()
  for x in range(3):
    t.fd(extensão)
    t.lt(240) 
  t.end_fill()
  t.rt(90)
  

def retangulo(posX, posY, largura, altura, cor):
  t.penup()
  t.goto(posX, posY)
  t.pendown()
  t.fillcolor(cor)
  t.begin_fill()
  for x in range(2):
    t.fd(largura)
    t.lt(90)
    t.fd(altura)
    t.lt(90)
  t.end_fill()
  t.fd(largura)

def estrela(posX, posY, tamanho, cor):
  t.penup()
  t.goto(posX, posY)
  #t.pendown()
  t.fillcolor(cor)
  t.begin_fill()
  
  for x in range(5):
    t.fd(tamanho)
    t.rt(144)
  
  t.end_fill()

  t.fillcolor(cor)
  t.begin_fill()
  t.penup()
  t.fd(tamanho/3)
  #t.pendown()
  
  for x in range(5):
    t.fd(tamanho-29)
    t.rt(72)
  t.end_fill()

def meia_lua(posX1, posY1, posX2, posY2,  raio1, raio2, cor1, cor2):
  #círculo maior
  t.penup()
  t.goto(posX1, posY1)
  t.rt(240)
  t.pendown()
  t.fillcolor(cor1)
  t.begin_fill()
  t.circle(raio1)
  t.end_fill()

  #círculo menor
  t.penup()
  t.goto(posX2, posY2)
  t.fillcolor(cor2)
  t.begin_fill()
  t.circle(raio2)
  t.end_fill()
  t.penup()
  t.home()
  t.pendown()

def circulo(posX, posY, raio, cor):
  t.penup()
  t.goto(posX, posY)
  t.lt(90)
  t.pendown()
  t.fillcolor(cor)
  t.begin_fill()
  t.circle(raio)
  t.end_fill()
  t.penup()
  t.home()
  t.pendown()

#Bloco Principal:
#Bandeira Bélgica:
retangulo(-200, 100, 30, 60, "black")
retangulo(-200+30, 100, 30, 60, "yellow")
retangulo(-200+60, 100, 30, 60, "red")

#Bandeira França:
retangulo(-110, 100, 30, 60, "blue")
retangulo(-110+30, 100, 30, 60, "White")
retangulo(-110+60, 100, 30, 60,"red")

#Bandeira Alemanha:
retangulo(-20, 100, 75, 60,"black")
retangulo(-20, 100, 75, 40, "red")
retangulo(-20, 100, 75, 20, "yellow")

#Bandeira Bukinafaso:
retangulo(55, 100, 75, 60,"red")
retangulo(55, 100, 75, 30, "white")

#Bandeira Republica Checa:
retangulo(130, 100, 75, 60,"red")
retangulo(130, 100, 75, 30, "white")
triangulo(130, 100, 60, "blue")

#Bandeira Vietnam:
retangulo(130, 100, 75, -60,"red")
estrela(148, 75, 40, "yellow")

#Bandeira Maldivas:
retangulo(55, 100, 75, -60, "red")
retangulo(69, 53, 50, 39, "green")
meia_lua(105, 80, 108, 79, 15, 11, "white", "green")


#Bandeira Somália:
retangulo(-20, 100, 75, -60,"blue")
retangulo(-20, 100, 75, -60,"blue")
estrela(-3, 75, 40, "white")

#Bandeira Japão:
retangulo(-110, 100, 90, -60, "white")
circulo(-50, 70, 15, "red")

#Bandeira Brasil:
retangulo(-200, 100, 90, -60, "green")
triangulo(-155, 100, -56, "yellow")

triangulo(-155, 100-56, -56*-1, "yellow")
circulo(-140, 70, 15, "blue")

#Bandeira Bahamas:
retangulo(130, 40, 75, -60,"lightblue")
retangulo(130, 40, 75, -40, "yellow")
retangulo(130, 40, 75, -20, "lightblue")
triangulo(130, -20, 60, "black")

#Bandeira Birmania: 
retangulo(55, 40, 75, -60,"yellow")
retangulo(55, 40, 75, -40, "green")
retangulo(55, 40, 75, -20, "red")
estrela(73, 15, 40, "white")






t.hideturtle()

