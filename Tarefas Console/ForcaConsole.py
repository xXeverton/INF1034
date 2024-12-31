#####################################################
# Jogos não gráficos
# Tarefa 8.2 - Forca
# Aluno:Everton Pereira Militão 
#####################################################
# Usar somente python com a tela interativa.
# Não é para usar o Pygame e nem o Turtle.
#####################################################
 #Funções: 
#Criar duas funções nos quais verificam se a palavra inserida é valida para o jogo
def verificaPalavra(palavra):
  for letra in palavra:
    if not letra.isalpha(): 
      return False
  return True

def verificaPalavraInserida():
  while True:
    palavraSecreta = input('Digite a palavra secreta:\t').upper()
    if verificaPalavra(palavraSecreta):
      return palavraSecreta

    else:
     print("A palavra inserida deve conter apenas letras. Tente novamente!")

def jogoAdivinha():
  s = "SIM"
  while s == 'SIM':


    palavraSecreta = verificaPalavraInserida()
    
    print("\n"*100)
    # Cria uma lista com o tamanho da palavra secreta e com underlines
    listOculto = ["_"] * len(palavraSecreta)
    lista = list(palavraSecreta)#Cria uma lista com as letras da palavraSecerta
    tentativas = len(palavraSecreta)#Verifica a quatidades de letras da palavra secreta

    #Cria um laço no qual o jogador continua até acertar a palavra
    while tentativas > 0:
      #letra sugerida pelo usuário
      sugerida = str(input("Entre com uma letra:\t ")).upper()
      #Verifica se a letra sugerida está na palavraSecreta
      if sugerida in lista:
        print("Certo!")
        indice = lista.index(sugerida)
        #Verifica quantas vezes a letra sugerida aparece na palavraSecreta
        for indice in range(len(lista)):
          if lista[indice] == sugerida:
            listOculto[indice] = sugerida
        print("".join(listOculto)) #.join-> ele vai unir a string da lista
        
        print("TENTATIVAS RESTANTES: %d" %tentativas)
        print("------------------------------------------------")
    
      else:
        tentativas -= 1
        print("TENTATIVAS RESTANTES: %d" %tentativas)
        print("------------------------------------------------")
        
      if "_" not in listOculto:
        print("Fim! Você ganhou! A palavra é %s 👏👏👏" %palavraSecreta)
        print("------------------------------------------------")
        break
    
      if tentativas == 0:
        print("Tente novamente, você perdeu 😢")
        print("------------------------------------------------")
      
    s = input("Deseja jogar novemente?Digite 'sim' ou 'não':?\t").upper()
    
#Bloco Principal:

jogoAdivinha()
print("JOGO ENCERRADO")
  
  
