#FAÇA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
#PARA SALÁRIOS SUPERIORES A R$1,2500,00 , CALCULE UM AUMENTO DE 10% . PARA INFERIORES OU IGUAIS , O AUMENTO É DE 15%

salario = float(input('Qual é o salário do funcionário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganha R${:.2f} passa a ganhar R${:.2f}' .format(salario, novo))