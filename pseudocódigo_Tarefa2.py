# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:27:45 2023

@author: c2320462
"""
"""

#Exercício 1

def calcula_tamanho(altura_inicial, taxa_crescimento, n):
    altura_final = altura_inicial

    for ano in range(n):
        altura_final = altura_final + altura_final * taxa_crescimento

    return altura_final

#solicitar ao úsuario que insira os dados
altura_inicial = float(input("Digite a altura inicial da árvore: "))
taxa_crescimento = float(input("Digite a taxa de crescimento anual (em decimal): "))
n = int(input("Digite a quantidade de anos: "))
altura_final = altura_inicial

altura_final = calcula_tamanho(altura_inicial, taxa_crescimento, n)

print(f"A altura da árvore após {n} anos é: {altura_final} metros")


#Exercício 2
def calcula_tempo_para_duplicar(capital_inicial, taxa_de_juros):
    saldo = capital_inicial
    anos = 0

    while saldo < capital_inicial*2:
        saldo = saldo + taxa_de_juros*saldo
        anos = anos + 1

    return anos

capital_inicial = float(input("Digite o valor inicial aplicado: "))
taxa_de_juros = float(input("Digite a taxa de juros anual (em decimal): "))

anos_duplica = calcula_tempo_para_duplicar(capital_inicial, taxa_de_juros)

print(anos_duplica)

#Exercício 3
lista = []
i = 0

for i in range(6):
    lista.append(int(input('insira idade:')))
    i = i + 1
   
quantidade = 0
soma = 0

#Para saber a média
for valores in lista:
    quantidade = quantidade + 1
    soma = soma + valores
media = soma/quantidade

#Para contar valores menores de 18 anos
cont = 0 
for x in lista:
    if x < 18:
        cont = cont + 1

#Para contar valores maiores de 20 anos
cont2 = 0 
for x in lista:
    if x > 20:
        cont2 = cont2 + 1
            
maior_idade = max(lista)
print("A média das idades é: %d" %media)
print("A maior idade é:%d" %maior_idade)
print("A quantidade de pessoas menores de 18 anos são: %d" %(cont))

percental = cont2/len(lista)*100
print("O percentual de pessoas com idade maior que 20 anos é: %.2f" %percental)

"""
