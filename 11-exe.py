#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A ÁREA E A QUANTIDADE DE TINTA PARA PINTAR
#SABENDO QUE A CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M²

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt 
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².' .format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.' .format(tinta))