#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

N = int(input('Me diga um número qualquer: '))
resultado = N % 2 #O resto da divisão de qualquer número par por 2 é zero e o resto da divisão de qualquer número impar é 1.
if resultado == 0:
    print('O número {} é PAR'.format(N))
else:
    print('O número {} é IMPAR'.format(N))