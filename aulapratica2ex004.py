d = int(input('Digite a quantidade de dias: '))
h = int(input('Digite a quantidade de horas: '))
m = int(input('Digite a quantidade de minutos: '))
s = int(input('Digite a quantidade de segundos: '))
ts = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)
print('O total de segundos contabilizados foi de {}' .format(ts))