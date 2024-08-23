#CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO,TRIPLO E RAIZ QUADRADA.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O doblo de {} vale {}.' .format(n, d))
print('O triplo de {} vale {}.' .format(n, t))
print('A raiz quadrada de {} vale {:.2f}.' .format(n,r))