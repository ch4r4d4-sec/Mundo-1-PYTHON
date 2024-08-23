#FAÇA UM PROGRAMA QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE O SEU NOVO SALÁRIO COM 15% DE AUMENTO

salario = float(input('Qual o seu salário? R$ '))
novo = salario + (salario * 15 / 100)

print('Um funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa areceber R$ {:.2f}' .format(salario, novo))