#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE É IMPAR OU PAR.

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2

if resultado == 0:
    print('O número {} é PAR' .format(numero))
else:
    print('O número {} é IMPAR' .format(numero))