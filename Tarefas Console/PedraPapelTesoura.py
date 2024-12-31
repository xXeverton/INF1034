#####################################################
# Jogos não gráficos
# Tarefa 8.3 - Pedra, Papel, Tesoura
# Aluno: Everton Pereira Militão
#####################################################
# Usar somente python com a tela interativa.
# Não é para usar o Pygame e nem o Turtle.
#####################################################
#Falta travar a entrada apenas de numeros no usuario
#Módulos:
import random

#Funções:
def verificaNum(numero):
  while numero != 1 and numero != 2 and numero !=3: 
    numero = int(input("Entre com sua escolha 1 (pedra), 2 (papel) ou 3 (tesoura): "))

def jogoPedraPapelTesoura():
  s = "SIM"
  contador = 1
  print("<-------------------PEDRA,PAPEL,TESOURA-------------------------->\n\n")
  while s == "SIM":
    
  
    #número 1 representa pedra, 2 representa papel e 3 representa tesoura
    possibilidade = [1, 2, 3]
    computador = random.choice(possibilidade)
    print("\n--------------------RODADA%d----------------------------" %contador) 
    usuario = int(input("Entre com sua escolha 1 (pedra), 2 (papel) ou 3 (tesoura): "))
    verificaNum(usuario)
    
    print("Escolha do computador: %s" %(computador))
    
    #TRASNFORMANDO A NUMERAÇÃO EM UMA POSSIBILIDADE
    #PARA O COMPUTADOR 
    if computador == 1:
      escComp = "PEDRA"
    elif computador == 2:
      escComp = "PAPEL"
    else:
      escComp = "TESOURA"
    
    #PARA O USUARIO
    if usuario == 1:
      escolhaUsuario = "PEDRA"
    elif usuario == 2:
      escolhaUsuario ="PAPEL"
    else:
      escolhaUsuario = "TESOURA"
    
    #GERENCIANDO as jogadas de acordo com as possibilidades escolhidas:
    
      #Em Caso de EMPATE:
    if (usuario == computador):
      print("Usuário:%s Computador: %s"% (escolhaUsuario, escComp))
      print("Empate!")
      
    #Em caso de Vitória do COMPUTADOR:
    else:
      if computador == 1 and usuario == 3 or \
      (computador == 2 and usuario == 1) or \
      (computador == 3 and usuario == 2):
        
        print("Usuário:%s Computador: %s" % (escolhaUsuario, escComp))
        print("Computador ganhou!")
        print("------------------------FIM----------------------------\n\n") 

      else:
        print("Usuário:%s Computador: %s" % (escolhaUsuario, escComp))
        print("Usuário ganhou!")
        print("------------------------FIM----------------------------\n\n") 
    contador += 1
    s = input("Jogar novamente?Digite 'sim' ou 'não':").upper()
    
#Bloco Principal:
jogoPedraPapelTesoura()
print("JOGO ENCERRADO")
