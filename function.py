idade = int(input('Digite sua idade: '))
nome = input('Digite seu nome: ')
if idade<18:
    print('Bem vindo {}, você ainda é uma pessoa jovem com {}!'.format(nome,idade))
else:
    print('Bem vindo {}, você ainda é uma pessoa com experiencia de vida, com {}!'.format(nome, idade))
