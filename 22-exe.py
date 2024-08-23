#CRIE UM PROGRMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE
#O NOME EM MAIÚSCULAS E MINÚSCULAS
#QUANTAS LETRAS TEM O NOME AOTODOS
#QUANTAS LETRAS TEM O PRIMEIRO NOME.

nome = str(input('Qual o seu nome: ')).strip()

print('Analisando o seu nome...')
print('Seu nome em maiúscula é {}' .format(nome.upper()))
print('Seu nome  em minúscula é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))