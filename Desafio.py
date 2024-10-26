# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 09:08:40 2023

@author: c2320462
"""
"""




imposto = float(1.15)

peso = float(input("Digite o peso dos peixes: "))
total_imposto_kg = peso*imposto
quota = float(50)


print("O peso total dos peixes é: %.2fkg" %peso)


if peso > quota:
    quilo_excedente = abs(quota - peso)
    multa = float(quilo_excedente*4)
    if multa > 1000:
        print("A sua multa será: $1000.00")
        imposto_total = total_imposto_kg + multa
        print("Você deve a receita federal: %.2f" %imposto_total)
    else:
        print("A sua multa será: $%.2f " %multa)
        imposto_total = total_imposto_kg + multa
        print("Você deve a receita federal: $%.2f" %imposto_total)

else:
    print("Você não pagará multa")
    print("Você deve a receita federal: $%.2f" %total_imposto_kg)
"""
        


#Desafio 2

candidatos = int(input("Entre com numero de candidatos: "))
contador = 0
aprovados = 0
reprovado = 0

while candidatos <= contador:
    nome = input("Nome:")
    print(nome)
    nota1 = int(input(""))
    nota2 = int(input(""))
    nota3 = int(input(""))
    nota4 = int(input(""))
    nota5 = int(input(""))
    nota6 = int(input(""))
    
    media = (nota1+nota2+nota3+nota4+nota5+nota6)/6
    print("A media de %s é %.1f" %(media, nome))
    if media > 80:
        print("Aprovado")
        aprovados = aprovados + 1
    else:
        print("Reprovado")
        reprovado = reprovado + 1
        
        
    contador = contador + 1


print("A quantidade de aprovados é %d" %aprovados)
print("A quantidade de reprovados é %d" %reprovado)
