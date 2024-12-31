#####################################################
# Jogos não gráficos
# Tarefa 8.4 - Adivinhação Usuário
# Aluno: Everton Pereira Militão
#####################################################
# Usar somente python com a tela interativa.
# Não é para usar o Pygame e nem o Turtle.
#####################################################
import random

#Função:
def jogoAdivinha():
  s = "SIM"
  print("<---------------Jogo da Adivinhação---------------->")
  while s == "SIM":

    # Variáveis:
    numero_sorteado = random.randint(1,1023)
    numero_adivinha = 0
    contador = 1
    numero_adivinha = 0
    print("\n\n\n\n<--------------------------------------->")
    
    
    #Verificando se o número é válido:
    while numero_adivinha != numero_sorteado:
      numero_adivinha = (input("Digite um número:"))
      ehNumero = numero_adivinha.isnumeric()
      
      while ehNumero is False:
        numero_adivinha = (input("Digito inválido, tente novamente:"))
        ehNumero = numero_adivinha.isnumeric()
        if ehNumero is True:
          
          break
      
      while 0 < int(numero_adivinha) > 1023:
        numero_adivinha = int(input("Número inválido digite novamente:"))
      
      #Verificando se o número é maior ou menor: 
      if int(numero_adivinha) == numero_sorteado:
        print("=")
        print("Parabéns, você acertou!O numero sorteado é %d: " %numero_sorteado )
        print("Número de TENTATIVAS: %d" %(contador))
        contador +=1
        print("<---------------FIM---------------->")
        break
        
      elif int(numero_adivinha) > numero_sorteado:
        print("Numero \t > \t  Sorteado")
        contador += 1
    
      else:
        print("Numero \t < \t Sorteado")
        contador += 1
        
    
    s = input("Jogar novamente?Digite 'sim' ou 'não':").upper()

#Bloco principal  
jogoAdivinha()
print("JOGO ENCERRADO")
