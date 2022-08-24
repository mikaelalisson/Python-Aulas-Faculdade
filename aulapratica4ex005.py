print('CINEMA')

total = 0
dinheiro = 0
while True:
    idade = input('Por favor digite a sua idade: ')
    if idade == 'sair':
        print('Saindo...')
        break
    idade = int(idade)

    total += 1

    if (idade < 3):
        ingresso = 0
    elif (idade >= 3 and idade < 12):
        ingresso = 15
    else:
        ingresso = 30

    dinheiro += ingresso

media = dinheiro / total
print('Total de pessoas {}' .format(total))
print('Total de dinheiro ${:.2f}'.format(dinheiro))
print('Media de valores ${:.2f}'.format(media))