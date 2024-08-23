#FAÇA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO
#CALCULE O PREÇO A APAGAR, SABENDO QUE O CARRO CUSTA r$ 60 POR DIA 3 r$ 0,15 POR KM RODADO

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R$ {:.2f}' .format(pago))