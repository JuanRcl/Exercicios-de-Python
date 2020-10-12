from datetime import date
atual = date.today().year #Pegando o ano atual do sistema
jovem = 0
adulto = 0
for c in range(1,8,1):
    nasc = int(input('{}ª Digite seu ano de nascimento: '.format(c)))
    res=atual-nasc
    if res>=18:
        adulto += 1
    else:
        jovem += 1
print('Temos {} jovens e {} adultos'.format(jovem, adulto))