#FAÇA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM
#COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS.

distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.' .format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}' .format(preco))