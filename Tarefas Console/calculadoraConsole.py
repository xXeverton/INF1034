#####################################################
# Jogos não gráficos
# Tarefa 8.1 - Calculadora
# Aluno:Everton Pereira Militão
#####################################################
# Usar somente python com a tela interativa.
# Não é para usar o Pygame e nem o Turtle.
#####################################################
#Módulos: 
import math

#Funções -> Fazer funções para cada operação
def calculaSoma(x, y):
  soma = x + y
  return print("O resultado é: %.2f" %soma)

def calculaSubtracao(x, y):
  subtracao = x - y
  return print("O resultado é: %.2f" %subtracao)

def calculaMultiplicacao(x, y):
  multiplicacao = x*y
  return print("O resultado é: %.2f" %multiplicacao)

def calculaDivisao(x , y):
  if y == 0:
    return print("Infity")
  else:
    divisao = x/y
    return print("O resultado é: %.2f" %divisao)

def calculaPorcentagem(x):
  porcentagem = x/100
  return print("O resultado é: %.2f" %porcentagem)

def calculaPotencia(x, y):
  potencia = math.pow(x, y)
  return print("O resultado é: %.2f" %potencia)


#Bloco Principal:
contador = 1
print("\n")
print("Instuções de uso: ")
print("Digite o Operando 1, entre com o operador e entre com o operando 2 ")
print("Para encerrar a calculadora digite SAIR no operador!")

while True: #Executa a calculadora até que o usuario encerre o programa
  print("\n\n<-----------CONTA%d------------>" %(contador))
  operadoresBasicos = "+", "-", "*", "/", "%", "^", "SAIR"
  operando1 = float(input("Entre com o operando 1:\t "))
  operador = str(input("Entre com o operador:\t "))
  if operador == "SAIR":#Condição para parar a calculadora
    break
  operando2 = 0
  
  while operador not in operadoresBasicos:#caso o usuário erre o operador!
      operador = str(input("Entre com o operador novamente:\t "))
    
  if operador == "%":
    print("------------------------------------")
    calculaPorcentagem(operando1)
     
  else:#operando 2
    operando2 = float(input("Entre com o operando 2:\t "))
    print("-------------------------------")

  #Definindo qual função será chamada com a entrada do operador
  if operador == "+":
    calculaSoma(operando1, operando2)
  
  elif operador == "-":
    calculaSubtracao(operando1, operando2)
  
  elif operador == "*":
    calculaMultiplicacao(operando1, operando2)
  
  elif operador == "/":
    calculaDivisao(operando1, operando2)
  
  elif operador == "^":
    calculaPotencia(operando1, operando2)
  contador += 1
  
print("FIM CALCULADORA")

#############FIM#############
