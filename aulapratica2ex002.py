km = int(input('Quantos KM você rodou?'))
dia = int(input('Quantos dias você usou o carro?'))

preco = 60 * dia + 0.15 * km

print('A distância percorrida foi de {}km por um total de {} dias' .format(km,dia))
print('Valor a ser pago:{}R$'.format(preco))