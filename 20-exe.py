#O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS.
#FAÇA UM PROGRAMA QUE LEIA O NOME DOS ALUNOS E MOSTRE A ORDEM SORTEADA.

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)