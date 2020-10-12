from random import choice
lista = [1,2,3,4,5]
escolhido = choice(lista)
n = int(input('Digite um número de 1 a 5: '))
if n == escolhido:
    print('Parabens, você ACERTOU o número!!')
else:
    print('Infelizmente você NÃO acertou, o numero certo era {}'.format(escolhido))

