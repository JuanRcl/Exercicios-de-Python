km = float(input('Quantos kilometros tem a viagem pro seu destino?: '))
if km <=200:
    preco = km*0.50
    print('O preço da viagem é: R${:.2f}'.format(preco))
else:
    preco = km*0.45
    print('O preço da viagem é: R${:.2f}'.format(preco))