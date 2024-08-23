#FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELE.

a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaço? ', a.isspace())
print('É um alfabético? ', a.isalpha())
print('É um número? ', a.isnumeric())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúscula? ', a.isupper())
print('Está em minúscula? ', a.islower())
print('Está capitalizada? ', a.istitle())