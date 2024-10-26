# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:18:37 2023

@author: aluno

Faça um programa que leia uma sequência de 10 notas de alunos e informe 
quantos alunos passaram direto em CTC4002 (média 6)
"""

i = 0

while (i<=10):
    aluno = input('Nome:')
    nota = int(input('Nota:'))
    
    if (nota >= 6):
        print('Parabéns, passou"')
    else:
        print('ops!')
    i = i + 1
    
'''FIM'''
