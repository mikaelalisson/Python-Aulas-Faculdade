preco = float(input('Digite o valor do produto: '))
p = float(input('Digite o percentual de desconto (0-100)%: '))
desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é {}. O valor do desconto foi de: {}' .format(preco, p))
print('Valor calculado do DESCONTO {}. Valor do produto final {}' .format(desconto, final))