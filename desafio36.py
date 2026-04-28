#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.Pergunte o valor da casa, o salario do comprador
#e em quantos anos ele vai pagar.
#A prestação mensal, não pode exceder 30% do salario ou então o emprestimo será negado.

casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Quanto você recebe por mês: R$ '))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa /(anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestação))
if prestação <=minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')

