# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:31:10 2023

@author: c2320462
"""
"""
#Exercício 1
def calcula_média(nota1, nota2):

    media = (nota1 + nota2)/2
    print("A sua média é: %.1f" %media)
    #Função
    if media >= 5:
        print('Aprovado')

    else:
        print('Reprovado')

    return media

nota1 = float(input("Insira a primeira nota:"))
nota2 = float(input("Insira a segunda nota:"))

saber_situacao = calcula_média(nota1,nota2)

print(saber_situacao)
    
#Exercício 2
#Declaração da váriaveis:
#Valor de uma prestação(vp)
vp = 1500

# o tempo de atraso do pagamento(t em dias)
t = 30

# taxa de juros diária (i) 
i = 2

#Função

if t > 10:
    te = t - 10
    #o montante a ser pago(m)
    vf = input('Insira o valor fixo:\t')
    m = vp + (vp * i / 100 * t) + vf * te

else:
    #o montante a ser pago(m)
    m = vp + (vp * i / 100 * t)
    
"""

