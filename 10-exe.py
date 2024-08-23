#FAÇA UM PROGRAMA QUE LEIA QUANDO DINHEIRO UMA PESSOA TEM N A CARTEIRA E MOSTRE QUANTOS DOLARES PODE COMPRAR.

real = float(input('Quantos reias você tem? R$ '))
dolarHoje = 5.24
possoComprar = real / dolarHoje

print('Eu tenho na carteira R$ {} rais e o dolar ta custando hoje US$ {} com isso posso comprar US$ {:.2f} dolares' .format(real, dolarHoje, possoComprar))