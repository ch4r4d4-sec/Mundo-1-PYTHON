#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E O MENOR.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

#Verificar quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n2 < n3:
    menor = n3
#Verificar quem é maior
if n2 > n1 and n2 > n3:
    maior = n2 
if n3 > n1 and n3 > n2:
    maior = n3

print('O manor valor digitado foi {}' .format(menor))
print('O maior valor digitado foi {}' .format(maior))