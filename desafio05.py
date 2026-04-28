# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int (input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))
# print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}').format(n, (n-1), (n+1))

# A primeira opção de print pode ser usada se for precisar usar a informação futuramente, use esta opção.
# Caso não precise, se a opção 2