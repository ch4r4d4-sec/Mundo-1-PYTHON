#FAÇA UM PROGRAMA QUE LEIA UM VALOR EM METROS E MOSTRE COVERTIDO EM CENTIMETROS E MILIMETROS.

medida = float(input('Uma distancia me metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10

print('A medida de {} metros corresponde em centimetro {:.0f} CM \nem milimetro {:.0f} MM \nem quilometros {:.0f} KM \nem Hectómetro {:.0f} HM \nem Decâmetro {:.0f} DAM \nem decimetro {:.0f} DM' .format(medida, cm, mm, km, hm, dam, dm))