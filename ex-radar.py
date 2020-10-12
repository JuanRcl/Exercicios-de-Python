vel = float(input('Informe a velocidade: '))
if vel<=80:
    print('Velocidade normal!')
else:
    multa = (vel-80)*7
    print('Sua velocidade é {}km e o limite é 80km, então você foi multado no valor de R${:.2f}'.format(vel, multa))
