from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
n5 = input('Quinto nome: ')
lista = [n1, n2, n3, n4, n5]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

