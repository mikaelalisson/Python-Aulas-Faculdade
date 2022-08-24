print('CALCULADORA')
print('+ ADIÇÃO')
print('- SUBTRAÇÃO')
print('* MULTIPLICAÇÃO')
print('/ DIVISÃO')
print('Pressiona qualquer tecla para SAIR')


while True:
    op = input('Digite a OPERAÇÃO que deseja fazer: ')

    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o PRIMEIRO valor: '))
        y = int(input('Digite o SEGUNDO valor: '))

    if (op == '+'):
        res = (x + y)
        print('Resultado: {} + {} = {}'.format(x,y,res))
        continue
    elif (op == '-'):
        res = (x - y)
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif (op == '*'):
        res = (x * y)
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res = (x / y)
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif(op == 's'):
        break
    else:
        print('Você digitou uma operação inválida')

print('Encerrando o programa---')