import random




#função
def jogoAdvinha():
    s = 'Sim'
    while s == "Sim":
        numero_sorteado = random.randint(1,1023)
        print("<---------------Jogo da Adivinhação---------------->")
        print(numero_sorteado)
        numero_adivinha = 0
        contador = 1
        numero_adivinha = 0
        
        
        while numero_adivinha != numero_sorteado:
          numero_adivinha = (input("Digite número:"))
          ehNumero = numero_adivinha.isnumeric()
          
          while ehNumero is False:
            numero_adivinha = (input("Digito inválido, tente novamente:"))
            ehNumero = numero_adivinha.isnumeric()
            if ehNumero is True:
              
              break
              
          while 0 < int(numero_adivinha) > 1023:
            numero_adivinha = int(input("Número inválido digite novamente:"))
            
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
        
        s = input("Jogar de Novo: Sim ou Não?")
        if s == "Não":
            print("<---------------ENCERRADO---------------->")
        
#Bloco principal

jogoAdvinha()


