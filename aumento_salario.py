sal = float(input('Informe seu salário atual: '))
if sal>1250:
    saln = (sal*0.10)+sal
    print('Seu salário novo é R${}'.format(saln))
else:
    saln = (sal*0.15)+sal
    print('Seu salário novo é R${:.2f}'.format(saln))