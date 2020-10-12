n = int(input('Digite um número de 0 a 10: '))
for c in range(0,11,1):
    print('{} x {} = {}'.format(n, c, n*c))