#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO,
#CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}' .format(hi))