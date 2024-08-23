#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER E MOSTRE NA TELA A SUA PORÇÃO INTEIRA.

from math import trunc
#import math

num = float(input('Digite um número: '))

#print('O valor digitado foi {} e sua porção inteira é {}' .format(num, math.trunc(num)))

print('O valor digitado foi {} e sua porção inteira é {}' .format(num, trunc(num)))