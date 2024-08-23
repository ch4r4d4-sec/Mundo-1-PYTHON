#FAÇA UM PROGRAMA QUE CONVERTA EM TEMPERATURA DIGITADA EM °C E CONVERTA PARA °F

c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32

print('A temperatura de {}°C corresponde a {}°F!' .format(c, f))