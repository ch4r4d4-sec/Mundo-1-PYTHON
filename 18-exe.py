#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.

import math 

angulo = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}' .format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem COSSENO de {:.2f}' .format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(angulo, tangente)) 