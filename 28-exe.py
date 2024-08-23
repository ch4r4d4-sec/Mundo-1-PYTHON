#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USÚARIO TENTTAR DESCOBRIR
#QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR. O PROGRAMA DEVERÁ EXCREVER NA TELA SE O USÚARIO VENCEU.

from random import randint
from time import sleep

computador = randint(0, 5) #FAZ O COMPUTADOR 'PENSAR'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(1.2)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!' .format(computador, jogador))