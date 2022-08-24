print('CALCULADORA')
print('+ ADIÇÃO')
print('- SUBTRAÇÃO')
print('* MULTIPLICAÇÃO')
print('/ DIVISÃO')
print('Pressiona qualquer tecla para SAIR')


op =input('Digite a OPERAÇÃO que deseja fazer: ')

if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o PRIMEIRO valor: '))
    y = int(input('Digite o SEGUNDO valor: '))

while(op != 's'):
    if (op == '+'):
        res = (x + y)
        print('Resultado: {} + {} = {}'.format(x,y,res))
    elif (op == '-'):
        res = (x - y)
        print('Resultado: {} - {} = {}'.format(x, y, res))
    elif (op == '*'):
        res = (x * y)
        print('Resultado: {} * {} = {}'.format(x, y, res))
    elif (op == '/'):
        res = (x / y)
        print('Resultado: {} / {} = {}'.format(x, y, res))
    else:
        print('Você digitou uma operação inválida')

    op = input('Digite a OPERAÇÃO que deseja fazer: ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o PRIMEIRO valor: '))
        y = int(input('Digite o SEGUNDO valor: '))

print('Encerrando o programa---')