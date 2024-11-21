"""
Nome: Everton Pereira Militão
Matrícula: 2320462
Observação: O código quando iniciado apresenta todas as partes em ordem conforme instruções, cada desenho é feito e assim são contados dois segundos até que a tela seja limpa e comece outro desenho.
"""

#Módulos:
import turtle
from turtle import Screen
import random
from time import sleep
import math

#Definindo variáveis e Configurando a tartaruga:
t = turtle.Turtle()
lado = 80
raio = 44
passo = 0.5

#Parte 1-> Figuras geometricas no plano
#Funções:
#Plano Cartesiano

def planoCartesiano(x, y):
  #Fazer eixo x 
  t.setpos(x,0)
  t.fd(800)
  t.stamp()
  t.penup()

  #Fazer eixo y
  t.setpos(0, y)
  t.pendown()
  t.lt(90)
  t.fd(600)
  t.stamp()
  t.penup()
t.pendown()
#Fim_Plano Cartesiano

#Para fazer o quadrado:
cor_quadrado = turtle.textinput("Cor do quadrado:", "")
def quadrado(lado):
  t.penup()
  t.setpos(random.randint(15,300), random.randint(30,120))
  t.rt(90)
  t.fd(30)
  t.fillcolor(cor_quadrado)
  t.begin_fill()
  t.pendown()
  for i in range(4):
    t.fd(lado)
    t.lt(90)
  t.end_fill()
#Fim_quadrado

#Fazer triângulo
cor_triangulo = turtle.textinput("Cor do triângulo:", "")
def triangulo(lado):
    t.penup()
    t.setpos(random.randint(15,300), random.randint(30,150)*-1)
    t.fillcolor(cor_triangulo)
    t.begin_fill()
    t.pendown()
    for i in range(3):
      t.fd(lado)
      t.rt(120)
    t.end_fill()
#Fim_triângulo

#Fazer o circulo:
cor_circulo = turtle.textinput("Cor do circulo:", "")
def circle(raio):
  t.penup()
  t.setpos(random.randint(44,280)*-1, random.randint(50,150)*-1)
  t.rt(90)
  t.pendown()
  t.fillcolor(cor_circulo)
  t.begin_fill()
  t.circle(44)
  t.end_fill()
#Fim_circulo

#Fazer Espiral no Sentido horário:
def espiralHora(passo):
  t.penup()
  t.setpos(random.randint(50,300)*-1, random.randint(60,200))
  t.pendown()
  t.lt(180)

  for x in range(40):
    t.fd(passo*x)
    t.rt(45)
#Fim_EspiralHora

#Fazer Espiral no sentido Anti-Horário:
def espiralAnti(passo):
  t.penup()
  t.setpos(random.randint(50,300)*-1, random.randint(80,200))
  t.lt(180)
  t.fd(120)
  t.pendown()

  for x in range(40):
    t.fd(passo*x)
    t.lt(45)
#Fim_EspiralAnti
  
#Bloco Principal da Parte_1:
planoCartesiano(-400,-300)
quadrado(lado)
triangulo(lado)
circle(raio)
espiralHora(passo)
t.penup()
t.home()
espiralAnti(passo)

sleep(2)
Screen().clear()
t = turtle.Turtle()
t.setpos(0,0)
#Fim_PARTE1

#Parte 2 -> Bandeiras 

#Funções da Parte_2:
#Retângulo:
def retangulo(posX, posY, largura, altura, cor):
  t.penup()
  t.setpos(posX, posY)
  t.pendown()
  t.fillcolor(cor)
  t.begin_fill()

  for i in range(2):
    t.fd(largura)
    t.rt(90)
    t.fd(altura)
    t.rt(90)
    
  t.end_fill()

#Função de ajuste da tartaruga:
def ajuste(frente, direita, esquerda):
  t.penup()
  t.fd(frente)
  t.rt(direita)
  t.lt(esquerda)
  t.pendown()
  
def circulo(posX, posY, raio, cor):
  t.penup()
  if cor == "white":
    t.lt(90)
  t.setpos(posX, posY)
  t.fillcolor(cor)
  t.begin_fill()
  t.circle(raio)
  t.end_fill()
  t.pendown()

def estrela(posX, posY, tamanho, cor):
  t.penup()
  t.setpos(posX, posY)
  t.rt(90)
  t.fillcolor(cor)
  t.begin_fill()
  
  for x in range(5):
    t.fd(tamanho)
    t.left(144)
    
  t.end_fill()
  
  t.fillcolor("white")
  t.begin_fill()
  t.fd(tamanho)
  t.left(144)
  t.fd(tamanho)
  t.left(144)
  t.fd(tamanho/2)
  
  t.end_fill()
  t.hideturtle()
  
def triangulo(cor):
  t.fillcolor(cor)
  t.begin_fill()
  t.setpos(0,0)
  t.setpos(-230,-150)
  t.end_fill()
  
  t.end_fill()

def estrela_7pontos(xPos, yPos, tamanho, cor):
  t.penup()
  t.setpos(xPos, yPos)
  t.lt(120)
  t.pendown()
  
  t.penup()
  t.fillcolor(cor)
  t.begin_fill()

  for i in range(7):
    t.fd(tamanho)
    t.rt(180-180/7)
  t.end_fill()

  t.fd(16)
  t.rt(100)
  t.fd(4)
  t.fillcolor("white")
  t.begin_fill()
  t.circle(8)
  t.end_fill()
  t.hideturtle()

  
#Bloco Principal Parte_2:

#Bandeira Bélgica
retangulo(-250, 250, 150, 400, "black")
ajuste(150, 0, 0)
retangulo(-100, 250, 150, 400, "yellow")
ajuste(150, 0, 0)
retangulo(50, 250, 150, 400, "red")

#Espera 2 segundos e limpa tela para começar outro desenho
sleep(2)
Screen().clear()
t = turtle.Turtle()
t.setpos(0,0)
#Fim_bandeiraBelgica

#Bandeira Turquia
retangulo(-250, 250, 500, 480, "red")
ajuste(150, 0, 0)
circulo(-30, 0, 100, "white")
circulo(-25, 0, 77, "red")
estrela(-30, 0, 100, "white")

#Espera 2 segundos e limpa tela para começar outro desenho
sleep(2)
Screen().clear()
t = turtle.Turtle()
t.setpos(0,0)
#Fim_bandeiraTurquia

#Bandeira Jordânia
retangulo(-230, 150, 460, 300, "lightgreen")
retangulo(-230, 150, 460, 100, "black")
ajuste(0, 90, 0)
ajuste(100, 0, 90)
retangulo(-230, 50, 460, 100, "white")
ajuste(0, 0, 90)
ajuste(100, 90, 0)
triangulo("red")
estrela_7pontos(-143, -15, 44, "white")

#Espera 2 segundos e limpa tela para começar outro desenho
sleep(2)
Screen().clear()
t = turtle.Turtle()
t.setpos(0,0)
#Fim_Parte2

"""
Parte 3 -> Plotar funções matemáticas no plano cartesiano
"""
#Definindo constantes, elas foram utilizadas para alterar a escala do gráfico, ou seja, transladar seus eixos para que fiquem visiveis na tela. 
#Escala do Eixo X:
escala1 = 25
escala2 = 2
escala3 = 15
escala4 = 30
escala5 = 10
escala6 = 15

#Escala do Eixo Y:
escala1y = 25
escala2y = 400
escala3y = 5
escala4y = 25
escala5y = 5
escala6y = 25

t.speed(0)
#Funções:
def planoCartesiano2():
  #Eixo x
  t.penup()
  t.fd(400)
  t.pendown()
  t.stamp()
  t.fd(-800)
  t.fd(400)
  
  #Eixo y
  t.lt(90)
  t.fd(400)
  t.stamp()
  t.fd(-800)
  t.fd(400)
  t.penup()

  #Fazer marcações:
  for i in range(8):
    t.rt(90)
    t.pendown()
    t.fd(45)
    t.lt(90)
    t.fd(4)
    t.fd(-4)
    t.penup()
    t.pendown()

  t.home()
  for i in range(8):
    t.lt(90)
    t.pendown()
    t.fd(45)
    t.rt(90)
    t.fd(4)
    t.fd(-4)
    t.penup()
    t.pendown()
  
    
  t.home()
  for i in range(8):
    t.rt(90)
    t.pendown()
    t.fd(45)
    t.lt(90)
    t.fd(4)
    t.fd(-4)
    t.penup()
    t.pendown()
  t.home()
  t.lt(180)

  for i in range(8):
    #t.rt(90)
    t.pendown()
    t.fd(45)
    t.rt(90)
    t.fd(4)
    t.fd(-4)
    t.lt(90)
    t.penup()
    t.pendown()

  t.home()
  t.penup()

#1) y = Vx
def function1(x, escala, escala2):
  t.pendown()
  t.goto(x*escala, math.sqrt(x)*escala1y)

#Voltar pra posição Inicial 
def posInicial():
  t.penup()
  t.home()
  
#2) y = 1/x
def function2(x, escala, escala2):
  t.goto(x*escala, ((1/x)*escala2))
  t.pendown()
  
#3) y = 2^x
def function3(x, escala, escala2):
  t.goto(x*escala3, math.pow(2, x)*escala3y)
  t.pendown()
  
#4) y = 5 - x^2
def function4(x, escala, escala2):
  t.goto(x*escala4, (5- math.pow(x, 2))*escala4y)
  t.pendown()
  
#5) y = x^2 - 5x + 6
def function5(x, escala, escala2):
  t.goto(x*escala5, (math.pow(x, 2) - 5*x + 6)*escala5y)
  t.pendown()

#6) y = x^3 - x^2 -x + 1
def function6(x, escala, escala2):
  t.goto(x*escala6, ((math.pow(x, 3) - (math.pow(x,2)) - x +1)* escala6y))
  t.pendown()

#Bloco Principal Parte_3:
planoCartesiano2()

#Função 1:
t.color("green")
for x_1 in range(1, 400):
  function1(x_1, escala1, escala1y)

posInicial()

#Função 2:
t.color("blue")
for x_2 in range(-300, 0):
  function2(x_2, escala2, escala2y)

for x_2 in range(1, 200):
  function2(x_2, escala2, escala2y)

posInicial()

#Função 3:
t.color("cyan")
for x_3 in range(-10, 10):
  function3(x_3, escala3, escala3y)

posInicial()

#Função 4:
t.color("brown")
for x_4 in range(-10, 20):
  function4(x_4, escala4, escala4y)

posInicial()

#Função 5:
t.color("orange")
for x_5 in range(-10, 20):
  function5(x_5, escala5, escala5y)

posInicial()

#Função 6:
t.color("red")
for x_6 in range(-10, 20):
  function6(x_6, escala6, escala6y)
  
posInicial()

"""Fim_Parte3"""