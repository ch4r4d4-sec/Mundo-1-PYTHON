#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO .
#SE ELE ULTRAPASSAR 80KM;G. MOSTRE UMA MENSAGEM DIZENDO QUE LE FOI MULTADO
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar um amulta de R$ {:.2f}!' .format(multa))
print('Tenha um bom dia! Dirija com segurança!')